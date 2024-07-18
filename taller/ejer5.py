# La compañía de seguros de vida atlas se va a cambiar de domicilio y por lo tanto pone en venta su terreno, pero no tiene una idea del valor del terreno, entonces solicita al departamento de sistemas que le desarrolle un algoritmo y diagrama de flujo con la finalidad de que calcule e imprima el precio del terreno del cual se tiene los siguientes datos: largo, ancho y precio por metro cuadrado, si el terreno tiene más de 400 metros cuadrados se hace un descuento del 10%. 

largo = float(input("Ingrese el largo del terreno en metros: "))
ancho = float(input("Ingrese el ancho del terreno en metros: "))
precio_metro_cuadrado = float(input("Ingrese el precio por metro cuadrado: "))

area = largo * ancho
precio_terreno = area * precio_metro_cuadrado

if area > 400:
    descuento = precio_terreno * 0.1
    precio_terreno -= descuento

print("El precio del terreno es:", precio_terreno)