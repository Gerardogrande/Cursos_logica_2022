'''''
APROBADO                mayor  a 6 hasta 10
APROBADO DE PANSASO     iual a 6
REPROBADO               de 0 a menor que 6
PROMEDIO INVALIDO       menor que 0 o mayor que 10
'''''
# Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

# Entrada de datos:
calificación_1 = float(input("Escribe la 1er calificación: "))
calificación_2 = float(input("Escribe la 2da calificación: "))
calificación_3 = float(input("Escribe la 3er calificación: "))

# PROCESO:
promedio = (calificación_1 + calificación_2 + calificación_3) / 3

# SALIDA DE DATOS
if(promedio > 6 and promedio <= 10):
    print("Tu promedio es =", round(promedio, 1))
    print("Estatus: Aprobado")
elif(promedio == 6):
    print("Tu promedio es = " + str(promedio))
    print("Estatus: Aprobado de pansaso")
elif(promedio >= 0 and promedio < 6):
    print(f"Tu promedio es = {round(promedio, 1)}")
    print("Estatus: Rrepobado")
else:
    print("PROMEDIO INVALIDO")