# Leer una serie de números por parte del usuario hasta que el número ingresado sea negativo y determinar:


# *   Sumatoria de los números leídos
# *   Cantidad de números pares e impares
# *   El número menor y mayor leído


sumatoria = 0
cantidad_pares = 0
cantidad_impares = 0
numero_menor = float('inf')
numero_mayor = float('-inf')

x = int(input("Cantidad de numeros que va a ingresar:"))

y = 0

while y < x:
    numero = float(input("Ingrese un número: "))
    
    if numero < 0:
        break

    sumatoria += numero

    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    if numero < numero_menor:
        numero_menor = numero
    if numero > numero_mayor:
        numero_mayor = numero
    
    y += 1

print("Sumatoria:", sumatoria)
print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)
print("Número menor:", numero_menor)
print("Número mayor:", numero_mayor)