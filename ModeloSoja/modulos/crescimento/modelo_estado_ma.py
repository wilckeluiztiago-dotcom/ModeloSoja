from .modelo_arima import ModeloARIMA

class ModeloEstadoMA(ModeloARIMA):
    """
    Modelo para Maranhão. Fronteira agrícola.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'MA', ordem=(1, 2, 1)) # I=2 para capturar aceleração
