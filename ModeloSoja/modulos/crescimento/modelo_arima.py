from .modelo_base import ModeloCrescimentoBase
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

class ModeloARIMA(ModeloCrescimentoBase):
    """
    Modelo AutoRegressivo Integrado de Médias Móveis.
    """
    
    def __init__(self, dados_historicos, estado_alvo, ordem=(1,1,1)):
        super().__init__(dados_historicos, estado_alvo)
        self.ordem = ordem
    
    def treinar(self):
        dados_serie = self.obter_dados_estado()
        # Em dados reais, faríamos um grid search para 'order', aqui fixamos ou passamos param
        self.modelo = ARIMA(dados_serie, order=self.ordem).fit()
        
    def projetar(self, anos_futuros):
        steps = len(anos_futuros)
        previsoes = self.modelo.forecast(steps)
        previsoes.index = anos_futuros
        return previsoes
