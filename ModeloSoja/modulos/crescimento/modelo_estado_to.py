from .tendencia_linear import ModeloTendenciaLinear

class ModeloEstadoTO(ModeloTendenciaLinear):
    """
    Modelo para Tocantins. Crescimento linear forte de área.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'TO')
