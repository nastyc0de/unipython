# ---------------------------------------------------------------------------- #
#                               variable de clase                              #
# ---------------------------------------------------------------------------- #
class MiClase:
    variable_de_clase = 'Valor de variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    # ---------------------------- no recibe variables --------------------------- #
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_de_clase)
    # ----------------------- si recibe variables de clase ----------------------- #
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_de_clase)
    def metodo_de_instancia(self):
        self.metodo_clase
        self.metodo_estatico

# print(MiClase.variable_de_clase)
# clase1 = MiClase('valor')
# clase1.variable_instancia
# MiClase.metodo_estatico()
# MiClase.metodo_clase()

objeto1 = MiClase('variable de instancia')
objeto1.metodo_clase()