# Lista para almacenar los estudiantes inscritos en fútbol
futbol = []

# Lista para almacenar los estudiantes inscritos en baloncesto
baloncesto = []

# Lista para almacenar los estudiantes inscritos en ambos deportes
ambos_deportes = []

# Lista para almacenar todos los estudiantes inscritos en algún deporte
todos_deportes = []

# Lista para almacenar los estudiantes inscritos en solo un deporte
un_deporte = []

# Función para inscribir a un estudiante en fútbol
def inscribir_futbol(estudiante):
    futbol.append(estudiante)
    todos_deportes.append(estudiante)
    un_deporte.append(estudiante)

# Función para inscribir a un estudiante en baloncesto
def inscribir_baloncesto(estudiante):
    baloncesto.append(estudiante)
    todos_deportes.append(estudiante)
    un_deporte.append(estudiante)

# Función para inscribir a un estudiante en ambos deportes
def inscribir_ambos_deportes(estudiante):
    futbol.append(estudiante)
    baloncesto.append(estudiante)
    ambos_deportes.append(estudiante)
    todos_deportes.append(estudiante)

# Función para mostrar los listados de estudiantes inscritos
def mostrar_listados():
    print("Estudiantes inscritos en fútbol:")
    for estudiante in futbol:
        print(estudiante)
    
    print("\nEstudiantes inscritos en baloncesto:")
    for estudiante in baloncesto:
        print(estudiante)
    
    print("\nEstudiantes inscritos en ambos deportes:")
    for estudiante in ambos_deportes:
        print(estudiante)
    
    print("\nTodos los estudiantes inscritos en algún deporte:")
    for estudiante in todos_deportes:
        print(estudiante)
    
    print("\nEstudiantes inscritos en solo un deporte:")
    for estudiante in un_deporte:
        print(estudiante)

# Ejemplo de uso del programa
inscribir_futbol("Juan")
inscribir_baloncesto("Pedro")
inscribir_ambos_deportes("María")
inscribir_futbol("Luis")
inscribir_baloncesto("Ana")

mostrar_listados()