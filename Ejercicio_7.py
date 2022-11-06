
# Pedir el nivel del agua en metros de una cisterna

nivel_del_agua = float(input("Escribe el nivel del agua en metros: "))


if(nivel_del_agua < 0):                             # menor a 0 m fuga en sisterna
    print("Fuga en Sisterna")
elif(nivel_del_agua == 0):                          # nivel de 0 m Encender bomba de agua
    print("Encender Bomba de Agua")
elif(nivel_del_agua > 0 and nivel_del_agua < 2):    # Entre 0 m y 2 m Acelerar bomba de agua
    print("Acelerar Bombda Agua")
elif(nivel_del_agua > 2 and nivel_del_agua < 4):    # Entre 2 m y 4 m Bomba trabajando
    print("Bomba Trabajando")
elif(nivel_del_agua > 4 and nivel_del_agua < 6):    # Entre 4m y 6 m Desacelerar bomba
    print("Desacelerar Bomba")
elif(nivel_del_agua == 6):                          # Nivel de 6 m. Apagar bomba
    print("Apagar Bomba")
elif(nivel_del_agua > 6):                           # Si llega más de 6 m. Desbordamiento de agua en cisterna
    print("Desbordamiento de Agua en Cisterna")