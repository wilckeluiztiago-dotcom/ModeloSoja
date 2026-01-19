import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class GraficoMapaRisco:
    """
    Gera heatmap de risco de seca por ano e estado.
    Autor: Luiz Tiago Wilcke
    """
    
    def gerar(self, df_risco, arquivo_saida):
        """
        :param df_risco: DataFrame com index=Anos, columns=Estados, values=Probabilidade Seca
        """
        plt.figure(figsize=(14, 8))
        
        sns.heatmap(
            df_risco.T, 
            cmap='RdYlGn_r', # Vermelho = alto risco, Verde = baixo risco
            annot=True, 
            fmt=".2f",
            linewidths=.5,
            cbar_kws={'label': 'Probabilidade de Seca Severa'}
        )
        
        plt.title('Mapa de Calor: Risco de Seca Severa por Estado (2027-2050)', fontsize=16)
        plt.xlabel('Ano Projetado')
        plt.ylabel('Estado')
        
        plt.tight_layout()
        plt.savefig(arquivo_saida, dpi=300)
        plt.close()
