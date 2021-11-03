from q7_elementos_repetidos import remove_elementos_repetidos

lista = [1,1,2,2,"maria","maria","pedro", "pedro", 1.2, 1.2]

def main():
    nova_lista  = remove_elementos_repetidos(lista)
    print("Nova lista sem elementos repetidos: ")
    print(nova_lista)

if __name__ == '__main__':
    main()