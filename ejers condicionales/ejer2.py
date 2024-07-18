# Un programa de descarga de archivos multimedia tiene diferentes velocidades de descarga según la calidad de la conexión a internet del usuario. Si la conexión es mayor a 20 Mbps, la velocidad de descarga será de 10 Mbps, si la conexión es menor a 20 Mbps pero mayor a 5 Mbps, la velocidad será de 5 Mbps y si la conexión es menor a 5 Mbps, la velocidad de descarga será de 1 Mbps.Escribir un programa que calcule el tiempo de descarga de un archivo y el ancho de banda utilizado, según la velocidad de descarga.

def calcular_tiempo_descarga(tamano_archivo, velocidad_descarga):
    tiempo_descarga = tamano_archivo / velocidad_descarga
    return tiempo_descarga

def calcular_ancho_banda_utilizado(tamano_archivo, tiempo_descarga):
    ancho_banda_utilizado = tamano_archivo / tiempo_descarga
    return ancho_banda_utilizado


tamano_archivo = float(input("Ingrese el tamaño del archivo en MB: "))
velocidad_conexion = float(input("Ingrese la velocidad de conexión en Mbps: "))

if velocidad_conexion > 20:
    velocidad_descarga = 10
elif velocidad_conexion > 5:
    velocidad_descarga = 5
else:
    velocidad_descarga = 1

tiempo_descarga = calcular_tiempo_descarga(tamano_archivo, velocidad_descarga)
ancho_banda_utilizado = calcular_ancho_banda_utilizado(tamano_archivo, tiempo_descarga)

print("Tiempo de descarga:", tiempo_descarga, "segundos")
print("Ancho de banda utilizado:", ancho_banda_utilizado, "Mbps")