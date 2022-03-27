
class Contact:
    def __init__(self, nombre, apellido, apodo, telefono, email, birthday, numbers=''):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.email = email
        self.birthday = birthday
        self.Othernumber = numbers
        self.telefonosExtras = []

    def UploadJson(self):
        return {"nombre": self.nombre, "apellido": self.apellido, "apodo": self.apodo, "telefono": self.telefono, "email": self.email,"birthday": self.birthday, "otros numeros": self.Othernumber}

    def UploadXml(self):
        i = 0
        uploadXml = {"nombre": self.nombre, "apellido": self.apellido, "apodo": self.apodo, "telefono": self.telefono,
                     "email": self.email, "birthdayDay": self.birthday[0], "birthdayMonth": self.birthday[1]}

        for numeros in self.Othernumber:
            uploadXml[f'numeroextra{i+1}'] = numeros
            i += 1
        uploadXml['numerosextras'] = i
        return uploadXml

    def otrosTelefonos(self, newTelefono):
        add = self.comparePhone(newTelefono)
        if add:
            self.telefonosExtras.append(newTelefono)
            return newTelefono
        else:
            print("No fue posible agregarlo")

    def comparePhone(self,phone):
        if str(phone) == self.telefono:
            print("\033[1;31m" + "ESTAS REPITIENDO EL NUMERO" + '\033[0;m')
            return False
        elif phone in self.telefonosExtras:
            print("\033[1;31m"+"ESTAS REPITIENDO EL NUMERO"+'\033[0;m')
            return False
        else:
            return True
