import datetime
import math

current_date = datetime.datetime.now()
print(current_date.strftime("%A %d %B %Y"))
print(current_date.strftime("%H:%M:%S"))
print("En este programa podras calcular el area de un circulo a partir de su radio")
print("Digite el valor del radio del circulo")
radio = float(input("->"))
print("En que unidades de medicion esta")
units = input("->")
Area = float(math.pi * math.pow(radio,2))
print("EL area del circulo de radio ",radio,units,"es de:",Area,units)
