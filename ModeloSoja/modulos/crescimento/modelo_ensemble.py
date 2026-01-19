import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

class ModeloEnsemble:
    """
    Modelo Híbrido que combina múltiplas técnicas (Stacking/Weighted Average).
    Combina:
    1. Regressão Linear (Tendência)
    2. Holt-Winters (Suavização com Tendência)
    3. ARIMA (Autoregressivo)
    
    A previsão final é uma média ponderada baseada no erro quadrático (MSE).
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_serie):
        self.dados = dados_serie
        self.pesos = {'linear': 0.33, 'hw': 0.33, 'arima': 0.33}
        self.modelos = {}
        
    def treinar(self):
        y = self.dados.values
        X = np.arange(len(y)).reshape(-1, 1)
        
        # 1. Linear
        mod_linear = LinearRegression()
        mod_linear.fit(X, y)
        pred_linear = mod_linear.predict(X)
        self.modelos['linear'] = mod_linear
        
        # 2. Holt-Winters
        try:
            mod_hw = ExponentialSmoothing(self.dados, trend='add', seasonal=None, damped_trend=True).fit()
            pred_hw = mod_hw.fittedvalues.values
            self.modelos['hw'] = mod_hw
        except:
            # Fallback se falhar convergência
            self.modelos['hw'] = None
            pred_hw = pred_linear
            self.pesos['hw'] = 0
            
        # 3. ARIMA
        try:
            mod_arima = ARIMA(self.dados, order=(1,1,1)).fit()
            pred_arima = mod_arima.fittedvalues.values
            self.modelos['arima'] = mod_arima
        except:
            self.modelos['arima'] = None
            pred_arima = pred_linear
            self.pesos['arima'] = 0
            
        # Recalcular pesos baseado em erro inverso (quem erra menos tem mais peso)
        mse_lin = np.mean((y - pred_linear)**2)
        mse_hw = np.mean((y - pred_hw)**2) if self.modelos['hw'] else float('inf')
        mse_ari = np.mean((y - pred_arima)**2) if self.modelos['arima'] else float('inf')
        
        inv_mse = [1/mse_lin, 1/mse_hw, 1/mse_ari]
        total = sum(inv_mse) # Normalizar para soma 1
        
        self.pesos['linear'] = inv_mse[0] / total
        self.pesos['hw'] = inv_mse[1] / total
        self.pesos['arima'] = inv_mse[2] / total
        
    def projetar(self, anos_futuros, n_ultimo_treino):
        steps = len(anos_futuros)
        indices_futuros = np.arange(n_ultimo_treino, n_ultimo_treino + steps).reshape(-1, 1)
        
        # Linear
        y_lin = self.modelos['linear'].predict(indices_futuros)
        
        # HW
        if self.modelos['hw']:
            y_hw = self.modelos['hw'].forecast(steps).values
        else:
            y_hw = np.zeros(steps)
            
        # ARIMA
        if self.modelos['arima']:
            y_ari = self.modelos['arima'].forecast(steps).values
        else:
            y_ari = np.zeros(steps)
            
        # Média Ponderada
        y_final = (y_lin * self.pesos['linear']) + \
                  (y_hw * self.pesos['hw']) + \
                  (y_ari * self.pesos['arima'])
                  
        return pd.Series(y_final, index=anos_futuros)
