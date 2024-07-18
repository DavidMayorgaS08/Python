# En la tienda de mayoreo San Juanita el impuesto que se debe pagar por los artículos adquiridos se calcula de la siguiente manera: los primeros $30 no causan impuesto, los siguientes $30 tienen un 30% de impuesto y el resto el 40% de impuesto, pero si el costo del producto es mayor a $400, entonces se cobra el 50%. Desarrollar un algoritmo y diagrama de flujo que lea el costo básico de un artículo y calcule el costo total. Muestre el artículo y su costo total

costo_basico = float(input("Ingrese el costo básico del artículo: "))

if costo_basico <= 30:
    impuesto = 0
elif costo_basico <= 60:
    impuesto = costo_basico * 0.3
elif costo_basico <= 400:
    impuesto = costo_basico * 0.4
else:
    impuesto = costo_basico * 0.5

costo_total = costo_basico + impuesto

print("El artículo tiene un costo total de:", costo_total)