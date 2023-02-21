# El "and" operador regresa Truesi ambas condiciones son True, y regresa Falseen caso contrario.
# El "or" operador regresa Truesi al menos una de las condiciones es True, y regresa Falseen caso contrario.
# El "not" operador regresa Truesi la condición es False, y viceversa.

altura = int(input('Ingrese la altura: '))
credit = int(input('Ingrese el valor de creditos: '))
con_persona_alta = int(input('Viene acompañado/a? (false = 0 o true = 1): '))

if credit >= 10:
    if altura < 200:
        if altura < 100 and con_persona_alta == 0:
            print('Aún no eres lo suficientemente alto/a para este paseo')
            # print('if 1')
        elif altura < 100 and con_persona_alta == 1:
            print('Aún no eres lo suficientemente alto/a para este paseo')
            # print('if 2')
        elif altura >= 100 and con_persona_alta == 1:
            print('¡Disfruta del viaje!')
            # print('if 3')
        elif altura >= 137:
            print('¡Disfruta del viaje!')
            # print('if 4')
        else:
            print('Aún no eres lo suficientemente alto/a para este paseo')
            # print('else 1')
    else:
        print('valor invalido')
        # print('else 2')
else:
    print('No tienes suficientes créditos para viajar')
    # print('else 3')