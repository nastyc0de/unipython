from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(4,'rojo')
print(f'El area es: {cuadrado1.getArea()}')
print(cuadrado1)

rec1 = Rectangulo(3,8, 'verde')
print(f'El area es: {rec1.getArea()}')
print(rec1)