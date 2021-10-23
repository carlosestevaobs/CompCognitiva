import numpy as np
import matplotlib.pyplot as plt

def limiarizar(matriz, valor):
    matrizLim = np.zeros(shape = (matriz.shape[0], matriz.shape[1]))
    print(matrizLim.shape)
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if(matriz[i][j] >= valor):
                matrizLim[i][j] = 1

    plotar(matriz, matrizLim)
    
    
def plotar(matriz1, matriz2):
    fig = plt.figure(figsize=(10, 7))
    fig.add_subplot(1, 2, 1)
    plt.imshow(matriz1,cmap='gray')
    plt.title("Primeira")
    
    fig.add_subplot(1, 2, 2)
    plt.imshow(matriz2, cmap='gray')
    plt.title("Segunda")
      
    
    plt.show()  





