"""
Obtener el largo de una lista sin usar la funcion len()

El programa solicitará al usuario una serie de números
que se irán añadiendo a una lista.

Despues se calculará la longitud de esa lista.
"""

lista_numeros = []
numero = None

while True:

    print('Para salir del bucle, introduce: Fin')
    numero = input('Introduce un numero: ')
    fin = numero.capitalize()

    if fin == 'Fin':

        break

    lista_numeros.append(int(numero))
    print(lista_numeros)

largo_lista = 0

for item in lista_numeros:

    largo_lista += 1

print(largo_lista)
