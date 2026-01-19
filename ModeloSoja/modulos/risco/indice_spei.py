from .indice_spi import IndiceSPI

class IndiceSPEI(IndiceSPI):
    """
    Standardized Precipitation Evapotranspiration Index.
    Considera o balanço hídrico (Precipitação - Evapotranspiração).
    Mais robusto que o SPI em cenários de aquecimento global.
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_precipitacao, dados_evapotranspiracao):
        # O SPEI usa o input D = P - PET
        balanco = np.array(dados_precipitacao) - np.array(dados_evapotranspiracao)
        super().__init__(balanco)
