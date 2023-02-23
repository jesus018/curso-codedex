intentos = 3
num_secre = 0

print('Adivine el numero del 1 al 10')

while num_secre != 6 and intentos != 0:
    print('Tiene', intentos,'intentos')
    num_secre = int(input('Adivine el numero: '))
    intentos = intentos - 1

if num_secre == 6:
    print('¡Felicitaciones!, lo ha adivinado')
elif intentos == 0:
    print('Has perdido')
else:
    print('error')