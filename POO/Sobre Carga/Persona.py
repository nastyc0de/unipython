class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __add__(self, other):
        return self.name + other.name
    
    def __sub__(self, other):
        return self.age - other.age

persona1 = Persona('Andres ', 28)
persona2 = Persona('Pablo', 40)
print(persona1 + persona2)
print(persona1 - persona2)

