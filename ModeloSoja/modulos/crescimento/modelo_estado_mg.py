from .modelo_arima import ModeloARIMA

class ModeloEstadoMG(ModeloARIMA):
    """
    Modelo para Minas Gerais.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'MG', ordem=(0, 1, 1))
