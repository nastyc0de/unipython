from Gerente import Gerente
from Empleado import Empleado

def print_detail(object):
    print(object)
    print(type(object))
    if isinstance(object,Gerente):
        print(object.dpto)

empleado = Empleado('Andres', 6000)
print_detail(empleado)

gerente = Gerente('asa', 4000, 'sistemas')
print_detail(gerente)