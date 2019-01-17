def bigger_number(list):

    number = 0

    for item in list:

        if item > number:

            number = item

    return print(number)

import random

a = range(1,101)
lista_numeros = []

while len(lista_numeros) < 15:

    b = random.choice(a)

    if b not in lista_numeros:

        lista_numeros.append(b)

print(lista_numeros)

variable = lista_numeros

bigger_number(variable)