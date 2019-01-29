"""
Este ejercicio trata sobre contar las palabras que aparecen en una cadena.
Para este cometido, vamos a definir una funcion muy basica que detecte las palabras de cualquier texto.
"""


def detectar_palabras(cadena):
    lista_palabras = []
    palabra = ''
    for item in cadena:
        if item != ' ' and item != ',' and item != '.':
            palabra += item

        else:
            lista_palabras.append(palabra)
            palabra = ''
    print(lista_palabras)
    return lista_palabras


def cont_palabras(lista):
    apariciones_palabra = dict()
    for item in lista:
        if item not in apariciones_palabra:
            indice = 0
            apariciones = 0
            while indice < len(lista):
                if item == lista[indice]:
                    apariciones += 1
                indice += 1
            apariciones_palabra[item] = 'aparece {} vez/veces'.format(apariciones)
    print (apariciones_palabra)
    return


cadena_usuario = 'hola hola moco moco nate borja hola moco'
lista_usuario = detectar_palabras(cadena_usuario)
cont_palabras(lista_usuario)

