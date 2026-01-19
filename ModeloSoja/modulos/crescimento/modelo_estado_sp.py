from .modelo_arima import ModeloARIMA

class ModeloEstadoSP(ModeloARIMA):
    """
    Modelo para São Paulo. Área convertida de cana, dinâmica complexa.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'SP', ordem=(1, 0, 0))
