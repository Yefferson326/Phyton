from src.view.view import View
from src.Models.contact import Contact
from src.Models.GroupContacts import group
import json
from dict2xml import dict2xml
import xmltodict
from datetime import datetime


class Agenda:
    def __init__(self):
        self.userOption = 0
        self.vista = View()
        self.Contacts = []
        self.Groups = []
        self.date = datetime.now()

    def menu(self):
        while self.userOption != "8":
            checkBirthday = self.checkDateBirthday()
            self.userOption = self.vista.menu(self.date, checkBirthday)
            if self.userOption == "1":
                self.addContact()
            elif self.userOption == "2":
                self.searchContact()
            elif self.userOption == "3":
                self.removeContact()
            elif self.userOption == "4":
                self.createGroup()
            elif self.userOption == "5":
                self.showContacts(1,0)
            elif self.userOption == "6":
                self.uploadContacts(0)
            elif self.userOption == "7":
                self.loadContacts()
            elif self.userOption == "8":
                self.copySecurity()
                break
            else:
                self.vista.error()
        self.vista.exit()

    def addContact(self):
        newContact = self.vista.addContact()
        verifyNum = self.check_tel(newContact.telefono)
        verifyEmail = self.checkEmail(newContact.email)
        numbersNew = []
        moreNumber = True
        while moreNumber:
            otherNumbers = self.vista.addOtherNumber()
            try:
                if otherNumbers == "1":
                    otherNumber = self.vista.addNewNumber(newContact.nombre)
                    verifyNewNum = self.check_tel(otherNumber)
                    checkNum = newContact.otrosTelefonos(verifyNewNum)
                    if checkNum is not None:
                        numbersNew.append(checkNum)
                elif otherNumbers == "2":
                    moreNumber = False
            except ValueError:
                self.vista.error()
        contactNew = Contact(newContact.nombre, newContact.apellido, newContact.apodo, verifyNum, verifyEmail, newContact.birthday, numbers=numbersNew)
        if not self.Contacts:
            self.Contacts.append(contactNew)
            self.vista.contactSavedSuccessfully(contactNew.nombre)
            self.vista.pulseForContinue()
        else:
            exitNumber = False
            for contact in self.Contacts:
                if contactNew.telefono == contact.telefono or contactNew.email == contact.email:
                    exitNumber = True
                    break
                else:
                    for otherNumOfContact in contact.Othernumber:
                        if contactNew.telefono == otherNumOfContact:
                            exitNumber = True
                            break
                    else:
                        continue
                    break
            print(exitNumber)
            if exitNumber:
                self.vista.contactExist(contactNew.telefono,contactNew.email)
                self.vista.pulseForContinue()
            else:
                self.Contacts.append(contactNew)
                self.vista.contactSavedSuccessfully(contactNew.nombre)
                self.vista.pulseForContinue()

    def check_tel(self, telefono):
        type_num = True
        while type_num:
            try:
                phone = int(telefono)
                numCorrect = self.correctTelefono(phone)
                num = int(numCorrect)
                return num
            except ValueError:
                self.vista.noIsANumber()
                telefono = self.vista.checkPhone()

    def correctTelefono(self, num):
        noPhone = True
        while noPhone:
            if len(str(num)) == 10 and str(num)[0] == "3":
                noPhone = False
            else:
                num = self.vista.phone()
        return num

    def checkEmail(self, email):
        valid_email = False
        valid_at_sing = 0
        valid_point = 0
        Exit = True
        while Exit:
            for n in email:
                if n == '@':
                    valid_at_sing += 1
                    valid_email = True
                elif n == '.':
                    valid_point += 1
                elif valid_at_sing != 1 and valid_point < 1:
                    valid_email = False

            if valid_email:
                Exit = False
            else:
                email = self.vista.messageIncorrectEmail()
        return email

    def checkDateBirthday(self):
        if not self.Contacts:
            return None
        else:
            contactsBirthday = []
            for contact in self.Contacts:
                if str(contact.birthday[0]) == f"{format(self.date.day)}" and str(contact.birthday[1]) == f"{format(self.date.month)}":
                    contactsBirthday.append(contact)
            return contactsBirthday

    def searchContact(self):
        if not self.Contacts:
            self.vista.emptyContactList("CONTACTO")
            self.vista.pulseForContinue()
        else:
            d = ""
            while d != ("1", "2", "3"):
                d = self.vista.searchContact()
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
                    self.vista.error()


    def searchContactWithName(self):
        searched_name = self.vista.searchContactWithName("NOMBRE",3)
        self.checkcontact(searched_name,1)


    def searchContactWithNickname(self):
        searched_nickname = self.vista.searchContactWithName("APODO",2)
        self.checkcontact(searched_nickname, 2)

    def searchContactWithPhone(self):
        searched_phone = self.vista.searchContactWithName("TELEFONO",1)
        self.checkcontact(searched_phone, 3)

    def checkcontact(self,searchedContact, d):
        if d == 1:
            result = []
            for contact in self.Contacts:
                if contact.nombre == searchedContact:
                    result.append(contact)
            if not result:
                self.vista.mostrarContactoNoEncontrado(searchedContact, "NOMBRE")
                self.vista.pulseForContinue()
            else:
                for contact in result:
                    self.vista.showContacts(contact)
                self.vista.pulseForContinue()
        elif d == 2:
            result = []
            for contact in self.Contacts:
                if contact.apodo == searchedContact:
                    result.append(contact)
            if not result:
                self.vista.mostrarContactoNoEncontrado(searchedContact, "APODO")
                self.vista.pulseForContinue()
            else:
                for contact in result:
                    self.vista.showContacts(contact)
                self.vista.pulseForContinue()
        elif d == 3:
            for contact in self.Contacts:
                if searchedContact == contact.telefono:
                    self.vista.showContacts(contact)
                    self.vista.pulseForContinue()
                    noFoundContact = False
                    break
                else:
                    noFoundContact = True
            if noFoundContact:
                self.vista.mostrarContactoNoEncontrado(searchedContact, "TELEFONO")
                self.vista.pulseForContinue()

    def removeContact(self):
        if not self.Contacts:
            self.vista.emptyContactList("CONTACTO")
            self.vista.pulseForContinue()
        else:
            self.showContacts(2, 1)
            numContactRemove = self.vista.removeContact()
            for contact in self.Contacts:
                if numContactRemove == contact.telefono:
                    numberFound = True
                    numContact = self.Contacts.index(contact)
                    break
                else:
                    numberFound = False
            if numberFound:
                self.Contacts.pop(numContact)
                self.vista.removeContactSuccessful(numContactRemove)
                self.vista.pulseForContinue()
            else:
                self.vista.removeContactFailed(numContactRemove)
                self.vista.pulseForContinue()

    def createGroup(self):
        continuar = True
        contactsGroup = []
        if not self.Contacts:
            self.vista.emptyContactList("CONTACTO")
            self.vista.pulseForContinue()
        else:
            name = self.vista.createGroup()
            nameGroup = self.checkGroup(name)
            while continuar:
                contactAddGroup = self.vista.integrantsGroup()
                numContact = self.check_tel(contactAddGroup)
                noFound = 0
                for contact in self.Contacts:
                    if int(contact.telefono) == numContact:
                        contactsGroup.append(contact)
                        break
                    else:
                        noFound += 1
                if noFound == len(self.Contacts):
                    self.vista.mostrarContactoNoEncontrado(numContact, "Telefono")
                addMoreContact = self.vista.addOtherIntegrant()
                if addMoreContact == 2:
                    break
            if not contactsGroup:
                self.vista.noCreateGroup()
            else:
                self.vista.createGroupCorrect(nameGroup)
                self.Groups.append(group(nameGroup, contactsGroup))
            self.vista.pulseForContinue()

    def checkGroup(self, nameNewGroup):
        if not self.Groups:
            return nameNewGroup
        else:
            for group in self.Groups:
                if group.nameGroup == nameNewGroup:
                    self.vista.groupExist(nameNewGroup)
                else:
                    return nameNewGroup

    def showContacts(self, a, b):
        show = 0
        if a != 2:
            show = self.vista.showContactsMesagge()
        i = 0
        if show == 1 or b == 1:
            if not self.Contacts:
                if b == 1:
                    self.vista.removeContact()
                self.vista.emptyContactList("CONTACTO")
            else:
                if b == 1:
                    self.vista.removeContactTitle()
                contactsOrder = sorted(self.Contacts, key=lambda contact: contact.nombre)
                for contact in contactsOrder:
                    i += 1
                    self.vista.showContacts(contact,i)

            if a == 1:
                self.vista.pulseForContinue()
        elif show == 2:
            if not self.Groups:
                self.vista.emptyContactList("GRUPO")
                self.vista.pulseForContinue()
            else:
                groupsOrder = sorted(self.Groups, key=lambda group: group.nameGroup)
                for Group in groupsOrder:
                    self.vista.showGroup(Group)
                self.vista.pulseForContinue()

        else:
            self.vista.error()

    def uploadContacts(self, securityActive):
        if not self.Contacts:
            self.vista.emptyContactList("CONTACTO")
            self.vista.pulseForContinue()
        else:
            typeUpload = ""
            while typeUpload != "1" or "2":
                if securityActive == 1:
                    typeUpload = self.vista.uploadContacts(1)
                else:
                    typeUpload = self.vista.uploadContacts(0)
                if typeUpload == "1":
                    nameFile = self.vista.nameFile("guarden")
                    listContactsUpload = []
                    listGroupsUpload = []
                    for contact in self.Contacts:
                        listContactsUpload.append(contact.UploadJson())
                    if self.Groups:
                        for groupSaved in self.Groups:
                            listGroupsUpload.append(groupSaved.UploadJson())

                    with open(f"data/{nameFile}_contactos.json", "w") as fp:
                        json.dump(listContactsUpload, fp)
                    with open(f"data/{nameFile}_grupos.json", "w") as fp:
                        json.dump(listGroupsUpload, fp)

                    self.vista.messageUploadCorrect()
                    self.vista.pulseForContinue()
                    break
                elif typeUpload == "2":
                    nameFile = self.vista.nameFile("guarden")
                    listContactsUpload = []
                    listGroupsUpload = []
                    for contact in self.Contacts:
                        print(contact.UploadXml())
                        listContactsUpload.append(contact.UploadXml())
                    if self.Groups:
                        for groupSaved in self.Groups:
                            listGroupsUpload.append(groupSaved.UploadXml())
                    numberOfContacts = len(listContactsUpload)
                    numberOfGroups = len(listGroupsUpload)
                    with open(f"data/{nameFile}.xml", "w") as fp:
                        fp.write("<?xml version='1.0' encoding='utf-8'?>\n\n")
                        fp.write("<Agenda>\n")
                        fp.write("<Contacts>\n")
                        for i in range(0, numberOfContacts):
                            fp.write(dict2xml(listContactsUpload[i], wrap=f"Contacto{i+1}", indent="\t"))
                        fp.write("\n</Contacts>")
                        fp.write("<Groups>\n")
                        for i in range(0, numberOfGroups):
                            fp.write(dict2xml(listGroupsUpload[i], wrap=f"Grupo{i + 1}", indent="\t"))
                        fp.write("\n</Groups>")
                        fp.write("\n</Agenda>")
                    self.vista.messageUploadCorrect()
                    self.vista.pulseForContinue()
                    break
                elif typeUpload == "3":
                    break
                else:
                    self.vista.error()

    def loadContacts(self):
        typeUpload = ""
        while typeUpload != "1" or "2":
            typeLoad = self.vista.loadContacts()
            if typeLoad == "1":
                nameFile = self.vista.nameFile("carguen")
                try:
                    with open(f"data/{nameFile}_contactos.json", "r") as fp:
                        dataContacts = json.load(fp)
                    with open(f"data/{nameFile}_grupos.json", "r") as fp:
                        dataGroups = json.load(fp)
                    for contact in dataContacts:
                        if not self.existPhone(contact["telefono"]):
                            self.Contacts.append(Contact(
                                    nombre=contact["nombre"],
                                    apellido=contact["apellido"],
                                    apodo=contact["apodo"],
                                    telefono=contact["telefono"],
                                    email=contact["email"],
                                    birthday=contact["birthday"],
                                    numbers=contact["otros numeros"]
                                )
                            )
                    for Group in dataGroups:
                        if not self.existGroup(Group["nombre del grupo"]):
                            members = []
                            for i in range(0, len(Group["miembros"])):
                                for contact in self.Contacts:
                                    if Group["miembros"][i] == contact.telefono:
                                        members.append(contact)
                                        break
                            self.Groups.append(group(
                                nombre=Group["nombre del grupo"],
                                contacts=members
                                )
                                )
                    self.vista.messageUploadCorrect()
                    self.vista.pulseForContinue()
                    break
                except Exception as e:
                    self.vista.messageLoadIncorrect(e)
                    self.vista.pulseForContinue()
                    break
            elif typeLoad == "2":
                nameFile = self.vista.nameFile("carguen")
                try:
                    Groups = []
                    archive = f'data/{nameFile}.xml'
                    file = open(archive, "r")
                    xml_content = file.read()
                    my_ordered_dict = xmltodict.parse(xml_content)
                    listContacts = dict(my_ordered_dict['Agenda']['Contacts'])
                    listGroupsXml = my_ordered_dict['Agenda']['Groups']
                    if listGroupsXml is not None:
                        listGroups = dict(listGroupsXml)
                        Groups = listGroups.values()
                    contacts = listContacts.values()
                    for contact in contacts:
                        if not self.existPhone(int(contact["telefono"])):
                            telefonosExtra = []
                            for i in range(0, int(contact["numerosextras"])):
                                telefonosExtra.append(contact[f"numeroextra{i+1}"])
                            self.Contacts.append(Contact(
                                nombre=contact["nombre"],
                                apellido=contact["apellido"],
                                apodo=contact["apodo"],
                                telefono=contact["telefono"],
                                email=contact["email"],
                                birthday=[contact["birthdayDay"], contact["birthdayMonth"]],
                                numbers=telefonosExtra
                                )
                            )
                    for Group in Groups:
                        if not self.existGroup(Group["nombre_del_grupo"]):
                            members = []
                            for i in range(0, int(Group["numerosdemiembros"])):
                                for contact in self.Contacts:
                                    if Group[f"miembro{i+1}"] == contact.telefono:
                                        members.append(contact)
                                        break
                            self.Groups.append(group(
                                nombre=Group["nombre_del_grupo"],
                                contacts=members
                            )
                            )
                    self.vista.messageUploadCorrect()
                    self.vista.pulseForContinue()
                    break
                except Exception as e:
                    self.vista.messageLoadIncorrect(e)
                    self.vista.pulseForContinue()
                    break
            else:
                self.vista.error()

    def existGroup(self,name):
        result = False
        for Group in self.Groups:
            if Group.nameGroup == name:
                result = True
                break
        return result

    def existPhone(self, number):
        result = False
        for contactSaved in self.Contacts:
            if contactSaved.telefono == number:
                result = True
                break
        return result

    def copySecurity(self):
        self.vista.copySecurity()
        self.uploadContacts(1)

