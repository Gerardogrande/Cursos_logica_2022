# FUNCIONES / PROCEDIMIENTOS / MÉTODOS / RUTINAS
# Sonacciones o tareas a ejecutar (vervos en ar, er, ir)
# SINTAXIS
'''
def Nombre_de_la_Funcion ( Argumento o Parámetro ):
    contenido de la funcion de la función
    return valor(es)
'''
# DECLARAR LAS FUNCIONES
def Sumar (num1, num2):     # Obtener o recibir los parámetros
    return num1 + num2 #Retornar, Devolver, Retornar un valor

def Restar (a, b):
  resta = a - b
  print("La resta es =", resta)

def Multiplicar (x, y):
    return x * y

def División (dividendo, divisor):
    return dividendo / divisor

# Mndar a llamar o invocar las funciones
# Imprimir el resultado
suma = Sumar(10, 5)             # Enviar o pasar los parámetros
resta = Restar (50, 20)

# Imprimir e resultado
print("La suma es ", Sumar (10, 5))
Restar (1, 2)

# Imrpimir resultado
print("La multiplicación es =", Multiplicar(2, 10))

# Imprimr resultado
print("La división es = ", División(50, 5))
