from utils import contar
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-lst', '--lista',
                    default = ['maçã', 'laranja', 'maçã','abacate', 'pêra', 'limão',
                               'maça', 'uva', 'maçã'],
                    help = 'Lista de Strings')   
    
    args = vars(ap.parse_args())  
    lista = args['lista']         
    
    NLista = contar(lista)
    print(NLista)
  
if __name__ == '__main__': 
    main()