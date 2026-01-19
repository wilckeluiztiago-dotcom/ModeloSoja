from abc import ABC, abstractmethod
import pandas as pd

class ModeloCrescimentoBase(ABC):
    """
    Classe base abstrata para todos os modelos de crescimento de soja.
    Autor: Luiz Tiago Wilcke
    """
    
    def __init__(self, dados_historicos, estado_alvo):
        self.dados = dados_historicos
        self.estado = estado_alvo
        self.modelo_ajustado = None
        
    @abstractmethod
    def treinar(self):
        pass
        
    @abstractmethod
    def projetar(self, anos_futuros):
        pass
        
    def obter_dados_estado(self):
        """Filtra os dados apenas para o estado alvo."""
        return self.dados[self.dados['Estado'] == self.estado]['Producao_Mil_Toneladas']
