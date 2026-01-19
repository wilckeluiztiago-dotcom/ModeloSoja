import numpy as np
import scipy.stats as stats
from ..estatistica.distribuicoes import DistribuidorEstatistico

class IndiceSPI:
    """
    Calculadora do Standardized Precipitation Index (SPI).
    Mede a severidade da seca baseada em probabilidade de precipitação.
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_precipitacao):
        """
        :param dados_precipitacao: Array com valores mensais ou anuais de chuva (mm).
        """
        self.dados = np.array(dados_precipitacao)
        
    def calcular(self):
        """
        Ajusta uma distribuição Gamma e transforma em Z-score normal.
        """
        # Tratar zeros (chuva zero) que a Gamma não suporta direto
        zeros = self.dados == 0
        n_zeros = np.sum(zeros)
        n = len(self.dados)
        prob_zero = n_zeros / n
        
        dados_non_zero = self.dados[~zeros]
        
        if len(dados_non_zero) < 5:
            return np.zeros(n) # Dados insuficientes
            
        alpha, loc, scale = DistribuidorEstatistico.ajustar_gamma(dados_non_zero)
        
        # CDF da Gamma
        cdf_gamma = stats.gamma.cdf(dados_non_zero, alpha, loc=loc, scale=scale)
        
        # Probabilidade combinada (incluindo os zeros)
        H_x = prob_zero + (1 - prob_zero) * cdf_gamma
        
        # Transformada Inversa da Normal (Z-score)
        spi = stats.norm.ppf(H_x)
        
        # Reintegrar zeros (que terão valores muito negativos no SPI)
        spi_final = np.zeros(n)
        spi_final[~zeros] = spi
        # Para os zeros, usamos uma aproximação de 'seca extrema'
        if n_zeros > 0:
            spi_final[zeros] = -3.0 
            
        return spi_final
