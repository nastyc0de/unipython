# los diccionarios guardan un orden (a diferencia de los set)
diccionario = {'Nombre': 'Juan', 'Apellido':'Perez', 'Edad':30}
print(diccionario)

# los diccionarios son mutables, pero las llaves (key) deben de ser inmutables
# diccionario = {[1,2]:'Valor1'}
# diccionario['Dpto'] = 'Sistemas'
# print(diccionario)

# # no hay valores duplicados, se reemplaza si existe
# diccionario['Nombre'] = 'Luis'
# print(diccionario)

# # recuperar un valorr indicando una llave
# print(diccionario['Nombre'])
# # sino encuentra el valor, lanza una excepcion
# print(diccionario['Nombre'])

# metodo get recupera un valor, y si no existe lanza una excepcion
# ademas podemos regresar un valor en caso que no exista.
print(diccionario.get('Nombres', 'No se encontro la llave'))

# setdefault si se modifica el diccionario, ademas agrega un valor por defecto
nombre = diccionario.setdefault('Nombre', 'Valor por defecto')
print(nombre)
print(diccionario)

nombre = diccionario.setdefault('Nombres', 'Valor por defecto')
print(nombre)
print(diccionario)

# imprimir pprint
from pprint import pprint as pp
pp(diccionario)
