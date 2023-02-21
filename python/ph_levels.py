# == igual a
# != no igual a
# > mas que
# < menor que
# >= mayor o igual que
# <= menor igual que 


ph = int(input('INgrese el valor del ph (entre 0 y 14): '))

if ph > 7:
    print('Básico')
elif ph < 7:
    print('Äcido')
else:
    print('¡Neutral!')