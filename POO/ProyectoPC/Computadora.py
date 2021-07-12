from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
class Computadora:
    contador = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador += 1
        self._id = Computadora.contador
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    def __str__(self):
        return f'''
        {self._nombre}: {self._id}
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''
if __name__ =='__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'BLuetooth')
    monitor1 = Monitor('LG', 20)
    pc1 = Computadora('Dell',monitor1, teclado1, raton1)
    print(pc1)