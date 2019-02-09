from time import sleep
import random


def write_sent(phrase):

    while True:

        choosed_phrase = random.choice(phrase)
        with open('phrase.txt', 'a') as phrase_file:
            phrase_file.write(choosed_phrase)
            phrase_file.write('\n')

        sleep(2)


phrase1 = input('Escribe una oracion: ')
phrase2 = input('Escribe una oracion: ')
phrase3 = input('Escribe una oracion: ')
user_phrase = [phrase1, phrase2, phrase3]

write_sent(user_phrase)
