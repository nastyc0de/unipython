class Persona:
    def __init__(self, name, lastName, age) -> None:
        self._name = name 
        self._lastName = lastName
        self._age = age
    # ---------------------------------------------------------------------------- #
    #                             para el atributo name                            #
    # ---------------------------------------------------------------------------- #
    # -------------------------------- metodo get -------------------------------- #
    @property
    def name(self):
        return self._name
    # -------------------------------- metodo set -------------------------------- #
    @name.setter
    def setName(self, name):
        self._name = name
    # ---------------------------------------------------------------------------- #
    #                          para el atributo _lastName                          #
    # ---------------------------------------------------------------------------- #
    @property
    def lastName(self):
        return self._lastName
    @lastName.setter
    def setLastName(self, lastName):
        self._lastName = lastName
    # ---------------------------------------------------------------------------- #
    #                             para el atributo _age                            #
    # ---------------------------------------------------------------------------- #
    @property
    def age(self):
        return self._age
    @age.setter
    def setAge(self, age):
        self._age = age

    def showInfo(self):
        print(f"Persona: {self._name}, {self._lastName}, {self._age}")
# ---------------------------- crear una instancia --------------------------- #
if __name__ == '__main__':
    persona1 = Persona('Andres', "Pablo", 22)
    persona1.showInfo()

    persona1.setName = 'Andrew P'
    persona1.setLastName = 'RV'
    persona1.setAge = 21
    persona1.showInfo()
