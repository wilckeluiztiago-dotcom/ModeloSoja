import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing

class AnalisadorSerieTemporal:
    """
    Wrapper para modelos de séries temporais avançados.
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_serie):
        """
        :param dados_serie: Pandas Series com índice temporal.
        """
        self.dados = dados_serie
        
    def ajustar_arima(self, ordem=(1, 1, 1)):
        """Ajusta um modelo ARIMA."""
        modelo = ARIMA(self.dados, order=ordem)
        resultado = modelo.fit()
        return resultado
        
    def ajustar_holt_winters(self, sazonalidade='add', periodos_sazonais=12):
        """Ajusta Suavização Exponencial Holt-Winters."""
        modelo = ExponentialSmoothing(
            self.dados, 
            seasonal=sazonalidade, 
            seasonal_periods=periodos_sazonais,
            trend='add'
        )
        resultado = modelo.fit()
        return resultado
        
    def prever(self, modelo_ajustado, passos=10):
        """Gera previsões futuras."""
        return modelo_ajustado.forecast(steps=passos)
