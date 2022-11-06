
# Pedir el nivel del agua en metros de una cisterna

nivel_del_agua = float(input("Escribe el nivel del agua en metros: "))

# SALIDA DE DATOS
if(nivel_del_agua < 0):
    print("Fuga en Sisterna")
elif(nivel_del_agua == 0):
    print("Encender Bomba de Agua")
elif(nivel_del_agua > 0 and nivel_del_agua <= 2):
    print("Acelerar Bomba de Agua")
elif(nivel_del_agua > 2 and nivel_del_agua <= 4):
    print("Bomba Trabajando")
elif(nivel_del_agua > 4 and nivel_del_agua < 6):
    print("Desacelerar Bomba")
elif(nivel_del_agua == 6):
    print("Apagar Bomba")
else:
    print("Desbordamiento de Agua en Cisterna")