#Convert a decimal to a hex:
#Write a function in Python to convert a decimal to a hex. It must accept a
#string of ASCII characters as input. The function should return the value of
#each character as a hexadecimal string.

import msvcrt as m

def wait():
    m.getch()
    return None

print('Traductor ASCII - Hexadecimal')

datos = open('tabla.dat', encoding="utf8")
tabla = dict()      #tabla de conversion
for lineas in datos:
    linea = lineas.rstrip()
    letras = linea.split("--")

    tabla[letras[4]] = letras[1]
datos.close()

#Debug
#for (k,v) in tabla.items():
#    print(k,v)
archivo = False
frase = input('\nIngrese una frase a covertir o presione Enter para leer desde archivo:\n')
if len(frase) < 1:
    entrada = open('Texto.txt', encoding="utf8")
    salida = open('Hexa.txt',mode="a")
    frase = entrada.read()
    archivo = True
fhexa = ''

for letras in frase:
    try:
        letra = tabla[letras]
    except:
        if letras == '\n':
            if archivo:
                salida.write('0D')
            else:
                fhexa = fhexa + '0D'
        else:
            print('Caracter no encontrado (', letras, ').' )
            if archivo:
                salida.write('*/Traduccion incompleta!')
                salida.write(letras)
                salida.write('/*')
        continue
    if archivo:
        salida.write(letra)
    else:
        fhexa = fhexa + letra

if archivo:
    print('\nSalida guardada en Hexa.txt:\n')
    entrada.close()
    salida.close()
else:
    print('\nFrase en Hexadecimal:\n')
    print(fhexa)

print('\nPresione cualquier tecla para salir')
wait()
