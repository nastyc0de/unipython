from logger_base import log

class Persona:
    def __init__(self, id = None, name = None, lastName = None, email = None):
        self._id = id
        self._name = name
        self._lastName = lastName
        self._email = email
    def __str__(self) -> str:
        return f'''
            id: {self.id}
            nombre: {self.name}
            last Name: {self.lastName}
            email: {self.email}
        '''
    # getter y setter para id
    @property
    def id(self):
        return self._id
    @id.setter
    def idSet(self, id):
        self._id = id
    
    # getter y setter para name
    @property
    def name(self):
        return self._name
    @name.setter
    def nameSet(self, name):
        self._name = name

    # getter y setter para lastName
    @property
    def lastName(self):
        return self._lastName
    @lastName.setter
    def lastNameSet(self, lastName):
        self._lastName = lastName

    # getter y setter para email
    @property
    def email(self):
        return self._email
    @email.setter
    def emailSet(self, email):
        self._email = email
    
if __name__ =='__main__':
    persona1 = Persona(1, 'JUan', 'asv', 'Jasv@mail.com')
    log.debug(persona1)
    # simular un insertar
    persona1 = Persona(id=1, name='JUan', lastName='asv')
    log.debug(persona1)
    # simular un delete
    persona1 = Persona(id=1)
    log.debug(persona1)