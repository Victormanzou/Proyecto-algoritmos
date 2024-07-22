def lineal(lista, elemento):
    i = 0
    for n in lista:
        if n == elemento:
            return i
        i += 1
    return -1

def main():
    lista = [15, 23, 68, 95, 4, 1, 0, 10, 25, 12, 354, 8, 41]
    try:
        elemento = int(input("Introduce el número que quieres buscar: "))
    except ValueError:
        print("Por favor, introduce un número entero válido.")
        return
    
    pos = lineal(lista, elemento)
    if pos > -1:
        print(f"La posición es: {pos + 1}")
    else:
        print("El elemento no se encontró")

main()




