
# Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

# Entrada de datos:
calificación_1 = float(input("Escribe la 1er calificación: "))
calificación_2 = float(input("Escribe la 2da calificación: "))
calificación_3 = float(input("Escribe la 3er calificación: "))


# PROCESO:
suma = calificación_1 + calificación_2 + calificación_3
promedio = suma / 3

# SALIDA DE DATOS
print("El promedio es = ", round(promedio, 1))
print("El promedio es = " + str(round(promedio, 1)))
print(f"El promedio es = {round(promedio, 1)}")