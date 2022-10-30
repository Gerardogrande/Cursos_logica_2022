# Ejemplo 2. Operaciones Matematicas

# Importar una librería de funciones Matematicas: math
# SINTAXIS
import math


# ENTRADAAS DE DATOS
# Declarar o ceRrar las variables
numero_1 = float(input("Escribe el 1er número: "))
numero_2 = float(input("Escribe el 2do número: "))
# 12.55
# Declarar o crear constatntes: Elemento que su valor permanece fijo
PI = 3.1516


# procesos (Cálculos u Operaciones Matemáticas Y/Lógicas if, elif y else)
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicación = numero_1 * numero_2
división = numero_1 / numero_2

potencia1 = numero_1** numero_2
potencia2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2, 3)

raíz_cuadrada1 = math. sqrt(9)
raíz_cuadrada2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = numero_1 % numero_2




# SALIDAS DE DATOS (Mostrarlos resultados)
print("La suma es = ", round(suma, 1))
print("La suma es = " + str (suma)) #CONCATENACION: Unión de dos o más textos
# Conversión d eun tipo de dato en otro tipo de dato (CASTEO)
print (f"La suma es = {suma}") # Interpolación de textos f : Formateo

print("La resta es =", resta)
print("La resta es =" + str (resta))
print(f"La resta es = {resta}")


print("La multiplicación es =", multiplicación)
print("La multiplicación es = " + str (multiplicación))
print(f"La multiplicación es = {multiplicación}")

print("La división es =", división)
print("La división es =" + str (división))
print(f"La división es = {división}")

print(f"módulo o residuo es = {numero_1 % numero_2}")
print("El módulo o residuo es =", módulo_residuo)
print("El módulo o residuo es =" + str (módulo_residuo))


print("La potencia 1 es =", potencia1)
print("La potencia 1 es =" + str (potencia1))
print(f"La potencia 1 es = {potencia1}")

print("La potencia 2 es =", potencia2)
print("La potencia 2 es =" + str (potencia2))
print(f"La potencia 2 es = {potencia2}")

print("El cuadrado es =", cuadrado)
print("El cuadrado es " + str (cuadrado))
print(f"El cuadrado es = {cuadrado}")

print("El cubo es =", cubo)
print("El cubo es =" + str (cubo))
print(f"El cubo es = {cubo}")

print("La raíz cuadrada 1 es =", raíz_cuadrada1)
print("La raíz cuadrada 1 es =" + str (raíz_cuadrada1))
print(f"La raíz cuadrada 1 es = {raíz_cuadrada1}")

print("La raíz cuadrada 2 es =", raíz_cuadrada2)
print("La raíz cuadrada 2 es =" + str (raíz_cuadrada2))
print(f"La raíz cuadrada 2 es = {raíz_cuadrada2}")

print("La raíz cúbica es =", raíz_cúbica)
print("La raíz cúbica es =" + str (raíz_cúbica))
print(f"La raíz cúbica es = {raíz_cúbica}")