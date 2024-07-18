estudiantes = []

# Función para agregar un estudiante
def agregar_estudiante(id, nombre, edad, nota):
    estudiante = {
        'id': id,
        'nombre': nombre,
        'edad': edad,
        'nota': nota
    }
    estudiantes.append(estudiante)

# Función para mostrar la información de todos los estudiantes
def mostrar_todos_los_estudiantes():
    for estudiante in estudiantes:
        print(f"ID: {estudiante['id']}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Nota: {estudiante['nota']}")

# Función para mostrar la información de un estudiante específico
def mostrar_informacion_estudiante(id):
    for estudiante in estudiantes:
        if estudiante['id'] == id:
            print(f"ID: {estudiante['id']}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Nota: {estudiante['nota']}")
            return
    print("No se encontró información para el estudiante con ese ID.")

# Agregar estudiantes
agregar_estudiante(1, "Juan", 20, 85)
agregar_estudiante(2, "Maria", 19, 90)
agregar_estudiante(3, "Pedro", 21, 75)
agregar_estudiante(4, "Ana", 18, 95)
agregar_estudiante(5, "Luis", 22, 80)

# Mostrar todos los estudiantes
print("Información de todos los estudiantes:")
mostrar_todos_los_estudiantes()

# Mostrar información de un estudiante específico
id_estudiante = int(input("Ingrese el ID del estudiante para mostrar su información: "))
print("Información del estudiante:")
mostrar_informacion_estudiante(id_estudiante)