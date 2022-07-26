#Duplicate letter checker:
#Create a function in Python that accepts one parameter: a string that’s a
#sentence. This function should return True if any word in that sentence
#contains duplicate letters and False if not.

import msvcrt as m

def wait():
    m.getch()
    return None

def LetraDuplicada(x):
    base = dict()
    palabras = frase.split(' ')
    for palabra in palabras:
        palabra.split()
        for letra in palabra:
            base[letra] = base.get(letra, 0) + 1

    duplicado = False
    for v in base.values():
        if v > 1:
            duplicado = True

    return duplicado


frase = input('Ingrese una frase: ')

resultado = LetraDuplicada(frase)

if resultado:
    print("Hay caracteres duplicados")
else:
    print("No hay caracteres duplicados")

print('\nPresione una tecla para terminar')
wait()
