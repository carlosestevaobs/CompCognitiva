import sys
sys.path.insert(0, '../../')
from src.utils import calcDistEucl
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-p1', '--pont1',
                    default = [1, 0, 3, 30],
                    help = 'primeiro ponto')
    
    ap.add_argument('-p2', '--pont2',
                    default = [10, 12, 9, 47],
                    help = 'segundo ponto')
    
    
    args = vars(ap.parse_args())
    pont1 = args['pont1']
    pont2 = args['pont2']    
  
    distancia = calcDistEucl(pont1, pont2)
    print("A distância entre os dois pontos é " + str(distancia))

if __name__ == '__main__': 
    main()