"""

Adivina un n�mero.

El juego consiste en que el juego genera un n�mero aleatorio y el usuario tiene que adivinarlo.
El sistema responder� de la siguiente forma:

    - Buenas: '', Aqu� indica cuantos n�meros de los introducidos por el usuario coinciden en posici�n con el aleatorio.
    - Regulares: '', Aqu� indica cuantos n�meros de los introducidos por el usuario existen dentro
      del n�mero aleatorio pero no est�n bien posicionados.
    - Malas: '', Aqu� indica cuantos n�meros de los introducidos por el usuario ni existen ni
      coinciden en posici�n con el aleatorio.
Cuando el n�mero de Buenas sea 3, el usuario ha acertado el n�mero.

"""

from random import randint

number_to_guess = str(randint(100, 999))

user_number = '0'

while number_to_guess != user_number:

    user_number = input('Introduce un numero: ')

    buenas = 0
    regulares = 0
    malas = 0

    count = 0

    for item in user_number:

        if item == number_to_guess[count]:

            buenas += 1

        elif item in number_to_guess and not item == number_to_guess[count]:

            regulares += 1

        else:

            malas += 1

        count += 1

    print('Buenas: {}\nRegulares: {}\nMalas: {}\n'.format(buenas, regulares, malas))

