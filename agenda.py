'''
Ejercicio de una agenda de telefonos usando listas.
'''
agenda = []

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
        agenda.append([nombre, numero])

    elif accion == 'C':
        nombre = input('De quien quieres saber el numero? ').capitalize()
        print('')
        for item in agenda:
            if nombre == item[0]:
                print(item[1])

    else:
        break