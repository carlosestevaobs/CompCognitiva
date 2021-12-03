import sys
sys.path.insert(0, '../../')
from src.utils import multiplas_roi
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
list_coordenadas: lista de coordenadas central da roi
tamanho_matriz: tamanho das rois
'''
def main():
    list_coordenadas = [[3,3],[5,5],[2,3]]
    tamanho_matriz = 3,3
    resultado = multiplas_roi(matriz_teste, list_coordenadas, tamanho_matriz)
    print(resultado)

if __name__ == '__main__':
    main()