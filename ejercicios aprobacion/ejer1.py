def caracteres_unicos(oracion):
    caracteres_unicos = set(oracion)
    return caracteres_unicos

# Lee una oración del usuario
oracion = input("Ingresa una oración: ")

# Obtiene el conjunto de caracteres únicos
resultado = caracteres_unicos(oracion)

# Imprime el resultado
print("Caracteres únicos:", resultado)