from .modelo_base import ModeloCrescimentoBase
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

class ModeloTendenciaLinear(ModeloCrescimentoBase):
    """
    Modelo de Regressão Linear Simples para tendência de longo prazo.
    """
    
    def treinar(self):
        y = self.obter_dados_estado().values
        X = np.arange(len(y)).reshape(-1, 1) # Ano como feature numérica 0, 1, 2...
        
        self.modelo = LinearRegression()
        self.modelo.fit(X, y)
        self.ultimo_indice_treino = len(y)
        
    def projetar(self, anos_futuros):
        indices_futuros = np.arange(
            self.ultimo_indice_treino, 
            self.ultimo_indice_treino + len(anos_futuros)
        ).reshape(-1, 1)
        
        previsoes = self.modelo.predict(indices_futuros)
        
        return pd.Series(previsoes, index=anos_futuros, name='Predicao_Linear')
