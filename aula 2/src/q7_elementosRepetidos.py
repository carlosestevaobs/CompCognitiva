def remove_elementos_repetidos (lista):
    lista_nova = []
    for i in lista:
        if i not in lista_nova:
            lista_nova.append(i)
    return lista_nova