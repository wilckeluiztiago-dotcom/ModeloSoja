from .suavizacao_exponencial import ModeloSuavizacaoExponencial

class ModeloEstadoSC(ModeloSuavizacaoExponencial):
    """
    Modelo para Santa Catarina. Pequenas propriedades, estável.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'SC')
