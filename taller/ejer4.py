# El jefe del personal de operación de la industria aceitera Móvil desea calcular el sueldo neto de sus empleados bajo las siguientes normas, solicitar el nombre del empleado, número de horas trabajadas y la cuota por hora trabajada, para calcular el sueldo neto del empleado, se le otorga un incentivo del 5% si el empleado trabajó más de 40 horas. Imprimir el nombre del empleado y su sueldo. Desarrollar el algoritmo y diagrama de flujo.

nombre = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))

salario_bruto = horas_trabajadas * tarifa_hora

if horas_trabajadas > 40:
    incentivo = salario_bruto * 0.05
    salario_bruto += incentivo

salario_neto = salario_bruto

print("Nombre del empleado:", nombre)
print("Salario neto:", salario_neto)