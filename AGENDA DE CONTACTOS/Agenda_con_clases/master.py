
import funciones_generales


class Contact:
    def __init__(self, nombre, apellido, apodo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono


class Agenda:
    def __init__(self):
        self.Contacts = []

    def menu(self):
        print("\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")
        print("\t  \U0000260E\U0000260E\U0000260EAGENDA DE CONTACTOS\U0000260E\U0000260E\U0000260E")
        print("\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")
        print("\U0001F4D8 1. CREAR UN CONTACTO")
        print("\U0001F4D8 2. BUSCAR UN CONTACTO")
        print("\U0001F4D8 3. ELIMINAR CONTACTO")
        print("\U0001F4D8 4. LISTA DE CONTACTOS GUARDADOS")
        print("\U0001F4D8 5. SALIR")
        print("\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")

        option = input("Introduce una opcion ==> ")
        if option == "1":
            self.addContact()
        elif option == "2":
            self.searchContact()
        elif option == "3":
            self.removeContact()
        elif option == "4":
            self.showContacts(1)
        elif option == "5":
            funciones_generales.exit()
        else:
            funciones_generales.error()
            self.menu()

    def addContact(self):
        print("\n\t\t\U0000260E\U0000260EAGREGA UN CONTACTO\U0000260E\U0000260E")
        nombre = input("NOMBRE:")
        apellido = input("APELLIDO:")
        apodo = input("APODO:")
        telefono = funciones_generales.check_tel()
        if not self.Contacts:
            newContact = Contact(nombre, apellido, apodo, telefono)
            self.Contacts.append(newContact)
            print("\n\U00002714El contacto con Nombre <<" + nombre.upper() + ">> se guardo Exitosamente\U00002714\n")
        else:
            for contact in self.Contacts:
                if telefono == contact.telefono:
                    exitNumber = True
                    break
                else:
                    exitNumber = False
            if exitNumber:
                print(f"¡¡¡El contacto con el numero [{telefono}] YA EXISTE¡¡¡")
                input("\t\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")
            else:
                newContact = Contact(nombre, apellido, apodo, telefono)
                self.Contacts.append(newContact)
                print("\n\U00002714El contacto con Nombre <<" + nombre.upper() + ">> se guardo Exitosamente\U00002714\n")
                input("\t\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")
        self.menu()

    def searchContact(self):
        print("\n\t\t\U0001F50E\U0001F50E\U0001F50E BUSCAR CONTACTO \U0001F50D\U0001F50D\U0001F50D")
        if not self.Contacts:
            print("_____________________________________________")
            print("  ¡¡¡NO EXISTE NINGUN CONTACTO GUARDADO¡¡¡")
            print("_____________________________________________")
            input(" \U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")
            self.menu()
        else:
            d = ""
            while d != ("1", "2", "3"):
                print("Seleccione el filtro con el cual desea realizar la busqueda:\n1.Nombre\n2.Apodo\n3.Telefono")
                d = input("==> ")
                if d == "1":
                    self.searchContactWithName()
                    self.menu()
                elif d == "2":
                    self.searchContactWithNickname()
                    self.menu()
                elif d == "3":
                    self.searchContactWithPhone()
                    self.menu()
                else:
                    funciones_generales.error()


    def searchContactWithName(self):
        searched_name = input("Escriba el NOMBRE del contacto a buscar:")
        funciones_generales.checkcontact(self.Contacts,searched_name,1)


    def searchContactWithNickname(self):
        searched_nickname = input("Escriba el APODO del contacto a buscar:")
        funciones_generales.checkcontact(self.Contacts, searched_nickname, 2)

    def searchContactWithPhone(self):
        searched_phone = int(input("Escriba el TELEFONO del contacto a buscar:"))
        funciones_generales.checkcontact(self.Contacts, searched_phone, 3)

    def removeContact(self):
        if not self.Contacts:
            print("_____________________________________________")
            print("  ¡¡¡NO EXISTE NINGUN CONTACTO GUARDADO¡¡¡")
            print("_____________________________________________")
        else:
            self.showContacts(2)
            numContactRemove = int(input("\nINGRESA EL NUMERO TELEFONICO DEL CONTACTO QUE DESEA ELIMINAR:"))
            for contact in self.Contacts:
                if numContactRemove == contact.telefono:
                    numberFound = True
                    numContact = self.Contacts.index(contact)
                    break
                else:
                    numberFound = False
            if numberFound:
                self.Contacts.pop(numContact)
                print(f"\n\U00002705El contacto guardado con el numero telefonico({numContactRemove})fue ELIMINADO correctamente\U00002705")
            else:
                print(f"\n\U0001F44BEl numero telefonico {numContactRemove} NO coincide con el de ningun contacto guardado\U0001F44B")
        input(" \U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")
        self.menu()

    def showContacts(self, a):
        i = 0
        print("\n\t\t\U0000260E\U0000260ELISTA DE CONTACTOS\U0000260E\U0000260E\n")
        if not self.Contacts:
            print("_____________________________________________")
            print("  ¡¡¡NO EXISTE NINGUN CONTACTO GUARDADO¡¡¡")
            print("_____________________________________________")
        else:
            contactsOrder = sorted(self.Contacts, key=lambda contact: contact.nombre)
            for contact in contactsOrder:
                i += 1
                print("\t\t   \U0001F464 CONTACTO",i,"\U0001F464")
                print(f"NOMBRE:{contact.nombre}")
                print(f"APELLIDO:{contact.apellido}")
                print(f"TELEFONO:{contact.telefono}")
                print("________________________________")
        if a == 1:
            input(" \U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")
            self.menu()
        else:
            pass

A = Agenda
A().menu()


