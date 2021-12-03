import sys
sys.path.insert(0, '../../')
from src.utils import ordenar
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-lst', '--lista1',
                    default = ['maça', 'laranja', 'abacate', 'pêra', 'limão'],
                    help = 'Lista de Strings')
    
    ap.add_argument('-cond', '--condicao1',
                    default = False,
                    help = 'Valor booleando para ordenação')    
    
    args = vars(ap.parse_args())
    lista = args['lista1']   
    condicao = args['condicao1']  
    
    listaOrd = ordenar(lista, condicao)
    print(listaOrd)
  
if __name__ == '__main__': 
    main()