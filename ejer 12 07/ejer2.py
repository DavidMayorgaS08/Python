# Realiza una función que reciba una palabra y devuelva un diccionario donde las claves sean las diferentes letras que se encuentran en la palabra y los valores sean el número de veces que se repite cada letra en la palabra servicio "s": 1, "e":1,"r":1, "i":2

def contar_letras(palabra):
    diccionario = {}
    for letra in palabra:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

palabra = input("Ingrese una palabra: ")
resultado = contar_letras(palabra)
print(resultado)