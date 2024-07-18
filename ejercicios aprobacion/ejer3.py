# Diccionario de traducciones de frutas
frutas = {
    "manzana": "apple",
    "banana": "banana",
    "naranja": "orange",
    "uva": "grape",
    "pera": "pear"
}

while True:
    # Solicitar el nombre de una fruta al usuario
    fruta = input("Ingrese el nombre de una fruta en español: ")

    # Verificar si la fruta está en el diccionario
    if fruta in frutas:
        # Mostrar la traducción al inglés
        print(f"La traducción de '{fruta}' es '{frutas[fruta]}'")
    else:
        # Preguntar al usuario si desea agregar la fruta al diccionario
        respuesta = input("La fruta no se encuentra en el diccionario. ¿Desea agregarla? (s/n): ")

        if respuesta.lower() == "s":
            # Solicitar la traducción de la fruta
            traduccion = input("Ingrese la traducción de la fruta al inglés: ")

            # Agregar la fruta y su traducción al diccionario
            frutas[fruta] = traduccion
            print("Fruta agregada al diccionario.")
        else:
            # Salir del programa
            break