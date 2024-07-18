# Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo.

#   Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como negativo.
# La tabla en la que el medico se basa para obtener el
# resultado es la siguiente:
# 0 - 1 mes: 13 - 26 g%
# > 1 y < = 6 meses: 10 - 18 g%
# >6 y < = 12 meses: 11 - 13 g%
# > 1 y < = 5 años: 11.5 - 15 g%
# > 5 y < = 10 años: 12.6 - 15.5 g%
# > 10 y < = 15 años: 13 - 15.5 g%
# mujeres > 15 años: 12 - 16 g%
# hombres > 15 años: 14 - 18 g%

def verificar_anemia(hemoglobina, edad, sexo):
    if edad <= 1:
        if hemoglobina < 13 or hemoglobina > 26:
            return "Positivo"
    elif edad <= 6:
        if hemoglobina < 10 or hemoglobina > 18:
            return "Positivo"
    elif edad <= 12:
        if hemoglobina < 11 or hemoglobina > 13:
            return "Positivo"
    elif edad <= 5:
        if hemoglobina < 11.5 or hemoglobina > 15:
            return "Positivo"
    elif edad <= 10:
        if hemoglobina < 12.6 or hemoglobina > 15.5:
            return "Positivo"
    elif edad <= 15:
        if hemoglobina < 13 or hemoglobina > 15.5:
            return "Positivo"
    elif sexo == "femenino":
        if hemoglobina < 12 or hemoglobina > 16:
            return "Positivo"
    elif sexo == "masculino":
        if hemoglobina < 14 or hemoglobina > 18:
            return "Positivo"
    
    return "Negativo"

# Ejemplo de uso
resultado = verificar_anemia(12, 25, "femenino")
print(resultado)  # Salida: Negativo