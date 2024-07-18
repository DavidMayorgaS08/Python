# Recibir una frase por parte del usuario y devolver el número de palabras que se encuentran en la frase

frase = input("Ingresa una frase: ")
palabras = frase.split()
num_palabras = len(palabras)
print("El número de palabras en la frase es:", num_palabras)