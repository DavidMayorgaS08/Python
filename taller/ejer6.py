# El jefe del almacén de ropa almacenes del mayo pone una promoción en sus trajes por un período de tres días para sus clientes, de tal manera que si un cliente ordena un traje se captura el modelo del traje y el precio unitario. Si el cliente ordena tres o más trajes se le hace un descuento del 17%, si no se le cobra al precio normal. Desarrollar el algoritmo y diagrama de flujo

def calcular_precio_total(trajes):
    modelo = input("Ingrese el modelo del traje: ")
    precio_unitario = float(input("Ingrese el precio unitario del traje: "))

    if trajes >= 3:
        descuento = precio_unitario * 0.17
        precio_total = (precio_unitario - descuento) * trajes
    else:
        precio_total = precio_unitario * trajes

    return modelo, precio_total

cantidad_trajes = int(input("Ingrese la cantidad de trajes a ordenar: "))
modelo, precio_total = calcular_precio_total(cantidad_trajes)

print(f"Modelo del traje: {modelo}")
print(f"Precio total: {precio_total}")