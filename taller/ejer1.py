# La gasolinera Muralla, le acaban de llegar 6 bombas despachadoras de gasolina normal, el problema es que al despachar cierta cantidad de gasolina lo registra en galones, pero el precio de la gasolina está fijado en litros. Desarrollar un algoritmo y diagrama de flujo que calcule e imprima lo que hay que cobrarle al cliente, se introducirá la cantidad de galones y el precio por litro.

galones = float(input("Ingresa el número de galones: "))
precio_litro = float(input("Ingresa el precio por litro: "))

litros = galones * 4

total = litros * precio_litro

print("El monto total a cobrar es:", total)


