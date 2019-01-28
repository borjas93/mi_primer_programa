'''
Ejercicio de lista telefonica usando diccionarios
'''

agenda = dict()

while True:

    print('')
    print('¿Que quieres hacer?')
    print('')
    accion = input('Añadir numero [A] / Consultar numero [C] / Corregir numero [Corregir] / Salir [S] ').capitalize()
    print('')

    if accion == 'A':
        nombre = input('Cual es el nombre? ').capitalize()
        print('')
        numero = input('Cual es su numero? ')
        agenda[nombre] = numero

    elif accion == 'C':
        nombre = input('De quien quieres saber el numero? ').capitalize()
        print('')
        print(agenda[nombre])

    else:
        break