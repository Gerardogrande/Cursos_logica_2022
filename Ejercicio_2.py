
# Calcular el área y perímetro de un círculo.


# ENTRADA DE DATOS
radio = float(input("Escribe el valor del radio: "))

# DECLARAR CONSTANTES
pi = 3.14159265


# PROCESO
# OPCIÓN 1
perímetro = 2*pi*radio
área = pi* (radio**2)

# opción 2
área2 = pi*pow(radio, 2)


# SALIDA DE DATOS

# PERÍMETRO
print("El perímetro es =", round(perímetro, 2))
print("El perímetro es = " + str(round(perímetro, 2)))
print(f"El perímetro = {round(perímetro, 2)}")

# ÁREA
print("El área es =", round(área, 2))
print("El área es = " + str(round(área, 2)))
print(f"El área es = {round (área, 2)}")