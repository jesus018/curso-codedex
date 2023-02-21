import random

# name = 'Hola mundo'
# user_id = 1124853902
# progress = 0.75
# exp = 60
# verified = true

num = random.randint(1, 9)

pregunta = input('Escribe tu pregunta: ')

print('Pregunta:', pregunta)

if num == 1:
    print('Bola 8 Magica: Sí definitivamente.')
elif num == 2:
    print('Bola 8 Magica: Es decididamente así.')
elif num == 3:
    print('Bola 8 Magica: Sin duda.')
elif num == 4:
    print('Bola 8 Magica: Respuesta confusa, intenta otra vez.')
elif num == 5:
    print('Bola 8 Magica: Pregunta de nuevo más tarde.')
elif num == 6:
    print('Bola 8 Magica: Mejor no decirte ahora.')
elif num == 7:
    print('Bola 8 Magica: Mis fuentes dicen que no.')
elif num == 8:
    print('Bola 8 Magica: Las perspectivas no son tan buenas.')
elif num == 9:
    print('Bola 8 Magica: Muy dudoso.')
else:
    print('Bola 8 Magica: Se callo el sistema')