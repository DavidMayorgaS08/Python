# Realiza una función recursiva que reciba un número y muestre los números pares entre 1 y el número leído.

def mostrar_pares(numero):
    if numero < 1:
        return
    if numero % 2 == 0:
        print(numero)
    mostrar_pares(numero - 1)

numero = int(input("Ingrese un número: "))
mostrar_pares(numero)