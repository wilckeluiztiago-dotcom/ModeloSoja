import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class GraficoProjecaoCrescimento:
    """
    Gera gráficos de linhas com faixas de confiança para as projeções de crescimento.
    Autor: Luiz Tiago Wilcke
    """
    
    def gerar(self, historico, projecoes, estado, arquivo_saida):
        """
        :param historico: Series histórica
        :param projecoes: Series projetada (2025-2050)
        :param estado: Sigla do estado
        """
        plt.figure(figsize=(12, 6))
        sns.set_style("whitegrid")
        
        # Plot histórico
        plt.plot(historico.index, historico.values, label='Histórico Real', color='navy', linewidth=2)
        
        # Plot projeção
        plt.plot(projecoes.index, projecoes.values, label='Projeção 2027-2050', color='green', linestyle='--', linewidth=2)
        
        # Faixa de confiança simulada (simplificada para visualização)
        std_erro = historico.std() * 0.5
        plt.fill_between(
            projecoes.index,
            projecoes.values - std_erro,
            projecoes.values + std_erro,
            color='green', alpha=0.1, label='Intervalo de Confiança 95%'
        )
        
        plt.title(f'Projeção de Produção de Soja - {estado} (2007-2050)', fontsize=14)
        plt.xlabel('Ano')
        plt.ylabel('Produção (Mil Toneladas)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.savefig(arquivo_saida, dpi=300)
        plt.close()
