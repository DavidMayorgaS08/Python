# Realice un juego que simule el lanzamiento de un dado (muestre un valor aleatorio entre 1 y 6) el programa debe llevar la cuenta del total de lanzamientos.  Si el jugador lanza 10 veces sin sacar 1 gana el juego, en caso de sacar el 1 antes de los 10 lanzamientos pierde.
# Nota: si ya lanzó 10 veces sin sacar el 1 y ganó, no se le debe dejar volver a lanzar

import random

lanzamientos = 0
ganador = False

while lanzamientos < 10:
    lanzamiento = random.randint(1, 6)
    lanzamientos += 1
    print(f"Lanzamiento {lanzamientos}: {lanzamiento}")
    
    if lanzamiento == 1:
        print("Has perdido.")
        break
    
    if lanzamientos == 10:
        print("¡Has ganado!")
        ganador = True

if ganador:
    print("¡Felicidades! Has ganado el juego.")
else:
    print("Lo siento, has perdido el juego.")