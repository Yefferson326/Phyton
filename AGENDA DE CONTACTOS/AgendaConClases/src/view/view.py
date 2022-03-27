from src.Models.contact import Contact


class View:
    def menu(self, date, contactBirthday):
        print("\033[1;36m"+"\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8"+'\033[0;m')
        print("\033[1;36m"+"\t  \U0000260E\U0000260E\U0000260E"+'\033[0;m'+"AGENDA DE CONTACTOS"+"\033[1;36m"+"\U0000260E\U0000260E\U0000260E"+'\033[0;m')
        print("\033[1;36m"+f"\t\t\t \U0001F4C5 {format(date.day)}/{format(date.month)}/{format(date.year)} \U0001F4C5"+'\033[0;m')
        print("\033[1;36m"+"\t\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8"+'\033[0;m')
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 1. CREAR UN CONTACTO")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 2. BUSCAR UN CONTACTO")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 3. ELIMINAR CONTACTO")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 4. CREAR GRUPO")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 5. LISTA DE CONTACTOS GUARDADOS")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 6. GUARDAR CONTACTOS")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 7. CARGAR CONTACTOS")
        print("\033[1;36m"+"\U0001F4D8"+'\033[0;m'+" 8. SALIR")
        print("\033[1;36m"+"\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8"+'\033[0;m')
        if contactBirthday is not None:
            print("\033[1;36m" + "RECORDATORIO:" + '\033[0;m', end=" ")
            if not contactBirthday:
                print("Hoy no cumple años nadie")
            else:
                for contact in contactBirthday:
                    print("El contacto guardado con el nombre "+"\033[1;36m"+f"{contact.nombre}"+'\033[0;m'+" esta cumpliendo años hoy")
            print("\033[1;36m" + "\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8" + '\033[0;m')
        else:
            print("\033[1;36m" + "RECORDATORIO: No hay ningun contacto guardado, por favor cargue los contactos" + '\033[0;m', end=" ")
            print("\033[1;36m" + "\n\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8\U0001F4D8" + '\033[0;m')
        return input("Introduce una opcion ==> ")

    def addContact(self):
        print("\033[1;36m"+"\n\t\t\U0000260E\U0000260EAGREGA UN CONTACTO\U0000260E\U0000260E"+'\033[0;m')
        nombre = input("NOMBRE:")
        apellido = input("APELLIDO:")
        apodo = input("APODO:")
        telefono = input("TELEFONO:")
        Email = input("Correo Electronico:")
        birtday = self.birthday()
        return Contact(nombre,apellido,apodo,telefono,Email,birthday=birtday)

    def birthday(self):
        while True:
            print("Introduce la fecha de cumpleaños:")
            day = int(input("DIA:"))
            month = int(input("MES(número):"))
            if day in range(0, 32) and month in range(0,13):
                return [day, month]
                exit
            else:
                self.error()

    def adviceNotLoadContact(self):
        print("\033[1;31m"+"NO TIENES NINGUN CONTACTO GUARDADO\n"+'\033'+"\033[1;36m"+"Carga una lista de contactos o crea un nuevo contacto, para notificarte ¿quien esta cimpliendo años hoy?"+'\033')

    def checkPhone(self):
        return input("Ingrese de nuevo el TELEFONO:")

    def phone(self):
        return input("\033[1;31m"+"¡¡El numero ingresado no es un numero celular (debe contener por lo menos 10 numeros)!!\n"+'\033[0;m'+" Ejemplo: 3** *** ****\nIntente de nuevo:")

    def messageIncorrectEmail(self):
        return str(input("\033[1;31m"+"\t   ¡¡Email invalido!!\n\t\U000026A0Por favor ingreselo de nuevo\U000026A0"+'\033[0;m'+"\n==>"))

    def noIsANumber(self):
        print("\033[1;31m"+"\U000026A0\U000026A0El N° de telefono debe ser un numero entero\U000026A0\U000026A0\n\t\t\U0001F449Intente de nuevo\U0001F448"+'\033[0;m')

    def contactSavedSuccessfully (self,name):
        print("\033[1;32m"+f"\n\U00002714El contacto con Nombre ({name}) se guardo Exitosamente\U00002714\n"+'\033[0;m')

    def contactExist(self,telefono,email):
        print("\033[1;31m"+f"¡¡¡Verifica que el numero de telefono {telefono} o la direccion de correo {email} no sean de otro contacto ya guardado¡¡¡"+'\033[0;m')

    def removeContactTitle(self):
        print("\033[1;36m"+"\n\t\t\U0000274C\U0000274CELIMINAR CONTACTOS\U0000274C\U0000274C"+'\033[0;m')
        print("Contactos Guardados:")

    def addOtherNumber(self):
        print("¿Desea vincular otro numero de telefono para este contacto?")
        return input("1. SI\n2. NO\n==>")

    def addNewNumber(self, nombre):
        return input(f"Ingrese el nuevo numero que quiere asociar con el contacto de nombre {nombre}: ")

    def repeatNumber(self):
        print("\033[1;31m"+"ESTAS REPITIENDO EL NUMERO"+'\033[0;m')

    def emptyContactList(self, search):
        print("_____________________________________________")
        print("  ""\033[1;31m"+f"¡¡¡NO EXISTE NINGUN {search} GUARDADO¡¡¡"+'\033[0;m')
        print("_____________________________________________")

    def searchContact(self):
        print("\033[1;36m" + "\n\t\t\U0001F50E\U0001F50E\U0001F50E BUSCAR CONTACTO \U0001F50D\U0001F50D\U0001F50D" + '\033[0;m')
        print("Seleccione el filtro con el cual desea realizar la busqueda:\n1.Nombre\n2.Apodo\n3.Telefono")
        return input("==> ")

    def searchContactWithName(self,filtro,i):
        if i != 1:
            return input(f"Escriba el {filtro} del contacto a buscar:")
        else:
            return int(input(f"Escriba el {filtro} del contacto a buscar:"))

    def createGroup(self):
        print("\033[1;36m"+"\n\t\t\U0001F465CREAR GRUPO\U0001F465"+'\033[0;m')
        nameGroup = input("Ingrese el nombre del grupo:")
        return nameGroup

    def groupExist(self, name):
        print("\033[1;31m"+f"¡¡¡El grupo con el nombre [{name}] YA EXISTE¡¡¡"+'\033[0;m')

    def emailExist(self, email):
        print("\033[1;31m"+f"¡¡¡El email [{email}] YA esta asociado con otro contacto¡¡¡"+'\033[0;m')

    def integrantsGroup(self):
        try:
            return int(input("Ingrese el numero de telefono(Principal) del contacto que desea agregar:"))
        except ValueError:
            self.noIsANumber()
            self.pulseForContinue()

    def addOtherIntegrant(self):
        print("¿DESEA AGREGAR OTRO CONTACTO AL GRUPO?")
        return int(input("1.SI\n2.NO\n==>"))

    def noCreateGroup(self):
        print("\033[1;31m"+"NO FUE POSIBLE CREAR EL GRUPO"+'\033[0;m')

    def createGroupCorrect(self, nombre):
        print("\033[1;32m"+f"\n\U00002714El grupo con el nombre {nombre} fue creado correctamente\U00002714\n"+'\033[0;m')

    def mostrarContactoNoEncontrado(self, searchedContact, filtro):
        print("\033[1;31m"+f"El contacto con el {filtro} ({searchedContact}) NO existe"+'\033[0;m')

    def removeContact(self):
        return int(input("\nINGRESA EL NUMERO TELEFONICO (principal) DEL CONTACTO QUE DESEA ELIMINAR:"))

    def removeContactSuccessful(self,numContactRemove):
        print("\033[1;32m"+f"\n\U00002705El contacto guardado con el numero telefonico ({numContactRemove}) fue ELIMINADO correctamente\U00002705"+'\033[0;m')

    def removeContactFailed(self, numContactRemove):
        print("\033[1;31m"+f"\n\U0001F44BEl numero telefonico {numContactRemove} NO coincide con el de ningun contacto guardado\U0001F44B"+'\033[0;m')

    def showContactsMesagge(self):
        print("\033[1;36m"+"\n\t\t\U0000260E\U0000260ELISTA DE CONTACTOS\U0000260E\U0000260E"+'\033[0;m')
        return int(input("¿Que deseas ver?\n1. Contactos\n2. Grupos\n==>"))

    def showContacts(self, contact, i=''):
        print("\033[1;36m" + "\t\t   \U0001F464 CONTACTO", i, "\U0001F464" + '\033[0;m')
        print(f"NOMBRE:{contact.nombre}")
        print(f"APELLIDO:{contact.apellido}")
        print(f"APODO:{contact.apodo}")
        print(f"TELEFONO(Principal):{contact.telefono}")
        print(f"CORREO ELECTRONICO:{contact.email}")
        print("OTROS TELEFONOS:")
        if not contact.Othernumber or contact.Othernumber == [None]:
            print("\033[1;31m" + "NO TIENE MAS NUMEROS DE TELEFONO ASOCIADOS" + '\033[0;m')
        else:
            for numbers in contact.Othernumber:
                print("\t->",numbers)
        print("________________________________")

    def showGroup(self, group):
        print("\033[1;36m" + f"\t\t   \U0001F465 GRUPO ({group.nameGroup})", "\U0001F465" + '\033[0;m')
        print("Los integrantes de este grupo son")
        print("____________________________________")
        i = 0
        for contact in group.members:
            i += 1
            self.showContacts(contact,i)

    def uploadContacts(self, a):
        if a != 1:
            print("\033[1;36m"+"\n\t\t\U00002B06\U00002B06GUARDAR TUS CONTACTOS\U00002B06\U00002B06"+'\033[0;m')
        print("¿En que formato deseas guardar tus contactos?")
        print("1.JSON")
        print("2.XML")
        if a == 1:
            print("3.Salir sin guardar")
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

    def copySecurity(self):
        print("\033[1;36m"+"\t\t\U0001F4BE COPIA DE SEGURIDAD AUTOMATICA \U0001F4BE"+'\033[0;m')

    def exit(self):
        print("\033[1;36m"+"\t\t\U0001F44B\U0001F44B\U0001F44B\U0001F44BHASTA LUEGO\U0001F44B\U0001F44B\U0001F44B\U0001F44B"+'\033[0;m')