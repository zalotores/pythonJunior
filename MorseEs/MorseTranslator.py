#Morse code translator:
# Write a code in Python to create a Morse code translator. The string can also
# have any special characters as a part of the Morse code. The python code
#should return the Morse code that is equivalent to the string.

import msvcrt as m

def wait():
    m.getch()
    return None

print('Traductor Morse - Español')

tabla = dict()
fhandler = open('Codificador.txt', encoding="utf8")
print
for lineas in fhandler:
    linea = lineas.rstrip()
    letras = linea.split(" ")
    tabla[letras[0]] = letras[1]

fhandler.close()        #tabla de caracteres cargada

print('\nCargue los datos a traducir en el archivo Morse o Español.\n')
while True:
    op = input('Seleccione M para traducir a Morse o E para español: ')
    op= op.upper()
    if op == 'M':
        break
    elif op == 'E':
        break

if op == 'M':
    lector = open('Espanol.txt', encoding = "utf8")
    grabador = open('Morse.txt', mode="a")
    for lineas in lector:
        lineas = lineas.rstrip()
        palabras = lineas.split(' ')
        for palabra in palabras:
            palabra.split()
            for letra in palabra:
                letra = letra.upper()
                grabador.write(tabla[letra])
                grabador.write(" ")
            grabador.write("/")
        grabador.write('\n')

    grabador.close()
    lector.close()

    handlere = open('Espanol.txt', encoding = "utf8")
    entrada = handlere.read()
    print('\nTexto a traducir:\n')
    print(entrada)
    print('\n')
    handlers = open('Morse.txt', encoding = "utf8")
    salida = handlers.read()
    print('Texto traducido:\n')
    print(salida)
    handlere.close()
    handlers.close()
    print('Presione cualquier tecla para salir')
    wait()

else:
    lector = open('Morse.txt', encoding = "utf8")
    grabador = open('Espanol.txt', mode="a")
    for lineas in lector:
        lineas = lineas.rstrip()
        palabras = lineas.split('/')
        for palabra in palabras:
            letras = palabra.split(' ')
            for letra in letras:
                for (k,v) in tabla.items():
                    if v == letra:
                        grabador.write(k)
            grabador.write(" ")
        grabador.write('\n')

    grabador.close()
    lector.close()

    handlere = open('Morse.txt', encoding = "utf8")
    entrada = handlere.read()
    print('\nTexto a traducir:\n')
    print(entrada)
    print('\n')
    handlers = open('Espanol.txt', encoding = "utf8")
    salida = handlers.read()
    print('Texto traducido:\n')
    print(salida)
    handlere.close()
    handlers.close()
    print('Presione cualquier tecla para salir')
    wait()
