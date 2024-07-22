def partition(lista, inicio, final):
    pivote = lista[final]
    i = inicio
    for n in range(inicio, final):
        if lista[n] < pivote:
            lista[i], lista[n] = lista[n], lista[i]
            i += 1
    pivot= i
    lista[pivot], lista[final] = lista[final], lista[pivot]
    return pivot

def quick_sort(lista, inicio, final):
    if inicio < final:
        pivot = partition(lista, inicio, final)
        quick_sort(lista, inicio, pivot - 1) 
        quick_sort(lista, pivot + 1, final) 

def numeros_lista():
    entrada = input("Introduce una lista de números separados por comas: ")
    try:

        lista = [int(x) for x in entrada.split(',')]
        return lista
    except ValueError:
        print("Por favor, introduce solo números enteros válidos.")
        return None

def resultado():
    listafinal= numeros_lista()
    if listafinal is None:
        return  
    
    Inicio = 0
    final= len(listafinal) - 1
    print("Desorden: ")
    print(listafinal)
    quick_sort(listafinal, Inicio, final)
    print("Orden: ")
    print(listafinal)

resultado()
