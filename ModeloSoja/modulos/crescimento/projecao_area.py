import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class ProjecaoArea:
    """
    Modelo logístico para projeção de área plantada (limita o crescimento ao território disponível).
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, limite_maximo=45000):
        self.limite = limite_maximo # mil hectares
        
    def ajustar_e_projetar(self, anos_hist, area_hist, anos_futuros):
        # Transformação Logit para garantir assíntota
        # y = L / (1 + exp(-k(x-x0)))
        # Linearizando: ln(L/y - 1) = -kx + kx0
        
        y = area_hist.values
        # Evitar divisão por zero ou log de zero
        y = np.clip(y, 1, self.limite - 1)
        
        logit_y = np.log(self.limite / y - 1)
        X = anos_hist.reshape(-1, 1)
        
        modelo = LinearRegression()
        modelo.fit(X, logit_y)
        
        X_fut = anos_futuros.reshape(-1, 1)
        pred_logit = modelo.predict(X_fut)
        
        # Voltando para escala original
        pred_y = self.limite / (1 + np.exp(pred_logit))
        
        return pd.Series(pred_y, index=anos_futuros, name='Projecao_Area_Logistica')
