# En un sistema de automatización industrial, un motor puede estar encendido o apagado. Si la temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente. Escribir un programa que controle el estado del motor y lo apague si la temperatura supera los 80 grados.

temperatura = float(input("Ingrese la temperatura actual: "))

if temperatura > 80:
    print("La temperatura ha superado los 80 grados. Apagando el motor...")
else:
    print("La temperatura es segura. El motor sigue encendido.")