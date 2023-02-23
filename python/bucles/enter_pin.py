print('BANCO DE CODEDEX')

pin = int(input('Ingrese su PIN: '))

while pin != 1234:
    pin = int(input('El PIN ingresado es incorrecto. Ingrese su PIN otra vez: '))

if pin == 1234:
    print('PIN aceptado!')