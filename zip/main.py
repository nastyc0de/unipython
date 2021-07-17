nums = (1,2,3,4,5,6)
letters = ['a', 'b', 'c', 'd', 'e']
conjunto = {2,5,7,1,8,3}
# print(conjunto)
lista = zip(nums, letters, conjunto)
# print(list(lista))
# print(tuple(zip(nums, letter)))

#usando el for
# new_list = []
# for num, letter, conj in zip(nums, letters, conjunto):
#     new_list.append(f'CI:{num}-{letter}-{conj}')
# print(new_list)

# creando un unzip
# numeros, letras, conjuntos = zip(*lista)
# print(numeros, letras, conjuntos)
# print(type(numeros))

# ordenando por letra
print(sorted(zip(letters, nums), reverse = True))
print(sorted(zip(nums, letters), reverse = True))

# crear un diccionario con zip y dos iterables
diccionario =dict(zip(nums, letters))
print(diccionario)

# actualizar un elemento de un diccionario
llave = [1]
valor = ['primer valor']
diccionario.update(zip(llave,valor))
print(diccionario)