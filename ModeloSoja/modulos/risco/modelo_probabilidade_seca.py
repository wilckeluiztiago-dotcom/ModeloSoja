from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

class ModeloProbabilidadeSeca:
    """
    Modelo Logit para prever probabilidade de ocorrência de seca severa (SPI < -1.5).
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self):
        self.modelo = LogisticRegression()
        
    def treinar(self, features_climaticas, target_binario_seca):
        """
        :param features_climaticas: Matriz X (Temp, El Nino Index, etc)
        :param target_binario_seca: Vetor y (1 se houve seca, 0 caso contrário)
        """
        self.modelo.fit(features_climaticas, target_binario_seca)
        
    def prever_probabilidade(self, features_futuras):
        # Retorna a probabilidade da classe 1 (Seca)
        probs = self.modelo.predict_proba(features_futuras)[:, 1]
        return probs
