from src.utils import limiarizar
import numpy as np
import argparse

def main():        
    ap  = argparse.ArgumentParser()
    ap.add_argument('-M', '--mat',
                    default = np.random.randint(0,255,(10,10)),
                    help = 'Matriz')    
    
    ap.add_argument('-v', '--valor',
                    default = 100,
                    help = 'Valor')    
    
    
    args = vars(ap.parse_args())
    matriz = args['mat']
    valor =  args['valor']

    x = limiarizar(matriz, valor)
    print(x)
  
if __name__ == '__main__': 
    main()