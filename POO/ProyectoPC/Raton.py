from DispositivosEntradas import DispositivoEntrada as DE

class Raton(DE):

    contador = 0
    
    def __init__(self, marca, tipo_entrada):
        Raton.contador += 1
        self._id = Raton.contador
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f'{self._id}, {self._marca}, {self._tipo_entrada}'


if __name__ == "__main__":
    raton1 = Raton('Razer', 'USB')
    raton2 = Raton('HP', 'USB')
    print(raton1)
    print(raton2)