# En un partido de fútbol, se ofrece un descuento a los aficionados que depende del estrato y la edad.  Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la boleta.   Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%.  Si  el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o más, el descuento será del 5%.  Determinar el total del dinero recaudado y descontado por las últimas N personas que ingresan al partido.

def calcular_descuento(estrato, edad):
    if estrato == 1:
        if edad < 18:
            descuento = 0.2
        else:
            descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            descuento = 0.1
        else:
            descuento = 0.05
    else:
        descuento = 0
    
    return descuento

def calcular_recaudado(personas, estratos, edades):
    total_recaudado = 0
    total_descuentos = 0
    
    for i in range(personas):
        descuento = calcular_descuento(estratos[i], edades[i])
        valor_boleta = 100  # Valor de la boleta
        
        descuento_aplicado = valor_boleta * descuento
        total_recaudado += valor_boleta
        total_descuentos += descuento_aplicado
    
    return total_recaudado, total_descuentos

# Ejemplo de uso
personas = 5
estratos = [1, 2, 1, 2, 1]
edades = [15, 20, 18, 16, 19]

recaudado, descuentos = calcular_recaudado(personas, estratos, edades)
print(f"Total recaudado: {recaudado}")
print(f"Total descuentos: {descuentos}")