from .modelo_arima import ModeloARIMA

class ModeloEstadoMS(ModeloARIMA):
    """
    Modelo para Mato Grosso do Sul.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'MS', ordem=(2, 1, 2)) # Ciclos mais complexos

    def projetar(self, anos_futuros):
        return super().projetar(anos_futuros)
