import numpy as np

class AnaliseSensibilidade:
    """
    Analisa quão sensível é o modelo final a variações nos parâmetros de entrada.
    Autor: Luiz Tiago Wilcke
    """
    
    def executar(self, modelo_func, input_base, variacao_pct=0.10):
        """
        :param modelo_func: Função que aceita o input e retorna o output
        :param input_base: Valor base da variável
        :param variacao_pct: Quanto variar para +/-
        """
        base_result = modelo_func(input_base)
        
        plus_result = modelo_func(input_base * (1 + variacao_pct))
        minus_result = modelo_func(input_base * (1 - variacao_pct))
        
        sensibilidade_plus = (plus_result - base_result) / base_result
        sensibilidade_minus = (minus_result - base_result) / base_result
        
        return {
            'elasticidade_positiva': sensibilidade_plus,
            'elasticidade_negativa': sensibilidade_minus
        }
