def print_message_welcome():
    print(" _______   _______  __       _______  __    __   __       _______   ___    _______   ______  _______")
    print("|   ____| |   _   ||  |     |   ____||  |  |  | |  |     |   _   | |   \  |       | |   _  ||   _   |")
    print("|  |      |  |_|  ||  |     |  |     |  |  |  | |  |     |  |_|  | | |\ \ |   _   | |  |_| ||  |_|  |")
    print("|  |      |   _   ||  |     |  |     |  |  |  | |  |     |   _   | | | \ \|  | |  | |    __||   _   |")
    print("|  |      |  | |  ||  |     |  |     |  |  |  | |  |     |  | |  | | | / /|  |_|  | |    \  |  | |  |")
    print("|  |____  |  | |  ||  |____ |  |____ |  |__|  | |  |____ |  | |  | | |/ / |       | |  |\ \ |  | |  |")
    print("|_______| |__| |__||_______||_______||________| |_______||__| |__| |___/  |_______| |__| |_\|__| |__|")
    print("\t\t#####Es este programa podras realizar operaciones basicas para dos numeros#####")


def request_number_one():
    print("Ingrese el primer número")
    number_one = float(input("-->"))
    return number_one


def request_number_two():
    print("Ingrese el segundo número")
    number_two = float(input("-->"))
    return number_two


def check_continue():
    print("Desea realizar otra operacion\n1.SI\n2.NO")
    return int(input("-->"))


def message_menu():
    print("¿Que operacion desea realizar?")
    print("1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION\n5.SALIR")
    return int(input("-->"))


def operation_sum():
    print("\t\t##SUMA##")
    num_one = request_number_one()
    num_two = request_number_two()
    print("\t", num_one, " + ", num_two, " = ", num_one + num_two)
    return check_continue()


def operation_rest():
    print("\t\t##RESTA##")
    num_one = request_number_one()
    num_two = request_number_two()
    print("\t", num_one, " - ", num_two, " = ", num_one - num_two)
    return check_continue()


def operation_multiplication():
    print("\t\t##MULTIPLICACION##")
    num_one = request_number_one()
    num_two = request_number_two()
    print("\t", num_one, " x ", num_two, " = ", num_one * num_two)
    return check_continue()


def operation_division():
    check_divider = 1
    while check_divider == 1:
        print("\t\t##DIVISION##")
        dividend = request_number_one()
        divider = request_number_two()
        if divider == 0:
            print("\t¡¡El resultado de ", dividend, " entre ", divider,
                  " da un valor indefinido¡¡\n\t<<Por favor ingrese un valor para el divisor diferente de 0>>\n")
        else:
            break
    print("\t", dividend, "/", divider, "=", dividend / divider)
    return check_continue()


def error():
    print("\t¡¡Opcion incorrecta¡¡\n\t  Intente de nuevo")


def option_select(user_option):
    menu = {
        1: operation_sum,
        2: operation_rest,
        3: operation_multiplication,
        4: operation_division
    }
    operation = menu.get(user_option,error)
    return operation()


print_message_welcome()
repeat = 1
while repeat == 1:
    user_option = message_menu()
    repeat = option_select(user_option)
print("¡¡HASTA PRONTO¡¡")
