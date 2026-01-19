import pandas as pd
import numpy as np

class GeradorDadosSoja:
    """
    Gera dados históricos sintéticos realistas de produção de soja por estado.
    Baseado em tendências históricas reais aproximadas do Brasil.
    Autor: Luiz Tiago Wilcke
    """
    
    ESTADOS_PARAMS = {
        'MT': {'base': 30_000, 'crescimento': 1500, 'volatilidade': 2000}, # Mato Grosso
        'PR': {'base': 18_000, 'crescimento': 500,  'volatilidade': 3000}, # Paraná (mais instável clima)
        'RS': {'base': 16_000, 'crescimento': 400,  'volatilidade': 6000}, # Rio Grande do Sul (muita seca)
        'GO': {'base': 12_000, 'crescimento': 800,  'volatilidade': 1000}, # Goiás
        'MS': {'base': 10_000, 'crescimento': 700,  'volatilidade': 1200}, # Mato Grosso do Sul
        'BA': {'base': 6_000,  'crescimento': 400,  'volatilidade': 1500}, # Bahia (Matopiba)
        'MG': {'base': 5_000,  'crescimento': 300,  'volatilidade': 800},  # Minas Gerais
        'TO': {'base': 4_000,  'crescimento': 350,  'volatilidade': 900},  # Tocantins
        'MA': {'base': 3_000,  'crescimento': 250,  'volatilidade': 800},  # Maranhão
        'PI': {'base': 2_500,  'crescimento': 200,  'volatilidade': 700},  # Piauí
        'SC': {'base': 2_200,  'crescimento': 50,   'volatilidade': 400},  # Santa Catarina
        'SP': {'base': 3_500,  'crescimento': 100,  'volatilidade': 500},  # São Paulo
    }
    
    def __init__(self, ano_inicio=2000, ano_fim=2026):
        self.anos = np.arange(ano_inicio, ano_fim + 1)
        
    def gerar_serie_estado(self, sigla_estado):
        """Gera uma série temporal para um estado específico."""
        if sigla_estado not in self.ESTADOS_PARAMS:
            raise ValueError(f"Estado {sigla_estado} desconhecido.")
            
        params = self.ESTADOS_PARAMS[sigla_estado]
        n_anos = len(self.anos)
        
        # Tendência determinística
        tendencia = params['base'] + params['crescimento'] * np.arange(n_anos)
        
        # Ruído aleatório (clima, pragas)
        ruido = np.random.normal(0, params['volatilidade'], n_anos)
        
        # Eventos extremos (Secas severas aleatórias) - Ex: El Nino
        # Probabilidade de 15% de ocorrer uma queda brusca
        eventos_extremos = np.random.choice([1, 0.7, 0.6], size=n_anos, p=[0.85, 0.10, 0.05])
        
        producao = (tendencia + ruido) * eventos_extremos
        
        # Garantir não negativo
        producao = np.maximum(producao, 0)
        
        return pd.DataFrame({
            'Ano': self.anos,
            'Producao_Mil_Toneladas': producao,
            'Estado': sigla_estado
        }).set_index('Ano')

    def gerar_todos_estados(self):
        df_list = []
        for uf in self.ESTADOS_PARAMS.keys():
            df_list.append(self.gerar_serie_estado(uf))
        return pd.concat(df_list)
