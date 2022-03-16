from src.view.view import View
from src.Models.contact import Contact
import json
from dict2xml import dict2xml
import xml.etree.ElementTree
import xmltodict

class Agenda:
    def __init__(self):
        self.userOption = 0
        self.vista = View()
        self.Contacts = []

    def menu(self):
        while self.userOption != "7":
            self.userOption = self.vista.menu()
            if self.userOption == "1":
                self.addContact()
            elif self.userOption == "2":
                self.searchContact()
            elif self.userOption == "3":
                self.removeContact()
            elif self.userOption == "4":
                self.showContacts(1)
            elif self.userOption == "5":
                self.uploadContacts()
            elif self.userOption == "6":
                self.loadContacts()
            elif self.userOption == "7":
                break
            else:
                self.vista.error()
        self.vista.exit()

    def addContact(self):
        newContact = self.vista.addContact()
        verificarNum = self.check_tel(newContact.telefono)
        contactNew = Contact(newContact.nombre,newContact.apellido,newContact.apodo,verificarNum)
        if not self.Contacts:
            self.Contacts.append(contactNew)
            self.vista.contactSavedSuccessfully(contactNew.nombre)
            self.vista.pulseForContinue()
        else:
            for contact in self.Contacts:
                if contactNew.telefono == contact.telefono:
                    exitNumber = True
                    break
                else:
                    exitNumber = False
            if exitNumber:
                self.vista.contactExist(contactNew.telefono)
                self.vista.pulseForContinue()
            else:
                self.Contacts.append(contactNew)
                self.vista.contactSavedSuccessfully(contactNew.nombre)
                self.vista.pulseForContinue()

    def check_tel(self,telefono):
        type_num = True
        i = 1
        while type_num:
            if i == 1:
                user_num = telefono
            elif i == 2:
                user_num = self.vista.checkPhone()
            try:
                int(user_num)
                type_num = False
                return int(user_num)
            except ValueError:
                self.vista.noIsANumber()
                i = 2

    def searchContact(self):
        if not self.Contacts:
            self.vista.emptyContactList()
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
                    self.vista.mostrarContactoEncontrado(contact)
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
                    self.vista.mostrarContactoEncontrado(contact)
                self.vista.pulseForContinue()
        elif d == 3:
            for contact in self.Contacts:
                if searchedContact == contact.telefono:
                    self.vista.mostrarContactoEncontrado(contact)
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
            self.vista.emptyContactList()
            self.vista.pulseForContinue()
        else:
            self.showContacts(2)
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

    def showContacts(self, a):
        i = 0
        self.vista.showContactsMesagge()
        if not self.Contacts:
            self.vista.emptyContactList()
        else:
            contactsOrder = sorted(self.Contacts, key=lambda contact: contact.nombre)
            for contact in contactsOrder:
                i += 1
                self.vista.showContacts(i,contact)
        if a == 1:
            self.vista.pulseForContinue()
        else:
            pass

    def uploadContacts(self):
        if not self.Contacts:
            self.vista.emptyContactList()
            self.vista.pulseForContinue()
        else:
            typeUpload = ""
            while typeUpload != "1" or "2":
                typeUpload = self.vista.uploadContacts()
                if typeUpload == "1":
                    nameFile = self.vista.nameFile("guarden")
                    listUpload = []
                    for contact in self.Contacts:
                        listUpload.append(contact.Upload())
                    with open(f"data/{nameFile}.json", "w") as fp:
                        json.dump(listUpload, fp)

                    self.vista.messageUploadCorrect()
                    self.vista.pulseForContinue()
                    break
                elif typeUpload == "2":
                    nameFile = self.vista.nameFile("guarden")
                    listContacts = []
                    for contact in self.Contacts:
                        listContacts.append(contact.Upload())
                    numberOfContacts = len(listContacts)
                    with open(f"data/{nameFile}.xml", "w") as fp:
                        fp.write("<?xml version='1.0' encoding='utf-8'?>\n\n")
                        fp.write("<Contacts>\n")
                        for i in range(0, numberOfContacts):
                            fp.write(dict2xml(listContacts[i], wrap=f"Contacto{i+1}", indent="\t"))
                        fp.write("\n</Contacts>")
                    self.vista.messageUploadCorrect()
                    self.vista.pulseForContinue()
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
                    with open(f"data/{nameFile}.json", "r") as fp:
                        data = json.load(fp)

                    for contact in data:
                        self.Contacts.append(
                            Contact(
                                nombre=contact["nombre"],
                                apellido=contact["apellido"],
                                apodo=contact["apodo"],
                                telefono=contact["telefono"]
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
                    archive = f'data/{nameFile}.xml'
                    file = open(archive, "r")
                    xml_content = file.read()
                    my_ordered_dict = xmltodict.parse(xml_content)
                    list = dict(my_ordered_dict['Contacts'])
                    contacts = list.values()
                    for contact in contacts:
                        self.Contacts.append(
                            Contact(
                                nombre=contact["nombre"],
                                apellido=contact["apellido"],
                                apodo=contact["apodo"],
                                telefono=contact["telefono"]
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


def load_json(path: str) -> dict:
    if path.endswith(".json"):
        print(f"> Loading JSON from '{path}'")
        with open(path, mode="r") as open_file:
            content = open_file.read()

        return json.loads(content)
    elif path.endswith(".xml"):
        print(f"> Loading XML as JSON from '{path}'")
        Docxml = xml.etree.ElementTree.tostring(xml.etree.ElementTree.parse(path).getroot())
        return xmltodict.parse(Docxml, attr_prefix="@", cdata_key="#text", dict_constructor=dict)

    print(f"> Loading failed for '{path}'")
    return {}