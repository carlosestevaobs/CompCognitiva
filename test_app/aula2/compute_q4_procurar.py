from utils import procurar
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-plv', '--palavra',
                    default = 'maçã',
                    help = 'palavra a ser procurada')
    
    ap.add_argument('-lst', '--lista',
                    default = ['maçã', 'laranja', 'maçã','abacate', 'pêra', 'limão',
                               'maça', 'uva', 'maçã'],
                    help = 'Lista de Strings')   
    
    args = vars(ap.parse_args())
    palavra = args['palavra']
    lista = args['lista']         
    
    quantidade = procurar(palavra, lista)
    print(quantidade)
  
if __name__ == '__main__': 
    main()