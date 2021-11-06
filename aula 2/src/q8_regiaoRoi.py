def região_matriz(matriz, coordenada_central, tamanho_matriz):
    y, x = coordenada_central
    l,c = tamanho_matriz
    array_roi = matriz[y-int(l/2):y+int(l/2)+1,x-int(c/2):x+int(c/2)+1]
    return array_roi
