# with open('prueba.txt', 'r') as datafile:
#     print(datafile.read())
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as file:
    print(file.read())