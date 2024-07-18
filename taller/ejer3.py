# El Zoológico la Pastora desea tener un informe estadístico de sus rinocerontes con respecto a su longevidad, tal que da como datos el nombre de un rinoceronte, su edad, su peso, y su longitud, expresados estos dos últimos en libras y pies respectivamente. Desarrollar un algoritmo y diagrama de flujo que imprima el nombre del rinoceronte, su edad, su peso expresado en kilogramos y su longitud expresada en metros.

def convertir_a_kilogramos(peso):
    return peso * 0.453592

def convertir_a_metros(longitud):
    return longitud * 0.3048

def imprimir_info():
    nombre = input("Nombre del rinoceronte: ")
    edad = input("Edad del rinoceronte: ")
    peso = float(input("Peso del rinoceronte (libras): "))
    longitud = float(input("Longitud del rinoceronte (pies): "))
    peso_kg = convertir_a_kilogramos(peso)
    longitud_m = convertir_a_metros(longitud)
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Peso (kg):", peso_kg)
    print("Longitud (m):", longitud_m)

imprimir_info()
