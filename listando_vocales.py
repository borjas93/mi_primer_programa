# Ejemplo:
texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"

vocales = ['a', 'e', 'i', 'o', 'u']
lista_vocales = []

for item in texto_usuario:

    if item in vocales:

        lista_vocales.append(item)

print (lista_vocales)