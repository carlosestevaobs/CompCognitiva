
import numpy as np

def limiar(palavra, lista, limiar):
    lista = np.array(lista)
    lista2 = []
    posInicial = -1
    for i in range(lista.shape[0]): 
        if (palavra == lista[i]):
            posInicial = i
            break        
    if (posInicial == -1):       
        return lista2
    else:    
        if ((posInicial + limiar <= lista.shape[0]) and 
            (posInicial - limiar >= 0)):   
            for i in range(posInicial - limiar, posInicial):                 
                 lista2.append(lista[i])
             
            for i in range(posInicial + 1, (posInicial + 1 + limiar)):             
                lista2.append(lista[i])
                
           
           
   
        
    return lista2
    