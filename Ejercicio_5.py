
# Obtener valores para: a, b y c. Calcular la fórmula general.


# ENTRADA DE DATOS
from cmath import sqrt


a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))


# PROCESO
x_1 = (-b + ((b**2 - (4*a*c))**1/2)) / (2*a)
x_2 = (-b - ((b**2 - (4*a*c))**1/2)) / (2*a)



# SALIDA DE DATOS
print("x_1 es =", round(x_1, 1))
print("x_1 es = " + str(round(x_1, 1)))
print(f"x_1 es = {round(x_1, 1)}")

print("x_2 es =", round(x_2, 1))
print("x_1 es = " + str(round(x_2, 1)))
print(f"x_1 es = {round(x_2, 1)}")