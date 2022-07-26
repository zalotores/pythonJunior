#Create a calculator function:
#Write a Python function that accepts three parameters.
# The 1st parameter is an integer.
# The 2nd mathematical operator.
# The 3rd also be an integer.
#The function should perform a calculation and return the results.

import msvcrt as m

def wait():
    m.getch()
    return None

print('-------------------------')
print('Calculadora basica.')
print('----------')

a = input('Ingrese el primer entero a operar: ')
op = input('Ingrese el operador( +, -, x, /): ')
b = input('Ingrese el segundo entero a operar: ')

valido = True       #comprueba que los datos esten correctos
try:
    a = int(a)
    op.lower()
    if not(op == '+' or op == '-' or op =='x' or op == '/'): valido = False
    b = int(b)
except:
    valido = False

if valido:
    if op == '+':
        c = a + b
    elif op == '-':
        c = a - b
    elif op == 'x':
        c = a * b
    else:
        c = a / b

    print('----------')
    print( a, op, b, '=', c)
    print('-------------------------')
else:
    print('----------')
    print('Datos invalidos, no se puede calcular.')
    print('-------------------------')

print('\nPresione cualquier tecla para salir')
wait()
