import numpy as np

class CalculadoraVaR:
    """
    Calculadora de Value at Risk (VaR) e Expected Shortfall (ES).
    Métricas de risco financeiro aplicadas à produção agrícola.
    Autor: Luiz Tiago Wilcke
    """
    
    def calcular_var_historico(self, distribuicao_perdas, nivel_confianca=0.95):
        """
        Retorna o VaR: a perda máxima que não será excedida com X% de confiança.
        Se distribuicao_perdas são valores positivos de perda.
        Se forem retornos, procuramos o quantil da cauda esquerda.
        Aqui assumimos distribuicao_perdas como (Producao_Potencial - Producao_Real).
        """
        return np.percentile(distribuicao_perdas, 100 * nivel_confianca)
        
    def calcular_expected_shortfall(self, distribuicao_perdas, nivel_confianca=0.95):
        """
        CVaR (Conditional VaR): média das perdas nos piores (1-confianca)% casos.
        """
        var = self.calcular_var_historico(distribuicao_perdas, nivel_confianca)
        perdas_cauda = distribuicao_perdas[distribuicao_perdas >= var]
        return np.mean(perdas_cauda)
