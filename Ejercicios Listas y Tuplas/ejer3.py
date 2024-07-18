# Cree una aplicación que presente un menú con las siguientes opciones: 
# Aplicaciones con Listas

# 1. Ingresar lista nueva
# 2. Ordenar lista
# 3. Promedio lista
# 4. Buscar elemento
# 5. Salir


# *Ingresar lista* solicita los elementos de una lista, terminando con el ingreso de un número negativo el cual no formará parte de la lista

# *Ordenar lista* Presenta los valores de la lista ordenados.

# *Promedio lista* Muestra el promedio de los valores de la lista

# *Buscar elemento* solicita un número a buscar en la lista e indica si se encuentra en ella y cuántas veces aparece.

def ingresar_lista():
    lista = []
    while True:
        elemento = int(input("Ingrese un número (ingrese un número negativo para terminar): "))
        if elemento < 0:
            break
        lista.append(elemento)
    return lista

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

def promedio_lista(lista):
    promedio = sum(lista) / len(lista)
    print("Promedio de la lista:", promedio)

def buscar_elemento(lista):
    elemento = int(input("Ingrese el número a buscar: "))
    cantidad = lista.count(elemento)
    if cantidad > 0:
        print("El número", elemento, "se encuentra en la lista y aparece", cantidad, "veces.")
    else:
        print("El número", elemento, "no se encuentra en la lista.")

while True:
    print("\nAplicaciones con Listas")
    print("1. Ingresar lista nueva")
    print("2. Ordenar lista")
    print("3. Promedio lista")
    print("4. Buscar elemento")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        lista = ingresar_lista()
    elif opcion == 2:
        ordenar_lista(lista)
    elif opcion == 3:
        promedio_lista(lista)
    elif opcion == 4:
        buscar_elemento(lista)
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")