#The IP address:
#Write a function to find the domain name from the IP address.
#The function will accept an IP address, and return the domain name that maps
#to that IP address while using records of PTR DNS.

import msvcrt as m

def wait():
    m.getch()
    return None

import socket

print('\nBuscador de dominios basado en IP.\n---------')
ipe = input('Ingrese la IP:')
if len(ipe) < 1:
    print('LocalHost')

web = socket.getfqdn(ipe)
print('---------\n')
if web == ipe:
    print('Dominio no encontrado')
else:
    print(web)

print('\nPresione cualquier tecla para salir')
wait()
