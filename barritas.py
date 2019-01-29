"""
Crea una función que muestre por pantalla un texto y tantas
barritas de subrayado como larga sea la string.
"""


def barritas(cadena):

    cadena_barritas = len(cadena)*'-'
    print(cadena)
    print(cadena_barritas)
    return


user_string = input('Introduce un texto: ')
barritas(user_string)
