from src.Models.contact import Contact


class View:
    def menu(self):
        print(
            "\033[1;36m"+"\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8"+'\033[0;m')
        print("\033[1;36m"+"\t  \U0000260E\U0000260E\U0000260E"+'\033[0;m'+"AGENDA DE CONTACTOS"+"\033[1;36m"+"\U0000260E\U0000260E\U0000260E"+'\033[0;m')
        print("\033[1;36m"+"\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8"+'\033[0;m')
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 1. CREAR UN CONTACTO")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 2. BUSCAR UN CONTACTO")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 3. ELIMINAR CONTACTO")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 4. LISTA DE CONTACTOS GUARDADOS")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 5. GUARDAR CONTACTOS")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 6. CARGAR CONTACTOS")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 7. SALIR")
        print("\033[1;36m"+"\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8"+'\033[0;m')
        return input("Introduce una opcion ==> ")

    def addContact(self):
        print("\033[1;36m"+"\n\t\t\U0000260E\U0000260EAGREGA UN CONTACTO\U0000260E\U0000260E"+'\033[0;m')
        nombre = input("NOMBRE:")
        apellido = input("APELLIDO:")
        apodo = input("APODO:")
        telefono = input("TELEFONO:")
        return Contact(nombre,apellido,apodo,telefono)

    def checkPhone(self):
        return input("Ingrese de nuevo el TELEFONO:")

    def noIsANumber(self):
        print("\033[1;31m"+"\U000026A0\U000026A0El N° de telefono debe ser un numero entero\U000026A0\U000026A0\n\t\t\U0001F449Intente de nuevo\U0001F448"+'\033[0;m')

    def contactSavedSuccessfully (self,name):
        print("\033[1;32m"+f"\n\U00002714El contacto con Nombre ({name}) se guardo Exitosamente\U00002714\n"+'\033[0;m')

    def contactExist(self,telefono):
        print("\033[1;31m"+f"¡¡¡El contacto con el numero [{telefono}] YA EXISTE¡¡¡"+'\033[0;m')

    def searchContactMesagge(self):
        print("\033[1;36m"+"\n\t\t\U0001F50E\U0001F50E\U0001F50E BUSCAR CONTACTO \U0001F50D\U0001F50D\U0001F50D"+'\033[0;m')

    def emptyContactList(self):
        print("_____________________________________________")
        print("  ""\033[1;31m"+"¡¡¡NO EXISTE NINGUN CONTACTO GUARDADO¡¡¡"+'\033[0;m')
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
        print("\033[1;36m"+"\n\t\t\U0001F464CONTACTO\U0001F464"+'\033[0;m')
        print(f"NOMBRE: {contact.nombre}")
        print(f"APELLIDO:{contact.apellido}")
        print(f"APODO:{contact.apodo}")
        print(f"TELEFONO:{contact.telefono}")

    def mostrarContactoNoEncontrado(self, searchedContact, filtro):
        print("\033[1;31m"+f"El contacto con el {filtro} ({searchedContact}) NO existe"+'\033[0;m')

    def removeContact(self):
        return int(input("\nINGRESA EL NUMERO TELEFONICO DEL CONTACTO QUE DESEA ELIMINAR:"))

    def removeContactSuccessful(self,numContactRemove):
        print("\033[1;32m"+f"\n\U00002705El contacto guardado con el numero telefonico ({numContactRemove}) fue ELIMINADO correctamente\U00002705"+'\033[0;m')

    def removeContactFailed(self, numContactRemove):
        print("\033[1;31m"+f"\n\U0001F44BEl numero telefonico {numContactRemove} NO coincide con el de ningun contacto guardado\U0001F44B"+'\033[0;m')

    def showContactsMesagge(self):
        print("\033[1;36m"+"\n\t\t\U0000260E\U0000260ELISTA DE CONTACTOS\U0000260E\U0000260E\n"+'\033[0;m')

    def showContacts(self,i,contact):
        print("\033[1;36m"+"\t\t   \U0001F464 CONTACTO", i, "\U0001F464"+'\033[0;m')
        print(f"NOMBRE:{contact.nombre}")
        print(f"APELLIDO:{contact.apellido}")
        print(f"APODO:{contact.apodo}")
        print(f"TELEFONO:{contact.telefono}")
        print("________________________________")

    def uploadContacts(self):
        print("\033[1;36m"+"\n\t\t\U00002B06\U00002B06GUARDAR TUS CONTACTOS\U00002B06\U00002B06"+'\033[0;m')
        print("¿En que formato deseas guardar tus contactos?")
        print("1.JSON")
        print("2.XML")
        return input("Introduce una opcion ==> ")

    def messageUploadCorrect(self):
        print("\033[1;32m"+"\t\t\U00002714\U00002714Los contactos se guardaron correctamente\U00002714\U00002714"+'\033[0;m')

    def nameFile(self,type):
        return input(f"Ingrese el nombre del archivo con el que quiera que se {type} sus contactos:")

    def loadContacts(self):
        print("\033[1;36m"+"\n\t\t\U00002B07\U00002B07CARGAR TUS CONTACTOS\U00002B07\U00002B07"+'\033[0;m')
        print("¿En que formato deseas cargar tus contactos?")
        print("1.JSON")
        print("2.XML")
        return input("Introduce una opcion ==> ")

    def messageLoadIncorrect(self, e):
        print("\033[1;31m"+"\t\t\U00002714\U00002714Los contactos NO se pudieron cargar\U00002714\U00002714"+'\033[0;m')
        print(e)

    def pulseForContinue(self):
        input("\033[1;34m"+"\U0001F5E3\U0001F5E3Pulsa cualquier tecla para continuar\U0001F5E3\U0001F5E3"+'\033[0;m')

    def error(self):
        print("\033[1;31m"+"\t\U0000274C\U0000274C\U0000274COPCION INCORRECTA\U0000274C\U0000274C\U0000274C\n\t    ¡Intenta de nuevo¡"+'\033[0;m')
        self.pulseForContinue()

    def exit(self):
        print("\033[1;36m"+"\t\t\U0001F44B\U0001F44B\U0001F44B\U0001F44BHASTA LUEGO\U0001F44B\U0001F44B\U0001F44B\U0001F44B"+'\033[0;m')