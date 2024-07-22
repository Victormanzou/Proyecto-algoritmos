lista = [10, 6, 8, 7, 2, 45, 1, 7]
band = False

while not band:
    band = True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
          
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
            
            band = False

print(lista)
