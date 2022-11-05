
# ENTRDA DE DATOS

nombre = str(input("Ingresa tu nombre: "))
mes = str(input("Ingresa el nombre del mes: "))
días_laborados = float(input("Ingrsa el número de días del mes: "))
pago_por_día = float(input("Ingresa el pago por día: "))



# PROCESO

pago_base = días_laborados * pago_por_día
iva_trasladado = pago_base * 0.16
subtotal = pago_base + iva_trasladado
iva_retenido = (2/3) * iva_trasladado
isr_retenido = pago_base * 0.10
pago_neto = subtotal - iva_retenido - isr_retenido

# SALIDA DE DATOS
print(nombre, "tu pago neto en el mes de", str(mes), "es de =", round(pago_neto, 2))
print(str(nombre), "tu pago neto en el mes de", str(mes), "es de = " + str(round(pago_neto, 2)))
print(str(nombre), f"tu pago neto en el mes de {str(mes)} es de = {round(pago_neto, 2)}")