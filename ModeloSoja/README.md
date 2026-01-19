# Modelo Estatístico Avançado de Soja e Risco de Seca (V2.0)

**Autor:** Luiz Tiago Wilcke  
**Afiliação:** Estudante de Estatística - Unisociesc

## Resumo Executivo
Este projeto implementa uma arquitetura de modelagem preditiva de **Ensemble** (Empilhamento de Modelos) combinada com **Cópulas Gaussianas** para análise de risco sistêmico. O objetivo é projetar a produção de soja brasileira (2025-2050) e quantificar a probabilidade de falhas simultâneas de safra entre diferentes estados.

## Metodologia Estatística Avançada

### 1. Modelos de Crescimento: Abordagem Ensemble

Para cada estado, a produção projetada $Y_t$ segue a decomposição:

$$
Y_t = A_t \times P_t
$$

Onde $A_t$ (Área) e $P_t$ (Produtividade) são modelados independentemente por um Ensemble ponderado pelo erro quadrático inverso (Inv-MSE):

$$
\hat{y}_{ensemble} = w_1 \cdot \hat{y}_{ARIMA} + w_2 \cdot \hat{y}_{HoltWinters} + w_3 \cdot \hat{y}_{Linear}
$$

Com pesos definidos dinamicamente:
$$ w_i = \frac{MSE_i^{-1}}{\sum MSE_j^{-1}} $$

### 2. Risco Sistêmico Multivariado (Cópulas)

A dependência espacial entre as sobras/falhas de produtividade dos estados é modelada através de uma **Cópula Gaussiana**. Isso permite capturar correlações não-lineares de cauda (ex: Se RS tem seca severa, qual a probabilidade condicional do PR também ter?).

A função densidade da cópula $C$ é dada por:

$$
c(u_1, ..., u_d) = \frac{1}{\sqrt{|\Sigma|}} \exp \left( -\frac{1}{2} \zeta^T (\Sigma^{-1} - I) \zeta \right)
$$

Onde $\zeta = (\Phi^{-1}(u_1), ..., \Phi^{-1}(u_d))$ são os quantis normais das distribuições marginais dos resíduos de produtividade.

### 3. Value at Risk (VaR) Climático

Calculamos o VaR (95%) para a perda agregada nacional simulada via Monte Carlo (5000 cenários) usando a estrutura de dependência da Cópula.

## Resultados Gerados (Pasta `graficos_v2/`)

1. **Superfície 3D de Risco (`superficie_risco_3d.png`)**: Evolução espaço-temporal da probabilidade de seca severa.
2. **Distribuição Conjunta de Densidade (`correlacao_risco_MT_RS.png`)**: KDE Bivariado mostrando a interação de risco entre Pólo Sul (RS) e Centro-Oeste (MT).
3. **Projeções Ensemble**: Gráficos individuais por estado com faixas de confiança refinadas.

## Execução

```bash
python main.py
```
O sistema processará os dados históricos reais da CONAB segredados por área e produtividade, ajustará os ensembles e executará a simulação de cópula.
