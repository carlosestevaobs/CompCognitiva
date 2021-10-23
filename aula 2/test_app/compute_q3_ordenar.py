import sys
sys.path.append('../src/')

from q3_ordenar import ordenar;
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-lst', '--lista1',
                    default = ['maça', 'laranja', 'abacate', 'pêra', 'limão'],
                    help = 'Lista de Strings')
    
    ap.add_argument('-cond', '--condicao1',
                    default = True,
                    help = 'Valor booleando para ordenação')    
    
    args = vars(ap.parse_args())
    lista = args['lista1']   
    condicao = args['condicao1']  
    
    listaOrd = ordenar(lista, condicao)   
  
if __name__ == '__main__': 
    main()