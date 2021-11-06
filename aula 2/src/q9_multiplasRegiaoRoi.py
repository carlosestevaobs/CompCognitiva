from q8_regiaoRoi import região_matriz

def multiplas_roi(matriz, list_coordenadas, tamanho_matriz):
    lista_rois = []
    for i in list_coordenadas:
        x = região_matriz(matriz, i, tamanho_matriz)
        lista_rois.append(x)
    return lista_rois