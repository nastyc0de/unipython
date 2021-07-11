class Producto:
    contador = 0
    def __init__(self, name, price):
        Producto.contador += 1
        self._id = Producto.contador
        self._name = name
        self._price = price
    @property
    def price(self):
        return self._price

    def __str__(self):
        return f'Id Producto: {self._id}, Nombre:{self._name}, Precio:{self._price}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 140.00)
    print(producto2)