# Realiza una función que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
def separar_pares_impares(numeros):
    numeros_pares = []
    numeros_impares = []
    for num in numeros:
        if num % 2 == 0:
            numeros_pares.append(num)
        else:
            numeros_impares.append(num)
    numeros_pares.sort()
    numeros_impares.sort()
    return numeros_pares, numeros_impares

x = input("Cantidad de numeros a ingresar: ")
numeros = []
for i in range(int(x)):
    numeros.append(int(input("Ingrese un numero: ")))

pares, impares = separar_pares_impares(numeros)
print("Pares:", pares)
print("Impares:", impares)
