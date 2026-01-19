from .modelo_arima import ModeloARIMA
import numpy as np

class ModeloEstadoRS(ModeloARIMA):
    """
    Modelo especializado para o Rio Grande do Sul.
    Altíssima volatilidade devida a secas.
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_historicos):
        super().__init__(dados_historicos, 'RS', ordem=(2, 1, 0)) # Mais AR para capturar ciclos
        
    def projetar(self, anos_futuros):
        previsao = super().projetar(anos_futuros)
        # Simula ciclos de quebra a cada 4-5 anos (El Niño/La Niña proxys)
        for i, ano in enumerate(anos_futuros):
            if ano % 5 == 0: # Anos críticos
                previsao.iloc[i] *= 0.75 # Quebra de 25%
        return previsao
