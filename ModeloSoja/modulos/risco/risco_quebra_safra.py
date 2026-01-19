import numpy as np

class RiscoQuebraSafra:
    """
    Módulo que conecta índices de seca à perda de produtividade.
    Autor: Luiz Tiago Wilcke
    """
    
    def calcular_perda_estimada(self, spi_futuro, produtividade_base):
        """
        Calcula perda baseada no SPI.
        SPI < -1.0: Seca Moderada (-10% perda)
        SPI < -1.5: Seca Severa (-25% perda)
        SPI < -2.0: Seca Extrema (-50% perda)
        """
        
        perda_fator = np.zeros_like(spi_futuro)
        
        # Definindo faixas de risco
        mask_moderada = (spi_futuro < -1.0) & (spi_futuro >= -1.5)
        mask_severa = (spi_futuro < -1.5) & (spi_futuro >= -2.0)
        mask_extrema = (spi_futuro < -2.0)
        
        perda_fator[mask_moderada] = 0.10
        perda_fator[mask_severa]   = 0.25
        perda_fator[mask_extrema]  = 0.50
        
        produtividade_corrigida = produtividade_base * (1 - perda_fator)
        perda_toneladas = produtividade_base * perda_fator
        
        return produtividade_corrigida, perda_toneladas, perda_fator
