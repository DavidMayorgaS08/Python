# Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido

def invertir_frase(frase):
    frase_mayuscula = frase.upper()
    frase_invertida = frase_mayuscula[::-1]
    return frase_invertida

frase = input("Ingresa una frase: ")
frase_invertida = invertir_frase(frase)
print(frase_invertida)