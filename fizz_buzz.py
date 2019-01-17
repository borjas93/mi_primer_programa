"""
El ejercicio consiste en cambiar los números de una lista
por un fizz o un buzz en función de lo siguiente:
    Si el número es múltiplo de 3, se cambiará ese número
por un Fizz.
    Si el número es múltiplo de 5, se cambiará ese número
por un Buzz.
    En caso de que el número sea múltplo de 3 y 5, se cam-
biará el número por un Bazzinga
"""

import random

a = range(1,101)
lista_numeros = []

while len(lista_numeros) < 15:

    b = random.choice(a)

    if b not in lista_numeros:

        lista_numeros.append(b)

print(lista_numeros)

for item in lista_numeros:

    indice = lista_numeros.index(item)

    if item%3 == 0 and not item%5 == 0:

        lista_numeros[indice] = 'Fizz'

    elif item%5 == 0 and not item%3 == 0:

        lista_numeros[indice] = 'Buzz'

    elif item%3 == 0 and item%5 == 0:

        lista_numeros[indice] = 'Bazzinga'

print(lista_numeros)