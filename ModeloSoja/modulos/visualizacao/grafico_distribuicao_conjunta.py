import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class GraficoDistribuicaoConjunta:
    """
    Gera Joint Plot para visualizar a correlação de riscos entre dois estados.
    Autor: Luiz Tiago Wilcke
    """
    
    def gerar(self, serie_risco_estado1, serie_risco_estado2, nome1, nome2, arquivo_saida):
        df = pd.DataFrame({
            nome1: serie_risco_estado1,
            nome2: serie_risco_estado2
        })
        
        sns.set_theme(style="darkgrid")
        
        g = sns.jointplot(
            x=nome1, 
            y=nome2, 
            data=df,
            kind="kde", # Kernel Density Estimation
            fill=True,
            cmap="Reds",
            thresh=0.05
        )
        
        g.fig.suptitle(f'Densidade Conjunta de Risco: {nome1} vs {nome2}', y=1.02)
        
        plt.savefig(arquivo_saida, dpi=300)
        plt.close()
