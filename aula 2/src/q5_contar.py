from collections import Counter
import numpy as np

def contar(lista):     
    valores = np.array(list(Counter(lista).values()))
    indices = np.array(list(Counter(lista).keys()))

    return np.column_stack((indices, valores))   
    
   
    