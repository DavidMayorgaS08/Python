# Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total. Índice de cosecha = (cantidad de frutos recolectados / cantidad de frutos producidos) * 100%

frutos_recolectados = int(input("Ingrese la cantidad de frutos recolectados: "))
frutos_producidos = int(input("Ingrese la cantidad de frutos producidos: "))

indice_cosecha = (frutos_recolectados / frutos_producidos) * 100

print(f"El índice de cosecha es: {indice_cosecha}%")