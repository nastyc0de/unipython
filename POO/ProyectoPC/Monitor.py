class Monitor:
    contador = 0
    def __init__(self, marca, tamano):
        Monitor.contador += 1
        self._id = Monitor.contador
        self._marca = marca
        self._tamano = tamano
    
    def __str__(self):
        return f'{self._id}, {self._marca}, {self._tamano}'

if __name__ == '__main__':
    monitor1 = Monitor('Samsung', 15)
    monitor2 = Monitor('LG', 14)
    print(monitor1)
    print(monitor2)