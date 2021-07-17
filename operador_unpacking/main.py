# desempaquetar * para cualquier iterable excepto diccionarios.
nums = [1, 2, 3]
print(nums)
print(*nums)
print(*nums, sep=' - ')

# desempaquetando al momento de pasar un parametro a una funcion
def sumar(a, b, c):
    print(f'Suma:{a + b + c}')

sumar(*nums)
# extraer algunas partes de una lista
lista = [1, 2, 3, 4, 5, 6, 7]
a, *b, c, d = lista
print(a,b,c,d)
# unir listar
a = [1,2,3]
b = [4,5,6]
lista = [*a, *b]
print(f'la lista: {lista}')
# unir diccionarios
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5,'f':6}
dict3 = {**dict1, **dict2}
print(dict3)
# construir una lista a partir de un str
string = [*"is2 Thi1s T4est 3a"]
print(string)
print(*string, sep='')
