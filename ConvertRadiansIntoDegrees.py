#Convert radians into degrees: Write a function in Python that accepts
#one numeric parameter. This parameter will be the measure of an angle in
#radians. The function should convert the radians into degrees and then
# return that value.

from math import pi
import msvcrt as m

def wait():
    m.getch()
    return None

while True:
    raw = input('Ingrese el valor en radianes: ')
    try:
        rad = float(raw)
        break
    except:
        print('Debe ingresar un valor numerico')

deg = rad*180/pi
deg = round(deg,2)

print('')
print('El valor ingresado es de', deg, '°')
print('')
print('Presione una tecla para terminar')
wait()
