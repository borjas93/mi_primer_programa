"""
Crea una función que muestre por pantalla un texto y tantas
barritas de subrayado como larga sea la string.
"""


def barritas(cadena):

    cadena_barritas = len(cadena)*'-'

    return cadena_barritas


user_string = input('Introduce un texto: ')
str_bar = barritas(user_string)
print(user_string)
print(str_bar)