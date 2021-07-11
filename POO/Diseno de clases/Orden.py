from Producto import Producto

class Orden:
    contador = 0

    def __init__(self, productos):
        Orden.contador += 1
        self._id = Orden.contador
        self._productos = list(productos)
    
    def addProduct(self, producto):
        self._productos.append(producto)
    
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.price
        return total
    def __str__(self):
        producto_str = ''
        for producto in self._productos:
            producto_str += producto.__str__() + '|'
        
        return f"Orden: {self._id},  \nProductos:{producto_str}"

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 140.00)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)