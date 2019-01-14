lista_numeros = []
numero = None

while True:

    numero = input('Introduce un numero: ')
    print('Para salir del bucle, introduce: Fin')

    if numero == 'Fin':

        break

    lista_numeros.append(int(numero))
    print(lista_numeros)

for item in lista_numeros:

    numero_peque = lista_numeros[0]

    if item < numero_peque:

        numero_peque = item

print('El numero mas pequeno es: {}'.format(numero_peque))