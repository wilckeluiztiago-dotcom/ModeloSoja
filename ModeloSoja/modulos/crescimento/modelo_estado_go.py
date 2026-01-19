from .modelo_arima import ModeloARIMA

class ModeloEstadoGO(ModeloARIMA):
    """
    Modelo para Goiás. Alta tecnologia, crescimento consistente.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'GO', ordem=(1, 1, 1))

    def projetar(self, anos_futuros):
        return super().projetar(anos_futuros)
