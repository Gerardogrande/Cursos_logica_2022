# Obtener un número y determinar lo siguiente:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# c) en otro caso imprimir No Válido

j = número = float(input("Ingresa un número: "))

if (j < 0 and j > -100):
    for j in range(-1, -100, -2):
         print(f"{j}")
elif(j > 0 and j < 100):
    for j in range(2, 101, 2):
        print(f"{j}")
else:
    print("Número Inválido")
    