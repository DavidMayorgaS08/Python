# Realiza una función que reciba un número y devuelva una cadena con los nombres de los números recibidos, separando cada número con un guión medio.  Por ejemplo, si el número recibido es 134, la función devolverá la cadena "uno - tres - cuatro"
def nombres_numeros(numero):
    nombres = {
        '0': 'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve'
    }
    
    cadena = ''
    for digito in str(numero):
        if digito in nombres:
            cadena += nombres[digito] + ' - '
    
    return cadena.rstrip(' - ')

numero = input("Ingrese un número: ")
cadena_numeros = nombres_numeros(numero)
print(cadena_numeros)