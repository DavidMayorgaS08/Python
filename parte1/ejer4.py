# Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del examen final. 15% de la calificación de un trabajo final

parcial1 = float(input("Ingresa la primera nota parcial: "))
parcial2 = float(input("Ingresa la segunda nota parcial: "))
parcial3 = float(input("Ingresa la tercera nota parcial: "))

examen_final = float(input("Ingresa la nota del examen final: "))

proyecto_final = float(input("Ingresa la nota del proyecto final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

nota_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (proyecto_final * 0.15)

print("Tu nota final en la asignatura de Matemáticas es:", nota_final)