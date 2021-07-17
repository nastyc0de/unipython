#  un set coleccion de elementos unicos y es mutable
# los elementos de un set deben de ser inmutables
# conjunto = {'Juan', True, 18.0}
# print(conjunto)

# # conjunto vacio
# conjunto = set()
# print(conjunto)
# # mutable
# conjunto.add('Andress')
# print(conjunto)
# # contiene valores unicos (NO SE REPITEN)
# conjunto.add('Andress')
# print(conjunto)
# # crear un set a partir de un iterable
# conjunto = set([4,5,7,9,4])
# print(conjunto)
# # podemos agregar mas elementos o incluso otro set
# conjunto2 = {100,200,100,300,400}
# conjunto.update(conjunto2)
# print(conjunto)
# # copiar un set (copia poco profunda, solo copia referencias)
# conjunto_copia = conjunto.copy()
# print(conjunto_copia)
# # verificar igualdad
# print(f'Son iguales en contenido? {conjunto == conjunto_copia}')
# print(f'Son iguales en referencia? {conjunto is conjunto_copia}')
# --------------------- operaciones de conjuntos con set --------------------- #
# personas con distintas caracteristicas
pelo_negro = {'Juan', 'Carlos', 'Luis','Ana', 'Rosa'}
pelo_rubio = {'Laura', 'Marco', 'Maria'}
ojos_cafes = {'Maria', 'Juan'}
menores_30 = {'Carlos', 'Ana','Rosa'}
# todos con ojos cafe y pelo rubio
print(ojos_cafes.union(pelo_rubio))
# invertir el orden con el mismo resultado (conmutacion)
print(pelo_rubio.union(ojos_cafes))
# (intersection) Solo personas cn ojos cafes y pelo rubio
print(ojos_cafes.intersection(pelo_rubio))

# difference Pelo negro sin ojos cafes
# las personas que se encuentran en el primer set pero no en el segundo
print(pelo_negro.difference(ojos_cafes))
# difference simmetric Pelo negro u ojos cafe, pero no ambos
print(pelo_negro.symmetric_difference(ojos_cafes))

# preguntar si un set esta contenido en otro(subset)
# revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# preguntar si un set set contiene a otro set (superset)
# revisar si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))


# preguntar si los de pelo negro no tienen pelo rubio (disjoint)
print(pelo_negro.isdisjoint(pelo_rubio))



