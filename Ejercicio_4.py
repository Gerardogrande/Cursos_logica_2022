
# Pedir la cantidad de grados y convertirlos a °C, °F y K.

# ENTRADA DE DATOS

grados = float(input("Escribe el número de grados: "))


# PROCESO
fahrenheit = ((9 * grados) / 5) + 32
kelvin = grados + 273.15



# SALIDA DE DATOS
print("Grados fahrenheit es =", round(fahrenheit, 2))
print("Grados faherenheit es = " + str(round(fahrenheit, 2 )))
print(f"grados faherenheit = {round(fahrenheit, 2)}")


print("Grados kelvin =", round(kelvin, 2))
print("Grados kelvin = " + str(round(kelvin, 2)))
print(f"Grados kelvin = {round(kelvin, 2)}")