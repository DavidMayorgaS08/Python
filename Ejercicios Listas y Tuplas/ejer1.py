# Pregunte al usuario cuántos elementos desea ingresar en una lista, luego solicite cada uno de ellos y presente el contenido de la lista y su contenido invertido.

num_elementos = int(input("¿Cuántos elementos deseas ingresar? "))

mi_lista = []

for i in range(num_elementos):
    elemento = input("Ingresa el elemento {}: ".format(i+1))
    mi_lista.append(elemento)

print("Lista original:", mi_lista)

lista_invertida = mi_lista[::-1]
print("Lista invertida:", lista_invertida)