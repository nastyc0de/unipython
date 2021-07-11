class Persona:
    def __init__(self, name, lastName, age) -> None:
        self.name = name
        self.lastName = lastName
        self.age = age

    def show_info(self):
        print(f""" 
            Persona:
                    {self.name}
                    {self.lastName}
                    {self.age}
            """)
persona1 = Persona('Andres', "Pablo", 22)
print(persona1.name)

persona1.show_info()