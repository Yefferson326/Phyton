from Agenda_con_clases import funciones_generales
Contacts = []


def view_menu():
    consulting = True
    while consulting:
        print("\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")
        print("\t  \U0000260E\U0000260E\U0000260EAGENDA DE CONTACTOS\U0000260E\U0000260E\U0000260E")
        print("\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")
        print(" 1. LISTA DE CONTACTOS GUARDADOS")
        print(" 2. BUSCAR UN CONTACTO")
        print(" 3. CREAR UN CONTACTO")
        print(" 4. SALIR")
        print("\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")

        option = ""
        while option not in ("1", "2", "3", "4"):
            option = input("==>")
            menu = {
                "1": check_contact,
                "2": look_for_contact,
                "3": add_contact,
                "4": funciones_generales.exit
            }
            operation = menu.get(option, funciones_generales.error)
            consulting = operation()


def check_contact():
    print("\n\t\t\U0000260E\U0000260ELISTA DE CONTACTOS\U0000260E\U0000260E")
    if not Contacts:
        print("\n\t\U0000274C\U0000274CNo existe ningun contacto\U0000274C\U0000274C\n")
    else:
        order = sorted(Contacts, key=lambda contactos: contactos['Nombre'])
        j = 0
        for person in order:
            j += 1
            print("\n\t\t\U0001F464CONTACTO", j,"\U0001F464")
            print("NOMBRE:", person["Nombre"])
            print("APELLIDO:", person["Apellido"])
            print("TELEFONO:", person["Telefono"])
            print("CEDULA:", person["Cedula"])
    return funciones_generales.check_continue()


def look_for_contact():
    print("\n\t\t\U0001F50E\U0001F50E\U0001F50E BUSCAR CONTACTO \U0001F50D\U0001F50D\U0001F50D")
    if not Contacts:
        print("\t\U0000274C\U0000274C\U0000274CNo existe ningun contacto\U0000274C\U0000274C\U0000274C\n\n")
        return funciones_generales.check_continue()
    else:
        print("Seleccione el filtro con el cual desea realizar la busqueda:\n1.Nombre\n2.Apellido\n")
        user_filter = ""
        while user_filter not in ("1", "2", "3", "4"):
            user_filter = input("==>")
            filter = {
                "1": look_for_with_name,
                "2": look_for_with_last_name,
            }
            search = filter.get(user_filter, funciones_generales.error)
            search()
            return funciones_generales.check_continue()


def look_for_with_name():
    searched_name = input("Escriba el NOMBRE del contacto a buscar:")
    for person in Contacts:
        if searched_name in person["Nombre"]:
            exist = True
            break
        else:
            exist = False
    if exist:
        print("\n\t\t\U0001F464CONTACTO\U0001F464")
        print(f"NOMBRE: {searched_name}")
        print("APELLIDO:",person["Apellido"])
        print("TELEFONO:", person["Telefono"])
        print("CEDULA:",person["Cedula"])
    else:
        print(f"El contacto con el NOMBRE {searched_name} NO existe")


def look_for_with_last_name():
    searched_last_name = input("Escriba el APELLIDO del contacto a buscar:")
    for person in Contacts:
        if searched_last_name in person["Apellido"]:
            exist = True
            break
        else:
            exist = False
    if exist:
        print("\U0001F464CONTACTO\U0001F464")
        print(f"NOMBRE:", person["Nombre"])
        print(f"APELLIDO: {searched_last_name}")
        print("TELEFONO:", person["Telefono"])
        print("CEDULA:",person["Cedula"])
    else:
        print(f"El contacto con APELLIDO {searched_last_name} NO existe")


def add_contact():
    print("\n\t\t\U0000260E\U0000260EAGREGA UN CONTACTO\U0000260E\U0000260E")
    new_contact = {
       'Nombre': input("Nombre:").lower(),
       'Apellido': input("Apellido:").lower(),
       'Telefono': funciones_generales.check_tel(),
       'Cedula': check_ced()
    }
    contacts(new_contact)
    return funciones_generales.check_continue()


def contacts(new_contact):
    Contacts.append(new_contact)
    print("\n\U00002714El contacto con Nombre <<" + new_contact['Nombre']+">> se guardo Exitosamente\U00002714\n\n")


def check_ced():
    type_ced = True
    while type_ced:
        user_ced = input("N° de Cedula: ")
        try:
            int(user_ced)
            type_ced = False
            return user_ced
        except ValueError:
            print("\U000026A0\U000026A0El N° de Cedula debe ser un numero entero\U000026A0\U000026A0\n\t\t\U0001F449Intente de nuevo\U0001F448")
            type_ced


view_menu()
