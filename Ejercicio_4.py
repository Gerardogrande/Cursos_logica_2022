
# Pedir la cantidad de grados y convertirlos a °C, °F y K.

# ENTRADA DE DATOS

grados = float(input("Escribe el número de grados: "))


# PROCESO

celsius_1 = grados - 273.5
celsius_2 = ( 5* (grados - 32)) / 9
kelvin_1 = grados + 273.15
kelvin_2 = ((5 * (grados - 32)) / 9) + 273.15
fahrenheit_1 = ((9 * grados) / 5) + 32
fahrenheit_2 = ((9 * (grados - 273.15)) / 5) + 32




# SALIDA DE DATOS
print("Grados celcius_1 es =", round(celsius_1, 2))
print("Grados celcius_1 es = " + str (round(celsius_1, 2)))
print(f"Grados celcius_1 es = {round(celsius_1, 2)}")

print("Grados celcius_2 es =", round(celsius_2, 2))
print("Grados celsius_2 es =" + str(round(celsius_2, 2)))
print(f"Grados celsius_2 es = {round(celsius_2, 2)}")

print("Grados kelvin__1 es =", round(kelvin_1, 2))
print("Grados kelvin_1 es = " + str(round(kelvin_1, 2)))
print(f"Grados kelvin_1 es = {round(kelvin_1, 2)}")

print("Grados kelvin_2 es =", round(kelvin_2, 2))
print("Grados kelvin_2 es = " + str(round(kelvin_2, 2)))
print(f"Grados kelvin_2 es = {round(kelvin_2, 2)}")

print("Grados fahrenheit_1 es =", round(fahrenheit_1, 2))
print("Grados faherenheit_1 es = " + str(round(fahrenheit_1, 2)))
print(f"grados faherenheit_1 es = {round(fahrenheit_1, 2)}")

print("Grados fahrenheit_2 es =", round(fahrenheit_2, 2))
print("Grados fahrenheit_2 es = " + str(round(fahrenheit_2, 2)))
print(f"Grados fahrenheit_2 es = {round(fahrenheit_2, 2)}")