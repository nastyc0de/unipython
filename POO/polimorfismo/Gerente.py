from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, dpto):
        super().__init__(nombre, sueldo)
        self.dpto = dpto
    def __str__(self):
        return f'Gerente {self.dpto}, {super().__str__()}'