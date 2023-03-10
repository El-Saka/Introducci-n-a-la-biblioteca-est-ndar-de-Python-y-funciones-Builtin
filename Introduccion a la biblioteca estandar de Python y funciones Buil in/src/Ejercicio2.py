from functools import reduce

def suma_impares(lista):
    impares = filter(lambda x: x % 2 != 0, lista)
    suma = reduce(lambda x, y: x + y, impares)
    return suma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = suma_impares(lista)
print(resultado) # salida: 25