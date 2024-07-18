import random

def piedra_papel_tijeras():
    def obtener_opcion_usuario():
        while True:
            opcion = input("Ingresa tu elección (piedra, papel, tijeras) o 'q' para salir: ").lower()
            if opcion in ['piedra', 'papel', 'tijeras', 'q']:
                return opcion
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

    def obtener_opcion_computadora():
        return random.choice(['piedra', 'papel', 'tijeras'])

    def determinar_ganador(opcion_usuario, opcion_computadora):
        if opcion_usuario == opcion_computadora:
            return "¡Es un empate!"
        elif (opcion_usuario == 'piedra' and opcion_computadora == 'tijeras') or \
            (opcion_usuario == 'tijeras' and opcion_computadora == 'papel') or \
            (opcion_usuario == 'papel' and opcion_computadora == 'piedra'):
            return "¡Ganaste!"
        else:
            return "¡La computadora gana!"

    def jugar_juego():
        victorias_usuario = 0
        victorias_computadora = 0
        intentos = 3

        while intentos > 0:
            opcion_usuario = obtener_opcion_usuario()
            if opcion_usuario == 'q':
                break

            opcion_computadora = obtener_opcion_computadora()

            print("Tu elección:", opcion_usuario)
            print("Elección de la computadora:", opcion_computadora)

            resultado = determinar_ganador(opcion_usuario, opcion_computadora)
            print(resultado)

            if resultado == "¡Ganaste!":
                victorias_usuario += 1
            elif resultado == "¡La computadora gana!":
                victorias_computadora += 1

            intentos -= 1

        print("¡Fin del juego!")
        print("Ganaste", victorias_usuario, "veces.")
        print("La computadora ganó", victorias_computadora, "veces.")

    jugar_juego()


def ahorcado():
    def agregar_palabra(lista_palabras):
        palabra = input("Ingresa una palabra: ")
        lista_palabras.append(palabra)

    def configurar():
        while True:
            try:
                num_equivocaciones = int(input("Ingresa el número de equivocaciones permitidas: "))
                if num_equivocaciones > 0:
                    return num_equivocaciones
                else:
                    print("El número de equivocaciones debe ser mayor que 0. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

    def jugar(lista_palabras, num_equivocaciones):
        palabra_secreta = random.choice(lista_palabras)
        espacios = ['_'] * len(palabra_secreta)
        intentos = num_equivocaciones

        while intentos > 0:
            print("Palabra:", ' '.join(espacios))
            letra = input("Ingresa una letra: ").lower()

            if letra in palabra_secreta:
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra:
                        espacios[i] = letra
            else:
                intentos -= 1
                print("Letra incorrecta. Te quedan", intentos, "oportunidades.")

            if '_' not in espacios:
                print("¡Ganaste!")
                print("La palabra era:", palabra_secreta)
                return

        print("¡Perdiste!")
        print("La palabra era:", palabra_secreta)

    def menu():
        lista_palabras = []
        num_equivocaciones = 0

        while True:
            print("--- Menú ---")
            print("1. Agregar Palabra")
            print("2. Configurar")
            print("3. Jugar")
            print("4. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                agregar_palabra(lista_palabras)
            elif opcion == '2':
                num_equivocaciones = configurar()
            elif opcion == '3':
                if not lista_palabras:
                    print("No hay palabras en la lista. Agrega palabras antes de jugar.")
                elif num_equivocaciones == 0:
                    print("No has configurado el número de equivocaciones. Configura antes de jugar.")
                else:
                    jugar(lista_palabras, num_equivocaciones)
            elif opcion == '4':
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

    menu()


while True:
    print("Escoge el juego que quieres jugar:")
    print("1. Piedra, papel o tijeras")
    print("2. Ahorcado")
    print("3. Salir")

    opcion = input("Ingresa el número de tu elección: ")

    if opcion == '1':
        print("Jugando a piedra, papel o tijeras...")
        piedra_papel_tijeras()
    elif opcion == '2':
        print("Jugando al ahorcado...")
        ahorcado()
    elif opcion == '3':
        print("Saliendo del programa...")
        break