# #concatenación y formateo de cadenas
# print("1) hola"+"mundo"+"python")
# print("2) hola","mundo","python")

# lenguaje,version = "Python",3 #forma de asignar valores a dos variables en una sola línea
# print("3) hola mundo %s %s" % (lenguaje,version))
# print("4) hola mundo {} {}".format(lenguaje,version))
# print(f"5) hola mundo {lenguaje} {version}")

# # #multiplicación de cadenas
# cadena = "a,"
# print(cadena*10,"e i o u")

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# cadena = "lenguaje de programación python"
# print(cadena[0:8])
# print(cadena[9:11])
# print(cadena[12:24])
# print(cadena[25:31])

# a, b = "3","5"

# print(a+b)

# print(int(a)+int(b))

# cadena_base = "mi pobre angelito"

# cad1 = cadena_base.upper()
# print(cad1)

# numero_de_o = cadena_base.count("o")
# print(numero_de_o)

# print(f"la letra 'o' esta {numero_de_o} veces en la palabra/frase '{cadena_base}'")

# cad2 = cadena_base.replace("pobre", "dulce")
# print(cad2)

# marca = input("Ingrese la marca de su vehículo: ")
# print("La marca del vehículo es: ", marca)

# precio = int(input("Ingrese el precio del vehículo: "))
# print(f"El auto marca {marca} tiene un precio de: {precio} y con el descuento del 10% le queda en: {precio*0.9}")18

# edad = int(input("Ingrese la edad:"))
# if edad >= 18:
#     print("Puede votar")
# elif edad >= 17:
#     print("en un año mas podrá votar")
# else:
#     print("no puede votar")

# edad = int(input("Ingrese la edad:"))
# if edad >= 18:
#     print("Puede votar")
# else:
#     if edad >= 17:
#         print("en un año mas podrá votar")
#     else:
#         print("no puede votar")

# estado_civil = input("Ingrese estado civil (s,c):")
# edad = int(input("ingrese edad:"))
# buena_persona = input("Es buena persona? (s,n):")
# linda = input("es linda?:")
# if estado_civil == "c":
#     print("No me caso! ni me comprometo")
# elif edad <= 30 and linda == "s" or buena_persona == "s":
#     print("Si me caso!")
# else:
#     print("solo me comprometo")


# Ciclo while

# x = 1 
# while x < 100:
#     print(x)
#     x+=1

# color = "rojo"

# while color != "blanco":
#     color = input("Ingrese color:")
#     print("El color seleccionado fue", color)


# ciclo for

# for x in [1, 2, 3 , 98, 5]:
#     print(x)

# for x in "SENA":
#     print(x)

# for x in range (1, 10):
#     print(x)

# for x in range(5):
#     print("hola")

# for x in range(2, 12, 2):
#     print(x)

# for x in range (10):
#     print(x)

# for x in range (9,0,-1):
#     print(x)

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break

#     print("Dentro del bucle.", i)

# print("fuera del bucle.")

# while True:
#     n = int(input("Ingrese un número: "))
#     if n < 0:
#         break

# print("\nLa instruccion continue:")
# for i in range(1,6):
#     if i == 3:
#         continue
#     print("Dentro del bucle", i)
# print("Fuera del bucle")

# while True:
#     num = int(input("Ingrese un numero:"))
#     if num == 3:
#         print("perdio")
#         break
#     else:
#         print("gano")

# lenguajes = ["python", "java", "php"]
# print(lenguajes)
# print(lenguajes[0])
# lenguajes[0] = "python 3"
# print(lenguajes)

# numeros = [3,4,6,2,6,8,4,9]
# res = numeros[-3] + numeros[5]
# print(res)

# mi_lista = list("1234567")
# print(type(mi_lista))
# print(mi_lista)

# mi_lista = list(range(1,11))
# print(type(mi_lista))
# print(mi_lista)
# print(mi_lista[3])

# mi_lista = [2, 3.5, True, "amigo", [3, 8, "a"]]
# print(mi_lista)

# mi_lista = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
# print(mi_lista[3][2][1])
# print(mi_lista[-1][-1][-2])

# mi_lista = list(range(1,10))
# print(mi_lista)
# print(mi_lista[1:4])
# print(mi_lista[:2])
# print(mi_lista[7:])
# print(mi_lista[-5:-1])
# print(mi_lista[-3:])

# mi_lista = [1, 2, 3, 4, 5]
# mi_lista [0:3] = ["a", "b", "c"]
# print(mi_lista)

# mi_lista = [1, 2, 3, 4, 5]
# mi_lista = mi_lista + [6]
# print(mi_lista)
# mi_lista = mi_lista + [7, 8, 9]
# print(mi_lista)

# mi_lista = [1, 2, 3]
# x, y, z = mi_lista
# print(f"valor de x {x}")
# print(f"valor de y {y}")
# print(f"valor de z {z}")

# lenguajes = ["python", "java", "php"]
# del lenguajes[1]
# print(lenguajes)

# lenguajes = ["python", "java", "php"]
# lenguajes.append("C++")
# lenguajes.append("Ruby")
# lenguajes.insert(2, "Visual Basic")
# print(lenguajes)
# lenguajes.insert(round(len(lenguajes)/2), "Delphi")
# print(lenguajes)

# lenguajes = ["python", "java", "php"]
# print("python" in lenguajes)
# print("C++" in lenguajes)

# numeros = [1, 2, "papa", 3, 4, 0]
# print(numeros)

# for x in numeros:
#     print(x, end=", ")

# numeros = [1, 2, 3, 4, 5, "papa"]
# for x in numeros:
#     if type(x) == int:
#         if x % 2 == 0:
#             print(x)

# lista =[]
# x = int(input("Ingrese la cantidad de datos a almacenar en la lista "))
# for i in range(x):
#   lista.append(int(input("ingrese valor")))

# print ("La lista es ", lista)

# mi_lista = [4, 5, 6, 7]
# for i in range(0, len(mi_lista)):
#     print(mi_lista[i])

# numeros = [3, 39, 34, 42, 54]
# for x in enumerate(numeros):
#     print(x)

# numeros = ["A", "B", "C", "D", "E"]
# for a, b in enumerate(numeros):
#     print(f"En el indice {a} econtramos el valor {b}")

# lista = [2,3,4,5,6,7,8]
# for x in lista:
#     print(x)

# lista = [2,3,4,5,6,7,8]
# i = 0
# while i < len(lista):
#     print(lista[i])
#     i += 1

# lista1 = ["ma", "me", "mi", "mo", "mu"]
# lista2 = ["pa", "pe", "pi", "po", "pu"]
# for i in range(len(lista1)):
#     print(f"{lista1[i]} - {lista2[i]}")

# lista1 = ["ma", "me", "mi", "mo", "mu", "ja"]
# lista2 = ["pa", "pe", "pi", "po", "pu", "jo"]
# for x in zip (lista1, lista2):
#     print(x)

# nombres = ["maria", "luis", "carlos", "Juan", "Diego"]
# edades = [34, 20, 14, 18, 20]
# notas = [4, 3.8, 2, 5]
# for x in zip (nombres, edades, notas):
#     print (x)

# mi_lista = [5, 6, 3, 8, 1]
# mi_lista.sort()
# print(mi_lista)

# mi_lista = ["d", "a", "b"]
# mi_lista.sort(reverse=True)
# print(mi_lista)

# lenguajes = ["Python", "Javax", "PHP", "Java"]
# if "Javax" in lenguajes:
#     lenguajes.remove("Javax")
# print(lenguajes)

# lenguajes = ["Python", "Java", "PHP"]
# del lenguajes[1]
# print(lenguajes)

# cadena = "hola mundo"
# lista = list(cadena)
# print(lista)

# lista.reverse()
# print(lista)
# cadena = "".join(lista)
# print(lista)

# mi_tupla = (2, 3, 4, 5, 6, 9)
# print(type(mi_tupla))

# print(mi_tupla)
# print(mi_tupla[1])
# print(mi_tupla[1:3])
# print(mi_tupla[:])

# mi_tupla = ("a", "b", "c", "d")
# print(type(mi_tupla))
# mi_tupla[1] = "f"
# print(mi_tupla[1])
# print(mi_tupla)

# mi_tupla = (100, 'Hola', [1, 2, 3], -50)
# print(mi_tupla[2][-1])
# mi_tupla = (100, 'Hola', (1, (200, 'D', ["x", "y", "z"])), (1, 2, 3), -50)
# print(mi_tupla[2][1][2][1])

# mi_tupla = (1,2.5,2,6,9,3,2,78,45,3,2,0)
# print(mi_tupla.count(2))

# mi_tupla = (1,2.5,2,6,9,3,2,78,45,3,2,0)
# mi_tupla.sort()

# mi_tupla = tuple ("amomimama")
# print(mi_tupla)

# mi_lista = [1,2,3,4,5]
# print(f"{mi_lista} es de tipo {type(mi_lista)}")
# mi_tupla = tuple(mi_lista)
# print(f"{mi_tupla} es de tipo {type(mi_tupla)}")

# mi_tupla = (1,2,3,4,5)
# print(f"{mi_tupla} es de tipo {type(mi_tupla)}")
# mi_lista = list(mi_tupla)
# print(f"{mi_lista} es de tipo {type(mi_lista)}")

# mi_tupla = (3,8,5,1,9)
# mi_lista = list (mi_tupla)
# mi_lista.sort()
# mi_tupla = tuple (mi_lista)
# print (mi_tupla)

# t1 = (input("ingrese numero:"),input("ingrese numero:"),input("ingrese numero:"))
# print (t1)

# def dividir (x, y=2):
#     res = x / y
#     print(res)

# dividir(4, 3)
# dividir(8)

# def suma (*args):
#     return sum(args)

# print(f"la suma de los numeros es:", suma(5, 2.4, 5, 3, 8, 9))

# def mostrar_info(**kwargs):
#     print(type(kwargs))
#     for k in kwargs:
#         print(f"{k} -> {kwargs[k]}")

# mostrar_info(nombre="Juan", apellido="Perez")
# mostrar_info(nombre="Maria", apellido="Lopez", edad=25, telefono="1234567")

# def sumar(a, b):
#     return a + b

# print(sumar(3, 5))

# def mi_funcion():
#     return 1, "a", 3.5

# x = mi_funcion()
# print(type(x))
# print(x)

# def mi_funcion():
#     return 1, "a", 3.5

# for i in mi_funcion():
#     print(i)

# def doblar_valor(numero):
#     numero *= 2

# n = 10
# doblar_valor(n)
# print(n)

# def cambiar_valor():
#     global x
#     x = 3

# x = 5
# cambiar_valor()
# print(x)

# def factorial_recursivo(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursivo(n-1)
    
# num = int(input("Ingrese un número: "))
# print(f"El factorial de {num} es {factorial_recursivo(num)}")

# def atras(num):
#     print(num)
#     num -= 1
#     if num >= 0:
#         atras(num)

# atras(10)