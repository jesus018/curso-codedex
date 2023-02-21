
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
res1 = 0
res2 = 0
res3 = 0

print('Responda las preguntas y se le asignara a la casa que petenecera segun el resultado')
print('Pregunta #1: ¿Te gusta el Amanecer o el Atardecer?')

print('1) Amanecer')
print('2) Atardecer')

res1 = int(input('Respuesta: '))

if res1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif res1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Entrada incorrecta')

print('puntos hasta ahora:')
print('Gryffindor', Gryffindor)
print('Ravenclaw', Ravenclaw)
print('Hufflepuff', Hufflepuff)
print('Slytherin', Slytherin)

print('Pregunta #2: Cuando muera, quiero que la gente me recuerde como')

print('1) El Bueno')
print('2) El Grande')
print('3) El Sabio')
print('4) El Audaz')

res2 = int(input('Respuesta: '))

if res2 == 1:
    Hufflepuff = Hufflepuff + 1
elif res2 == 2:
    Slytherin = Slytherin + 1
elif res2 == 3:
    Ravenclaw = Ravenclaw + 1
elif res2 == 4:
    Gryffindor = Gryffindor + 1
else:
    print('Entrada incorrecta')

print('puntos hasta ahora:')
print('Gryffindor', Gryffindor)
print('Ravenclaw', Ravenclaw)
print('Hufflepuff', Hufflepuff)
print('Slytherin', Slytherin)

print('Pregunta #3: ¿Qué tipo de instrumento agrada más al oído?')

print('1) El viólin')
print('2) La trompeta')
print('3) El piano')
print('4) El tambor')

res3 = int(input('Respuesta: '))

if res3 == 2:
    Hufflepuff = Hufflepuff + 1
elif res3 == 1:
    Slytherin = Slytherin + 1
elif res3 == 3:
    Ravenclaw = Ravenclaw + 1
elif res3 == 4:
    Gryffindor = Gryffindor + 1
else:
    print('Entrada incorrecta')

print('puntos hasta ahora:')
print('Gryffindor', Gryffindor)
print('Ravenclaw', Ravenclaw)
print('Hufflepuff', Hufflepuff)
print('Slytherin', Slytherin)

print('La casa con mas puntos es: ')

if Hufflepuff > Slytherin and Hufflepuff > Ravenclaw and Hufflepuff > Gryffindor:
    print('Hufflepuff')
elif Slytherin > Hufflepuff and Slytherin > Ravenclaw and Slytherin > Gryffindor:
    print('Slytherin')
elif Ravenclaw > Slytherin and Ravenclaw > Hufflepuff and Ravenclaw > Gryffindor:
    print('Ravenclaw')
elif Gryffindor > Ravenclaw and Gryffindor > Slytherin and Gryffindor > Hufflepuff:
    print('Gryffindor')
else:
    print('Cayo el sistema')