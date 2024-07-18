# El maestro de la clase de matemáticas de la secundaria federal número 29, quiere Desarrollar un algoritmo que le permita calcular las raíces de la ecuación: Y = 3X2 + 7X – 15, con el motivo de tener una respuesta más precisa y rápida.

import math

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        return "No existen raíces reales"

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

raices = calcular_raices(a, b, c)
print(raices)
