from .suavizacao_exponencial import ModeloSuavizacaoExponencial

class ModeloEstadoBA(ModeloSuavizacaoExponencial):
    """
    Modelo para Bahia (Matopiba). Região de fronteira agrícola, alta volatilidade recente.
    Autor: Luiz Tiago Wilcke
    """
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'BA')
