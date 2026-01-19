import numpy as np

class MatrizTransicaoSeca:
    """
    Calcula matriz de transição de Markov para estados de seca.
    Estado 0: Normal/Úmido
    Estado 1: Seca
    Autor: Luiz Tiago Wilcke
    """
    
    def calcular_matriz(self, serie_spi):
        estado_seca = (serie_spi < -1.0).astype(int) # 1 se seca, 0 se não
        
        transicoes = np.zeros((2, 2))
        
        for t in range(len(estado_seca) - 1):
            atual = estado_seca[t]
            proximo = estado_seca[t+1]
            transicoes[atual, proximo] += 1
            
        probabilidades = transicoes / transicoes.sum(axis=1, keepdims=True)
        return probabilidades
        
    def simular_futuro(self, estado_inicial, n_passos, matriz):
        """Simula cadeia de Markov."""
        estados = [estado_inicial]
        atual = estado_inicial
        
        for _ in range(n_passos):
            novo = np.random.choice([0, 1], p=matriz[atual])
            estados.append(novo)
            atual = novo
            
        return estados
