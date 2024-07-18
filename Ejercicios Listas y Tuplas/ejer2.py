# Solicite al usuario dos frases y devuelva una lista con todas las letras que se repiten en la misma posición de ambas frases f1: hola mundo f2: como estas  r=["o"]

f1 = input("Ingrese la primera frase: ")
f2 = input("Ingrese la segunda frase: ")

repeated_letters = []

if len(f1) == len(f2):
    for i in range(len(f1)):
        if f1[i] == f2[i]:
            repeated_letters.append(f1[i])

print("Letras repetidas en la misma posición:", repeated_letters)