a = int(input('Cuanto le sobro en euro? '))
b = int(input('Cuanto le sobro en rublos? '))
c = int(input('Cunato le sobro en peso mexiano? '))

eur = a * 1.07
rub = b * 0.013
mxn = c * 0.054

res = eur + rub + mxn

print('resultado:',res)