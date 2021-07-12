class Orden:
    contador = 0
    def __init__(self, computadoras):
        Orden.contador +=1
        self._id = Orden.contador
        self._computadoras = computadoras
    
    def addPC(self, computadora):
        self._computadoras.append(computadora)
    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        
        return f'''
            {self._id}
            {computadoras_str}
        '''