from DispositivosEntradas import DispositivoEntrada as DE

class Teclado(DE):
    contador = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador += 1
        self._id = Teclado.contador
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f"{self._id}, {self._marca}, {self._tipo_entrada}"
if __name__ == "__main__":
    teclado1 = Teclado('Razer', 'Bluetooth')
    teclado2 = Teclado('Acer', 'Bluetooth')
    print(teclado1)
    print(teclado2)