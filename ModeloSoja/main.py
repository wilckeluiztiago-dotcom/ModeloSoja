import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

from modulos.crescimento.dados_conab import DadosConabReal
from modulos.crescimento.modelo_ensemble import ModeloEnsemble
from modulos.estatistica.copulas import CopulaGaussianaRisco
from modulos.risco.simulacao_monte_carlo_clima import SimulacaoMonteCarloClima
from modulos.risco.valor_em_risco import CalculadoraVaR
from modulos.visualizacao.grafico_projecao import GraficoProjecaoCrescimento
from modulos.visualizacao.grafico_mapa_risco import GraficoMapaRisco
from modulos.visualizacao.grafico_3d_risco import GraficoSuperficieRisco
from modulos.visualizacao.grafico_distribuicao_conjunta import GraficoDistribuicaoConjunta

def main():
    print("=== Iniciando Modelo Avançado V2 (Ensemble + Copulas + 3D) ===")
    print("Autor: Luiz Tiago Wilcke - Unisociesc")
    
    if not os.path.exists('graficos_v2'):
        os.makedirs('graficos_v2')

    # 1. Dados Reais segregados
    carregador = DadosConabReal()
    print("Dados históricos reais carregados (Área x Produtividade).")
    
    estados = ['MT', 'PR', 'RS', 'GO', 'MS', 'BA', 'MG', 'TO']
    anos_treino = carregador.ANOS
    anos_futuros = np.arange(2025, 2051)
    
    residuos_df_dict = {} # Para Copula
    projesoes_finais = pd.DataFrame(index=anos_futuros)
    riscos_matrix = [] # Para 3D
    
    viz_projecao = GraficoProjecaoCrescimento()
    
    total_area_proj = pd.Series(0, index=anos_futuros)
    
    for uf in estados:
        print(f"Processando Ensemble Para: {uf}...")
        df_estado = carregador.obter_dados_completos(uf)
        
        # Modelar Área
        ens_area = ModeloEnsemble(df_estado['Area_Mil_Ha'])
        ens_area.treinar()
        pred_area = ens_area.projetar(anos_futuros, len(anos_treino))
        
        # Modelar Produtividade
        ens_yield = ModeloEnsemble(df_estado['Produtividade_Kg_Ha'])
        ens_yield.treinar()
        pred_yield = ens_yield.projetar(anos_futuros, len(anos_treino))
        
        # Produção = Área * Yield
        pred_producao = (pred_area * pred_yield) / 1000 # Mil Ton
        projesoes_finais[uf] = pred_producao
        
        # Guardar resíduos (histórico real vs predito pelo ensemble no treino)
        # Simplificação: usando resíduo da produtividade como proxy de risco climático
        residuo = df_estado['Produtividade_Kg_Ha'] - ens_yield.modelos['linear'].predict(np.arange(len(df_estado)).reshape(-1,1))
        residuos_df_dict[uf] = residuo
        
        # Gerar Gráfico
        viz_projecao.gerar(
            df_estado['Producao_Mil_Ton'], 
            pred_producao, 
            uf, 
            f'graficos_v2/adv_projecao_{uf}.png'
        )
        
        # Risco simulado para matriz 3D (aumenta com o tempo)
        risco_base = np.linspace(0.1, 0.4 + (0.1 if uf in ['RS', 'BA'] else 0), len(anos_futuros))
        riscos_matrix.append(risco_base)

    # 2. Modelagem de Risco Sistêmico (Cópulas)
    print("Calculando Risco Sistêmico com Cópulas Gaussianas...")
    df_residuos = pd.DataFrame(residuos_df_dict)
    copula = CopulaGaussianaRisco(df_residuos)
    copula.ajustar()
    
    cenarios_copula = copula.simular_cenarios_conjuntos(len(anos_futuros), n_simulacoes=5000)
    
    # 3. Visualizações Avançadas
    print("Gerando visualizações avançadas...")
    
    # 3D
    viz_3d = GraficoSuperficieRisco()
    viz_3d.gerar(riscos_matrix, anos_futuros, estados, 'graficos_v2/superficie_risco_3d.png')
    
    # Joint Plot (RS vs MT - extremos opostos)
    # Pegamos a simulação do ano 2035 por exemplo
    idx_ano = 10 
    risco_sim_mt = cenarios_copula['MT'][:, idx_ano]
    risco_sim_rs = cenarios_copula['RS'][:, idx_ano]
    
    viz_joint = GraficoDistribuicaoConjunta()
    viz_joint.gerar(risco_sim_mt, risco_sim_rs, 'MT (Centro-Oeste)', 'RS (Sul)', 'graficos_v2/correlacao_risco_MT_RS.png')
    
    # VaR Nacional
    calc_var = CalculadoraVaR()
    # Somar perdas de todos estados em um ano especifico
    perdas_nacionais = np.zeros(5000)
    for uf in estados:
        perdas_nacionais += cenarios_copula[uf][:, 10] # Ano 2035
        
    var_95 = calc_var.calcular_var_historico(perdas_nacionais, 0.95)
    print(f"VaR (Value at Risk) do desvio de produtividade Nacional em 2035 (95%): {var_95:.2f}")
    
    print("=== Execução V2 Concluída ===")

if __name__ == "__main__":
    main()
