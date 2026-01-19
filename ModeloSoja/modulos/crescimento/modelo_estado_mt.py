from .modelo_arima import ModeloARIMA
import pandas as pd

class ModeloEstadoMT(ModeloARIMA):
    """
    Modelo especializado para o Mato Grosso.
    O MT tem crescimento muito estável e forte, usamos um ARIMA com componente MA maior.
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_historicos):
        # MT geralmente tem tendência forte (d=1) e inércia (ar=1, ma=1)
        super().__init__(dados_historicos, 'MT', ordem=(1, 1, 2))
        
    def projetar(self, anos_futuros):
        previsao_base = super().projetar(anos_futuros)
        # Aplicar um fator de correção específico de tecnologia para o MT (+1% ao ano extra boost)
        fator_tecnologia = [1.01 ** i for i in range(len(previsao_base))]
        return previsao_base * fator_tecnologia
