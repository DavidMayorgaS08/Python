# Un cliente ordena cierta cantidad de brochas de cerda, rodillos y sellador; las brochas de cerda tienen un 20% de descuento y los rodillos un 15% de descuento. Los datos que se tienen por cada tipo de artículo son: la cantidad pedida y el precio unitario. Además, si se paga de contado todo tiene un descuento del 7%. Desarrollar un algoritmo y diagrama de flujo que calcule y muestre el costo total de la orden, tanto para el pago de contado como para el caso de pago de crédito

cantidad_brochas = int(input("Ingresa la cantidad de brochas de cerda: "))
precio_brochas = float(input("Ingresa el precio unitario de las brochas de cerda: "))

cantidad_rodillos = int(input("Ingresa la cantidad de rodillos: "))
precio_rodillos = float(input("Ingresa el precio unitario de los rodillos: "))

cantidad_sellador = int(input("Ingresa la cantidad de sellador: "))
precio_sellador = float(input("Ingresa el precio unitario del sellador: "))

costo_total = (cantidad_brochas * precio_brochas) + (cantidad_rodillos * precio_rodillos) + (cantidad_sellador * precio_sellador)

descuento_brochas = 0.2
descuento_rodillos = 0.15
descuento_efectivo = 0.07

costo_total_efectivo = costo_total * (1 - descuento_brochas) * (1 - descuento_rodillos) * (1 - descuento_efectivo)
costo_total_credito = costo_total * (1 - descuento_brochas) * (1 - descuento_rodillos)

print("Costo total para pago en efectivo: $", costo_total_efectivo)
print("Costo total para pago con tarjeta de crédito: $", costo_total_credito)