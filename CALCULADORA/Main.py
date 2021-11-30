print(" _______   _______  __       _______  __    __   __       _______   ___    _______   ______  _______")
print("|   ____| |   _   ||  |     |   ____||  |  |  | |  |     |   _   | |   \  |       | |   _  ||   _   |")
print("|  |      |  |_|  ||  |     |  |     |  |  |  | |  |     |  |_|  | | |\ \ |   _   | |  |_| ||  |_|  |")
print("|  |      |   _   ||  |     |  |     |  |  |  | |  |     |   _   | | | \ \|  | |  | |    __||   _   |")
print("|  |      |  | |  ||  |     |  |     |  |  |  | |  |     |  | |  | | | / /|  |_|  | |    \  |  | |  |")
print("|  |____  |  | |  ||  |____ |  |____ |  |__|  | |  |____ |  | |  | | |/ / |       | |  |\ \ |  | |  |")
print("|_______| |__| |__||_______||_______||________| |_______||__| |__| |___/  |_______| |__| |_\|__| |__|")

def getNumOne ():
    print("Ingrese el primer número")
    num1 = float(input("-->"))
    return  num1
def getNumTwo():
    print("Ingrese el segundo número")
    num2 = float(input("-->"))
    return num2
def checkContinue ():
    print("Desea realizar otra operacion\n1.SI\n2.NO")
    repeat = int(input("-->"))
    return repeat
print("\t\t#####Es este programa podras realizar operaciones basicas para dos numeros#####")
repeat = 1
num1= float()
num2= float()
while (repeat == 1):
    print("¿Que operacion desea realizar?")
    print("1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION")
    operation= int(input("-->"))
    if operation == 1:
        print("\t\t##SUMA##")
        num1= getNumOne()
        num2= getNumTwo()
        print("\t",num1," + ",num2," = ",num1+num2)
        repeat =  checkContinue()
    elif operation == 2:
        print("\t\t##RESTA##")
        num1= getNumOne()
        num2= getNumTwo()
        print("\t",num1, " - ", num2, " = ", num1 - num2)
        repeat =  checkContinue()
    elif operation == 3:
        print("\t\t##MULTIPLICACION##")
        num1 = getNumOne()
        num2 = getNumTwo()
        print("\t",num1, " x ", num2, " = ", num1 * num2)
        repeat =  checkContinue()
    elif operation == 4:
        checkDivisor = 1
        while checkDivisor == 1:
            print("\t\t##DIVISION##")
            num1 = getNumOne()
            num2 = getNumTwo()
            if num2 == 0:
                print("\t¡¡El resultado de ",num1," entre ",num2," da un valor indefinido¡¡\n\t<<Por favor ingrese un valor para el divisor diferente de 0>>\n")
            else:
                break
        print("\t",num1, "/", num2, "=", num1 / num2)
        repeat = checkContinue()
    else:
        print("\t¡¡Opcion incorrecta¡¡\n\t  Intente de nuevo")
        repeat = 1
print("¡¡HASTA PRONTO¡¡")
