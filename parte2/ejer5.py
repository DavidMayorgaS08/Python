# Leer un password de ingreso a un programa y mostrar el mensaje de bienvenida si es correcto. Mientras no lo sea, debe mostrar el mensaje de Password incorrecto. El programa debe terminar automáticamente al quinto intento fallido.

password_correcto = "asd"
intentos = 0

while intentos < 5:
    password = input("Ingrese la contraseña: ")

    if password == password_correcto:
        print("¡Bienvenido!")
        break
    else:
        print("Contraseña incorrecta.")
        intentos += 1

if intentos == 5:
    print("Has excedido el número máximo de intentos. El programa se cerrará.")