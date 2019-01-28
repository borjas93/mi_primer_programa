agenda = []

while True:

    print('¿Que quieres hacer?')
    accion = input('Añadir numero [A] / Consultar numero [C] / Corregir numero [Corregir] / Salir [S] ').capitalize()

    if accion == 'A':
        nombre = input('Cual es el nombre? ').capitalize()
        numero = input('Cual es su numero? ')
        agenda.append([nombre, numero])

    elif accion == 'C':
        nombre = input('De quien quieres saber el numero? ').capitalize()
        for item in agenda:
            if nombre == item[0]:
                print(item[1])

    else:
        break