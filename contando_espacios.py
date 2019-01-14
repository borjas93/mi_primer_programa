# Ejemplo:
texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"

caracteres = [' ', '.', ',']

espacio = 0
punto = 0
coma = 0

for item in texto_usuario:

    if item in caracteres:

        if item == ' ':

            espacio += 1

        elif item == '.':

            punto += 1

        else:

            coma += 1

print ('En la frase hay: {} espacios, {} puntos y {} comas'.format(espacio, punto, coma))

"""Output esperado
espacios = 6
puntos = 1
comas = 1
"""