print("En este programa podras verificar si el número ingresado es PAR o IMPAR")
repeat = int(1)

while (repeat == 1):
    num = int(input("Ingrese un numero\n->"))
    checkPairOrOdd = num % 2
    if checkPairOrOdd == 0:
        print("El número (",num,") es un número PAR")
    else:
        print("El número(", num, ") es un número IMPAR")
    print ("¿Desea ingresar otro número?")
    repeat = int (input("1.Si\n2.No\n->"))
print("¡Hasta la proxima!")