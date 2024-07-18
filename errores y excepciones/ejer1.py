lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("Ingrese la posición del elemento que desea obtener: "))
        print(f"El valor en la posición {pos} es {lista[pos]}")
        break
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except IndexError:
        print("Error: La posición ingresada está fuera de rango.")