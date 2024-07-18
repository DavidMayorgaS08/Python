# Leer una frase y almacenar en una tupla la frase leída pero sin espacios.  Mostrar el contenido de la tupla.

frase = input("Ingrese una frase: ")

frase_sin_espacios = frase.replace(" ", "")

tupla = tuple(frase_sin_espacios)

print("Contenido de la tupla:", tupla)