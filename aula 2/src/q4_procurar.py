import numpy as np

def procurar(palavra, lista):
    lista = np.array(lista)
    contador = 0
    for i in range(lista.shape[0]):       
        if (palavra == lista[i]):
            contador+=1            
    return contador
    
            
    
    