print('Introdusca numeros enteros en a,b y c.')

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

raiz1 = ((-b) + (((b ** 2) - (4*a*c))) ** 0.5) / (2*a)

raiz2 = ((-b) - (((b ** 2) - (4*a*c))) ** 0.5) / (2*a)

print('Raiz 1 es:',raiz1)
print('Raiz 2 es:',raiz2)