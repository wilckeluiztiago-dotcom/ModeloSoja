from .modelo_base import ModeloCrescimentoBase
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import pandas as pd

class ModeloSuavizacaoExponencial(ModeloCrescimentoBase):
    """
    Modelo Holt-Winters para capturar nível e tendência.
    """
    
    def treinar(self):
        dados_serie = self.obter_dados_estado()
        # Usa tendência aditiva, sem sazonalidade anual pois os dados são anuais
        # Se fossem mensais, usaria seasonal='add'
        self.modelo = ExponentialSmoothing(
            dados_serie, 
            trend='add', 
            damped_trend=True,
            initialization_method="estimated"
        ).fit()
        
    def projetar(self, anos_futuros):
        steps = len(anos_futuros)
        previsoes = self.modelo.forecast(steps)
        previsoes.index = anos_futuros
        return previsoes
