import numpy as np
import scipy.stats as stats

class DistribuidorEstatistico:
    """
    Classe utilitária para ajustes e gerações de distribuições estatísticas avançadas.
    Autor: Luiz Tiago Wilcke
    """
    
    @staticmethod
    def ajustar_gamma(dados):
        """Ajusta uma distribuição Gamma aos dados."""
        alpha, loc, scale = stats.gamma.fit(dados)
        return alpha, loc, scale
    
    @staticmethod
    def ajustar_normal(dados):
        """Ajusta uma distribuição Normal aos dados."""
        mu, std = stats.norm.fit(dados)
        return mu, std
        
    @staticmethod
    def gerar_gumbel(loc, scale, tamanho):
        """Gera dados de valor extremo (Gumbel)."""
        return stats.gumbel_r.rvs(loc=loc, scale=scale, size=tamanho)

    @staticmethod
    def teste_normalidade(dados):
        """Executa teste de Shapiro-Wilk."""
        stat, p = stats.shapiro(dados)
        return stat, p
