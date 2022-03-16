
def check_continue():
    option = ""
    while option != ("1", "2"):
        print("\U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0  \U000026A0")
        print("\t¿Desea regresar al menu?\n1.SI\n2.NO")
        option = input("-->")

        if option == "1":
            return True
        elif option == "2":
            exit()
            return False
        else:
            error()


def exit():
    print("\t\t\U0001F44B\U0001F44B\U0001F44B\U0001F44BHASTA LUEGO\U0001F44B\U0001F44B\U0001F44B\U0001F44B")
    return False


def error():
    print("\n\t\U0000274C\U0000274C\U0000274COPCION INCORRECTA\U0000274C\U0000274C\U0000274C\n\t    ¡Intenta de nuevo¡")
    input("\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")


def check_tel():
    type_num = True
    while type_num:
        user_num = input("N° de telefono: ")
        try:
            int(user_num)
            type_num = False
            return int(user_num)
        except ValueError:
            print("\U000026A0\U000026A0El N° de telefono debe ser un numero entero\U000026A0\U000026A0\n\t\t\U0001F449Intente de nuevo\U0001F448")


def checkcontact(Contacts, searchedContact, d):
    if d == 1:
        for contact in Contacts:
            if searchedContact == contact.nombre:
                mostrarContactoEncontrado(contact)
                noFoundContact = False
                break
            else:
                noFoundContact = True
        if noFoundContact:
            mostrarContactoNoEncontrado(contact,searchedContact,"NOMBRE")
    elif d == 2:
        for contact in Contacts:
            if searchedContact == contact.apodo:
                mostrarContactoEncontrado(contact)
                noFoundContact = False
                break
            else:
                noFoundContact = True
        if noFoundContact:
            mostrarContactoNoEncontrado(contact,searchedContact,"APODO")
    elif d == 3:
        for contact in Contacts:
            if searchedContact == contact.telefono:
                mostrarContactoEncontrado(contact)
                noFoundContact = False
                break
            else:
                noFoundContact = True
        if noFoundContact:
            mostrarContactoNoEncontrado(contact,searchedContact,"TELEFONO")


def mostrarContactoEncontrado (contact):
    print("\n\t\t\U0001F464CONTACTO\U0001F464")
    print(f"NOMBRE: {contact.nombre}")
    print(f"APELLIDO:{contact.apellido}")
    print(f"APODO:{contact.apodo}")
    print(f"TELEFONO:{contact.telefono}")
    input("\n\t\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")


def mostrarContactoNoEncontrado (contact,searchedContact,filtro):
    print(f"El contacto con el {filtro} ({searchedContact}) NO existe")
    input("\n\t\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")