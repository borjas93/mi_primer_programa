numeros = range (1,11)
numero = int(input('Introduce un numero: '))

print('El resultado es: ')

for item in numeros:
    if item%2 == 0:
        print('{} x {} = {}'.format(numero, item, item*numero))