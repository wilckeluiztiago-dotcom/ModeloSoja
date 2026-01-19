from scipy.stats import gumbel_r

class DistribuicaoGumbel:
    """
    Modelagem de valores extremos (máximos ou mínimos) de precipitação.
    Útil para prever secas recordes (mínimos extremos).
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_extremos):
        self.dados = dados_extremos
        
    def ajustar(self):
        self.loc, self.scale = gumbel_r.fit(self.dados)
        
    def calcular_periodo_retorno(self, valor):
        """Calcula o tempo médio de retorno para um evento dessa magnitude."""
        prob_excedencia = 1 - gumbel_r.cdf(valor, self.loc, self.scale)
        if prob_excedencia == 0: return float('inf')
        return 1 / prob_excedencia
        
    def prever_evento_anos(self, periodo_retorno):
        """Qual valor esperado para um evento de X anos (ex: seca de 100 anos)"""
        p = 1 - (1/periodo_retorno)
        return gumbel_r.ppf(p, self.loc, self.scale)
