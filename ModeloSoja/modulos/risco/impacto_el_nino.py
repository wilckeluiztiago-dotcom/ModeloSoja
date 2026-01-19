import pandas as pd
import numpy as np

class ImpactoElNino:
    """
    Analisa correlação entre ONI (Oceanic Niño Index) e produtividade no Sul.
    No sul do Brasil, El Niño aumenta chuva (bom/excesso) e La Niña causa seca (ruim).
    No Matopiba/Nordeste, El Niño causa seca.
    Autor: Luiz Tiago Wilcke
    """
    
    def ajustar_fator_regiao(self, previsao_base, regiao, indice_enso_futuro):
        """
        :param regiao: 'SUL' ou 'NORDESTE' ou 'CENTRO-OESTE'
        :param indice_enso_futuro: Array de índices (+1.0 El Nino, -1.0 La Nina)
        """
        fator = np.ones_like(indice_enso_futuro)
        
        if regiao == 'SUL':
            # La Niña (negativo) é ruim para o Sul
            fator = np.where(indice_enso_futuro < -0.5, 0.85, fator)
            fator = np.where(indice_enso_futuro > 0.5, 1.10, fator) # El Niño chove bem
            
        elif regiao in ['NORDESTE', 'MATOPIBA']:
            # El Niño (positivo) é muito ruim para o Nordeste (seca)
            fator = np.where(indice_enso_futuro > 0.5, 0.80, fator)
            fator = np.where(indice_enso_futuro < -0.5, 1.05, fator) # La Niña chove
            
        return previsao_base * fator
