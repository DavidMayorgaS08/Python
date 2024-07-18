def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
        else:
            lista.append(el)
    except ValueError as e:
        print(e)
    finally:
        print("Gracias por usar este programa")

lista = [1, 5, 4, 6]
agregar_una_vez(lista, 5)