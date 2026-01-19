from .tendencia_linear import ModeloTendenciaLinear

class ModeloEstadoPI(ModeloTendenciaLinear):
    """
    Modelo para Piauí.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'PI')
