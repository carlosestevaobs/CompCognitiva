# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../')
from src.utils import regiao_matriz
import numpy as np
#matriz_exemplo
matriz_teste = np.array([[1, 2, 3, 4,17,26,60],
                  [5, 6, 7, 8,18,27,63],
                  [9, 10, 11, 12,19,60,96],
                  [13, 14, 15, 16,20,69,30],
                  [21, 22, 23, 24,25,60,95],
                  [21, 22, 23, 24,25,50,88],
                  [21, 22, 23, 24,25,50,81]])
'''
Entradas da função:
matriz = matriz compelta 
coordenada_central: coordenada central da roi
tamanho_matriz: tamanho da roi
'''
def main():
    coordenada_central= 5,5
    tamanho_matriz = 3,3
    resultado = regiao_matriz(matriz_teste, coordenada_central, tamanho_matriz)
    print(resultado)
if __name__ == '__main__':
    main()
