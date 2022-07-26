#Convert a decimal number into binary:
#Write a function in Python that accepts a decimal number and returns the
#equivalent binary number. The decimal number will always be less than 1,024,
#so the binary number returned will always be less than ten digits long.
import msvcrt as m

def wait():
    m.getch()
    return None

def DecToBin(x):
    bin = ''
    while (x>0):
        if (x % 2 == 0):
            bin = '0' + bin
            x = x / 2
        else:
            bin = '1' + bin
            x = (x - 1) / 2
    binario = int(bin)
    return binario

while True:
    raw = input('Ingrese un numero en formato decimal: ')
    try:
        dec = int(raw)
        break
    except:
        continue

bin = bin(dec)
binario = DecToBin(dec)
print('Numero en formato binario(int):')
print(binario)
print('Numero en formato binario(str):')
print(bin)

print('\nPresione una tecla para terminar')
wait()
