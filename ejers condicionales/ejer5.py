# En un sistema de control de calidad, se deben inspeccionar las piezas de un producto para determinar si cumplen con los estándares de calidad. Si la pieza es defectuosa, se debe marcar como rechazada y enviar una alerta al operador. Si la pieza cumple con los estándares de calidad, se debe marcar como aprobada y continuar con la producción.  Realice un programa que lea una entrada binaria en la que los 1s significan estándares de calidad cumplidos y los 0s significan estándares de calidad No cumplidos.  El programa debe rechazar la pieza ante cualquier estándar no cumplido.

def verificar_calidad(entrada):
    if '0' in entrada:
        print("Pieza rechazada. No se cumplen los estándares de calidad.")
        # Enviar alerta al operador
    else:
        print("Pieza aprobada. Se cumplen los estándares de calidad.")
        # Continuar con la producción

entrada_binaria = input("Ingresa la entrada binaria: ")
verificar_calidad(entrada_binaria)