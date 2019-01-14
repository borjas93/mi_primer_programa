numeros = range (5,16)
numero = int(input('Introduce un numero: '))

print('El resultado es: ')

for item in numeros:

    print('{} x {} = {}'.format(numero, item, item*numero))