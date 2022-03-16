from src.Models.contact import Contact


class View:
    def menu(self):
        print(
            "\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")
        print("\t  \U0000260E\U0000260E\U0000260EAGENDA DE CONTACTOS\U0000260E\U0000260E\U0000260E")
        print(
            "\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")
        print("\U0001F4D8 1. CREAR UN CONTACTO")
        print("\U0001F4D8 2. BUSCAR UN CONTACTO")
        print("\U0001F4D8 3. ELIMINAR CONTACTO")
        print("\U0001F4D8 4. LISTA DE CONTACTOS GUARDADOS")
        print("\U0001F4D8 5. GUARDAR CONTACTOS")
        print("\U0001F4D8 6. CARGAR CONTACTOS")
        print("\U0001F4D8 7. SALIR")
        print("\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8")
        return input("Introduce una opcion ==> ")

    def addContact(self):
        print("\n\t\t\U0000260E\U0000260EAGREGA UN CONTACTO\U0000260E\U0000260E")
        nombre = input("NOMBRE:")
        apellido = input("APELLIDO:")
        apodo = input("APODO:")
        telefono = input("TELEFONO:")
        return Contact(nombre,apellido,apodo,telefono)

    def checkPhone(self):
        return input("Ingrese de nuevo el TELEFONO:")

    def noIsANumber(self):
        print("\U000026A0\U000026A0El N° de telefono debe ser un numero entero\U000026A0\U000026A0\n\t\t\U0001F449Intente de nuevo\U0001F448")

    def contactSavedSuccessfully (self,name):
        print(f"\n\U00002714El contacto con Nombre ({name}) se guardo Exitosamente\U00002714\n")

    def contactExist(self,telefono):
        print(f"¡¡¡El contacto con el numero [{telefono}] YA EXISTE¡¡¡")

    def searchContactMesagge(self):
        print("\n\t\t\U0001F50E\U0001F50E\U0001F50E BUSCAR CONTACTO \U0001F50D\U0001F50D\U0001F50D")

    def emptyContactList(self):
        print("_____________________________________________")
        print("  ¡¡¡NO EXISTE NINGUN CONTACTO GUARDADO¡¡¡")
        print("_____________________________________________")

    def searchContact(self):
        print("Seleccione el filtro con el cual desea realizar la busqueda:\n1.Nombre\n2.Apodo\n3.Telefono")
        return input("==> ")

    def searchContactWithName(self,filtro,i):
        if i != 1:
            return input(f"Escriba el {filtro} del contacto a buscar:")
        else:
            return int(input(f"Escriba el {filtro} del contacto a buscar:"))

    def mostrarContactoEncontrado(self,contact):
        print("\n\t\t\U0001F464CONTACTO\U0001F464")
        print(f"NOMBRE: {contact.nombre}")
        print(f"APELLIDO:{contact.apellido}")
        print(f"APODO:{contact.apodo}")
        print(f"TELEFONO:{contact.telefono}")

    def mostrarContactoNoEncontrado(self, searchedContact, filtro):
        print(f"El contacto con el {filtro} ({searchedContact}) NO existe")

    def removeContact(self):
        return int(input("\nINGRESA EL NUMERO TELEFONICO DEL CONTACTO QUE DESEA ELIMINAR:"))

    def removeContactSuccessful(self,numContactRemove):
        print(f"\n\U00002705El contacto guardado con el numero telefonico({numContactRemove})fue ELIMINADO correctamente\U00002705")

    def removeContactFailed(self, numContactRemove):
        print(f"\n\U0001F44BEl numero telefonico {numContactRemove} NO coincide con el de ningun contacto guardado\U0001F44B")

    def showContactsMesagge(self):
        print("\n\t\t\U0000260E\U0000260ELISTA DE CONTACTOS\U0000260E\U0000260E\n")

    def showContacts(self,i,contact):
        print("\t\t   \U0001F464 CONTACTO", i, "\U0001F464")
        print(f"NOMBRE:{contact.nombre}")
        print(f"APELLIDO:{contact.apellido}")
        print(f"APODO:{contact.apodo}")
        print(f"TELEFONO:{contact.telefono}")
        print("________________________________")

    def uploadContacts(self):
        print("\n\t\t\U00002B06\U00002B06GUARDAR TUS CONTACTOS\U00002B06\U00002B06")
        print("¿En que formato deseas guardar tus contactos?")
        print("1.JSON")
        print("2.XML")
        return input("Introduce una opcion ==> ")

    def messageUploadCorrect(self):
        print("\t\t\U00002714\U00002714Los contactos se guardaron correctamente\U00002714\U00002714")

    def nameFile(self,type):
        return input(f"Ingrese el nombre del archivo con el que quiera que se {type} sus contactos:")

    def loadContacts(self):
        print("\n\t\t\U00002B07\U00002B07CARGAR TUS CONTACTOS\U00002B07\U00002B07")
        print("¿En que formato deseas cargar tus contactos?")
        print("1.JSON")
        print("2.XML")
        return input("Introduce una opcion ==> ")

    def messageLoadIncorrect(self,e):
        print("\t\t\U00002714\U00002714Los contactos NO se pudieron cargar\U00002714\U00002714")
        print(e)

    def pulseForContinue(self):
        input("\t\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")

    def error(self):
        print("\n\t\U0000274C\U0000274C\U0000274COPCION INCORRECTA\U0000274C\U0000274C\U0000274C\n\t    ¡Intenta de nuevo¡")
        input("\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3")

    def exit(self):
        print("\t\t\U0001F44B\U0001F44B\U0001F44B\U0001F44BHASTA LUEGO\U0001F44B\U0001F44B\U0001F44B\U0001F44B")