import sys
sys.path.append('../src/')

from q1_distanciaEucl import calcDistEucl;
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
  
    calcDistEucl(pont1, pont2)
  
if __name__ == '__main__': 
    main()