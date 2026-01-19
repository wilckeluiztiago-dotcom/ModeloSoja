import numpy as np

class SimulacaoMonteCarloClima:
    """
    Simulação Estocástica de Cenários Climáticos Futuros (2027-2050).
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, n_simulacoes=1000):
        self.n_simulacoes = n_simulacoes
        
    def simular_precipitacao(self, media_hist, desvio_hist, anos_futuros):
        """
        Gera múltiplos cenários de precipitação baseados na estatística histórica.
        """
        n_anos = len(anos_futuros)
        
        # Matriz (Simulações x Anos)
        cenarios = np.random.normal(
            loc=media_hist, 
            scale=desvio_hist, 
            size=(self.n_simulacoes, n_anos)
        )
        
        return cenarios
        
    def calcular_risco_abaixo_limite(self, cenarios, limite_critico):
        """
        Calcula a % de simulações que ficaram abaixo de um nível crítico de chuva.
        """
        abaixo_limite = (cenarios < limite_critico).sum(axis=0)
        probabilidade_risco = abaixo_limite / self.n_simulacoes
        return probabilidade_risco
