# Hacer una función para que imprima un arreglo o lista de 10 elementos numéricos

areglo = [9, 5, 2, 8, 6, 3, 7, 4, 1, 10]

def Imprimir_Arreglo_De_Números(areglo):
    return areglo

# OPERACIONES CON AREGLOS O LISTAS
# Modificar un elemento del arreglo
areglo[5] = 30
# Agregar un elemento al arreglo
areglo.append(55)
# Eliminar un elemento del arrgelo
areglo.pop(0)
# Vaciar el arreglo
# areglo.clear()
# Ordenar el arreglo en orden ASC
areglo.sort()
# Ordenar el arreglo en orden DSC
areglo.reverse()

# SALIDA DE DATOS
print("El arreglo de los números es: ", Imprimir_Arreglo_De_Números(areglo))
