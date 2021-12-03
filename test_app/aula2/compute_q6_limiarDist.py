import sys
sys.path.insert(0, '../../')
from src.utils import limiar
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-plv', '--palavra',
                    default = 'uva',
                    help = 'palavra a ser procurada')
    
    ap.add_argument('-lst', '--lista',
                    default = ['abacate', 'pera', 'uva', 'banana', 
                               'maçã' , 'repolho', 'uva', 'feijão', 
                               'arroz'],
                    help = 'Lista de Strings') 
    
    ap.add_argument('-lim', '--valorLimiar',
                    default = 2,
                    help = 'limiar')
    
    args = vars(ap.parse_args())
    palavra = args['palavra']
    lista = args['lista']       
    valorLimiar = args['valorLimiar']
    
    lista2 = limiar(palavra, lista, valorLimiar) 
    print(lista2)     
  
if __name__ == '__main__': 
    main()