import sys
sys.path.insert(0, '../../')

from src.nlp_proc import createCSV

listaExemplo = [[[0, 1, 2], 'maçã', ['x', 'y', 'z'], 'k', 'h', ['a', 'b', 'c']],
         [[0], 'banana', ['k'], 'k', 'h', ['d']],
         [[1, 2], 'uva', ['k'], 'k', 'h', ['c']]
         ]

createCSV(listaExemplo)