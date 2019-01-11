import random

rival = input('Selecciona un rival: (Bulbasaur, Squirtle o Charmander) ').capitalize()
yo = 'Pikachu'

vida_pikachu = 100
vida_bulbasaur = 100
vida_squirtle = 120
vida_charmander = 90

[chispazo, bola_voltio] = 10,12
[dano_bul, dano_char, dano_squ] = 10 , 11 , 9

while rival != 'Bulbasaur' and rival != 'Charmander' and rival != 'Squirtle':

    print('Te has equivocado al escribir. Vuelve a introducir un nombre pokemon valido.')
    rival = input('Selecciona un rival: (Bulbasaur, Squirtle o Charmander) ').capitalize()


if rival == 'Squirtle':

    print('Los ataques de Pikachu son superefectivos contra Squirtle!')
    print('Se sumará +2 de ataque a chispazo y +3 a bola voltio')

    chispazo +=2
    bola_voltio +=3

    vida_rival = vida_squirtle
    dano_rival = dano_squ

elif rival == 'Charmander':

    vida_rival = vida_charmander
    dano_rival = dano_char

elif rival == 'Bulbasaur':

    vida_rival = vida_bulbasaur
    dano_rival = dano_bul


print('¡Que de comience el combate!')

while vida_pikachu and vida_rival > 0:

    contendientes = yo , rival
    turno = random.choice(contendientes)

    print('Es turno de {}'.format(turno))

    if turno == yo:

        ataque = input('Selecciona un ataque: (Bola voltio/Chispazo) ').capitalize()

        if ataque == 'Bola voltio':

            vida_rival -= bola_voltio
            print('Le has hecho {} puntos de daño. A {} le quedan {} puntos de vida'.format(bola_voltio , rival , vida_rival))

        elif ataque == 'Chispazo':

            vida_rival -= chispazo
            print('Le has hecho {} puntos de daño. A {} le quedan {} puntos de vida'.format(chispazo , rival , vida_rival))

        if vida_rival == 0:

            print('¡Has ganado!')
            break

        else:

            vida_pikachu -= dano_rival
            print('A {} le quedan {} puntos de vida'.format(yo , vida_pikachu))

    else:

        vida_pikachu -= dano_rival

        if vida_pikachu == 0:

            print('¡Has perdido!')
            break

        else:

            print('A {} le quedan {} puntos de vida'.format(yo, vida_pikachu))
            ataque = input('Selecciona un ataque: (Bola voltio/Chispazo) ').capitalize()

            if ataque == 'Bola voltio':

                vida_rival -= bola_voltio
                print('Le has hecho {} puntos de daño. A {} le quedan {} puntos de vida'.format(bola_voltio, rival, vida_rival))

            elif ataque == 'Chispazo':

                vida_rival -= chispazo
                print('Le has hecho {} puntos de daño. A {} le quedan {} puntos de vida'.format(chispazo, rival, vida_rival))

            if vida_rival == 0:

                print('¡Has ganado!')
                break

            else:

                vida_pikachu -= dano_rival
                print('A {} le quedan {} puntos de vida'.format(yo, vida_pikachu))
