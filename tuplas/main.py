# declarar variable
a, b = 'Hola', 'Adios'
print(a, b)
# swap(intercambio)
a, b = b, a
print(a, b)
# regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1,4,7,22,75,11,77,2,8,9,0,21,34])
print(min, max)

# regresar la suma de una tupla
resultado = sum((1,4,7,1,3,8))
print(resultado)

def sumar(*args):
    return sum(args)

resultado = sumar(1,4,7,1,3,8,3,1,5,7,2,1)
print(resultado)
