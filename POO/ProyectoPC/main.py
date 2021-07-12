from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'BLuetooth')
monitor1 = Monitor('LG', 20)
pc1 = Computadora('Dell',monitor1, teclado1, raton1)

teclado2 = Teclado('Razer', 'Bluetooth')
raton2 = Raton('Razer', 'Bluetooth')
monitor2 = Monitor('LG', 20)
pc2 = Computadora('MSI',monitor2, teclado2, raton2)


computadoras1 = [pc1, pc2]
orden1 = Orden(computadoras1)
print(orden1)