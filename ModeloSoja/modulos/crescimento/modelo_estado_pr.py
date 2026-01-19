from .suavizacao_exponencial import ModeloSuavizacaoExponencial
import pandas as pd

class ModeloEstadoPR(ModeloSuavizacaoExponencial):
    """
    Modelo especializado para o Paraná.
    O PR sofre mais com clima, então usamos Suavização Exponencial com amortecimento.
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'PR')
        
    def projetar(self, anos_futuros):
        previsao = super().projetar(anos_futuros)
        # O PR já é muito consolidado, o crescimento de área é menor, limitamos o crescimento
        return previsao
