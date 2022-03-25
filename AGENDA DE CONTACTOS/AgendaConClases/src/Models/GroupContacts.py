
class group():
    def __init__(self, nombre, contacts):
        self.nameGroup = nombre
        self.members = contacts

    def UploadJson(self):
        telefonos = []
        for contact in self.members:
            telefonos.append(contact.telefono)
        return {"nombre del grupo": self.nameGroup, "miembros": telefonos}

    def UploadXml(self):
        groups = {"nombre del grupo": self.nameGroup}
        i = 0
        for contact in self.members:
            groups[f'miembro{i+1}'] = contact.telefono
            i += 1
        groups['numerosdemiembros'] = i
        return groups