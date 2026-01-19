import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.cm as cm

class GraficoSuperficieRisco:
    """
    Gera gráfico 3D de superfície mostrando Risco x Tempo x Latitude (proxy do Estado).
    Autor: Luiz Tiago Wilcke
    """
    
    def gerar(self, dados_risco_matrix, anos, estados, arquivo_saida):
        """
        :param dados_risco_matrix: Matrix (N_estados x N_anos)
        """
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Grid X (Anos), Y (Indices Estados)
        X, Y = np.meshgrid(range(len(anos)), range(len(estados)))
        Z = np.array(dados_risco_matrix)
        
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        
        ax.set_xticks(range(0, len(anos), 5))
        ax.set_xticklabels(anos[::5])
        
        ax.set_yticks(range(len(estados)))
        ax.set_yticklabels(estados)
        
        ax.set_zlabel('Probabilidade de Seca Severa')
        ax.set_xlabel('Anos')
        ax.set_ylabel('Estados')
        
        plt.title('Superfície 3D: Evolução do Risco Climático (2027-2050)', fontsize=14)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        
        plt.tight_layout()
        plt.savefig(arquivo_saida, dpi=300)
        plt.close()
