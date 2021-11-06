import numpy as np
from collections import Counter

def calcDistEucl(p1, p2):
    '''
    A distância euclidiana é calculada por:
    distancia = raiz(somatorio((p1-p2)^2))
    :param p1: ponto1
    :param p2: ponto2
    :return: distância eucliana calculada
    '''

    p1 = np.array(p1)
    p2 = np.array(p2)

    distancia = np.sqrt(np.sum(np.square(p1-p2)))
    return distancia



def calcDistEuclList(ponto1, listaPontos):
    '''
    A distância euclidiana é calculada por:
    distancia = raiz(somatorio((p1-p2)^2))
    :param ponto1: ponto de referência
    :param listaPontos: lista de pontos
    :return: ponto com menor distância
    '''

    ponto1 = np.array(ponto1)
    listaPontos = np.array(listaPontos)

    distancia = []

    for i in range(listaPontos.shape[0]):
        distancia.append(np.sqrt(np.sum(np.square(ponto1 - listaPontos[i]))))

    distancia=np.array(distancia)
    ind = np.unravel_index(np.argmin(distancia, axis=None), distancia.shape)

    return listaPontos[ind]



def ordenar(lista, condicao):
    '''
    Ordena uma lista de elementos em formato
    decrescente ou crecente
    :param lista: lista de elementos
    :param condicao: True -> decrescente/False -> crescente
    :return: lista ordenada
    '''

    return sorted(lista, reverse=condicao)



def procurar(palavra, lista):
    '''
    :param palavra: palavra selecionada
    :param lista: lista de palavras
    :return: numero de repetições
    '''
    lista = np.array(lista)
    contador = 0
    for i in range(lista.shape[0]):
        if (palavra == lista[i]):
            contador+=1
    return contador



def contar(lista):
    '''
    :param lista: lista de palavras
    :return: ocorrência de todas as strings
    '''
    valores = np.array(list(Counter(lista).values()))
    indices = np.array(list(Counter(lista).keys()))

    return np.column_stack((indices, valores))



def limiar(palavra, lista, limiar):
    '''
    Calcula a lista de palavras com distância
    máxima (limiar)
    :param palavra: palavra a ser buscada
    :param lista: vetor de palavras
    :param limiar: distância
    :return: lista de palvras dentro do limiar
    '''
    lista_limiar = []
    indices_busca = lambda p, l: [i for i, e in enumerate(l) if e.lower().strip() == p]

    limiar, palavra = int(limiar), str(palavra).lower().strip()

    for indice in indices_busca(palavra, lista):
        inicio = 0 if (limiar > indice) else (indice - limiar)

        lista_esq_indice = lista[inicio:indice]
        lista_dir_indice = lista[(indice + 1):(indice + limiar + 1)]

        lista_indice = lista_esq_indice + lista_dir_indice
        lista_limiar.extend([i for i in lista_indice if i not in lista_limiar and \
                             i != palavra])

    return lista_limiar



def remove_elementos_repetidos (lista):
    '''
    :param lista: recebe uma lista de elementos
    :return: retorna lista com elementos únicos
    '''
    lista_nova = []
    for i in lista:
        if i not in lista_nova:
            lista_nova.append(i)
    return lista_nova



def regiao_matriz(matriz, coordenada_central, tamanho_matriz):
    '''
    Uma função que cria uma região
    de interesse de uma matriz 2D (ROI)
    :param matriz: recebe matriz
    :param coordenada_central: coordenada central do ROI
    :param tamanho_matriz: tamanho da ROI
    :return: retorna a ROI
    '''
    y, x = coordenada_central
    l,c = tamanho_matriz
    array_roi = matriz[y-int(l/2):y+int(l/2)+1,x-int(c/2):x+int(c/2)+1]
    return array_roi



def multiplas_roi(matriz, list_coordenadas, tamanho_matriz):
    '''
    Uma função que cria uma varias regiões
    de interesse de uma matriz 2D (ROI).
    :param matriz: matriz
    :param list_coordenadas: lista de coordenadas referente
    a quantidade de roi
    :param tamanho_matriz: tamanho da ROI
    :return: retorna lista de ROI
    '''
    lista_rois = []
    for i in list_coordenadas:
        x = regiao_matriz(matriz, i, tamanho_matriz)
        lista_rois.append(x)
    return lista_rois



def limiarizar(matriz, valor):
    '''
    Realiza a limiarização de uma matriz numérica
    :param matriz: matriz numérica
    :param valor: valor limiar
    :return: matriz limiarizada
    '''
    matrizLim = np.zeros(shape = (matriz.shape[0], matriz.shape[1]))
    print(matrizLim.shape)
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if(matriz[i][j] >= valor):
                matrizLim[i][j] = 1

    return matrizLim