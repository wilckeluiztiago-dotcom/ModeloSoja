import numpy as np
import pandas as pd
from scipy.stats import norm, kendalltau

class CopulaGaussianaRisco:
    """
    Modela a estrutura de dependência entre as quebras de safra dos estados.
    Permite simular se uma seca no RS ocorre ao mesmo tempo que no PR (risco sistêmico).
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, residuos_historicos_df):
        """
        :param residuos_historicos_df: DataFrame onde cada coluna é o resíduo (erro) do modelo de um estado.
        """
        self.residuos = residuos_historicos_df
        self.matriz_correlacao = None
        
    def ajustar(self):
        """Calcula a matriz de correlação de Spearman/Kendall ou Pearson dos resíduos."""
        # Usamos correlação de Pearson nos scores normais (abordagem Copula Gaussiana)
        # Primeiro transformamos os dados para [0,1] empiricamente (Rank/N)
        rankings = self.residuos.rank(pct=True)
        # Evitar inf na transformação probit
        rankings = rankings * (len(rankings) / (len(rankings) + 1)) 
        
        # Transformação para Normal Padrão
        z_scores = norm.ppf(rankings)
        z_df = pd.DataFrame(z_scores, columns=self.residuos.columns)
        
        self.matriz_correlacao = z_df.corr()
        
    def simular_cenarios_conjuntos(self, n_anos, n_simulacoes=1000):
        """
        Gera ruídos correlacionados para o futuro.
        """
        if self.matriz_correlacao is None:
            self.ajustar()
            
        medias = np.zeros(len(self.matriz_correlacao))
        cov = self.matriz_correlacao.values
        
        # Gera (N_anos * N_simulacoes, N_estados)
        total_steps = n_anos * n_simulacoes
        ruidos_correlacionados = np.random.multivariate_normal(medias, cov, size=total_steps)
        
        # O output é um dicionário {Estado: Matriz(Simulacoes, Anos)}
        resultado = {}
        cols = self.residuos.columns
        for i, estado in enumerate(cols):
            # Reshape para (Simulacoes, Anos)
            matriz_estado = ruidos_correlacionados[:, i].reshape(n_simulacoes, n_anos)
            resultado[estado] = matriz_estado
            
        return resultado
