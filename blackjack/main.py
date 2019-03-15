import random
from time import sleep

from blackjack_deck import Deck

if __name__ == '__main__':

    deck = Deck()
    while True:

        if deck.cards != []:
            random_card = deck.random_card()
            print(random_card)
            print(deck)
        else:
            print('\nNew deck\n')
            deck = Deck()
            random_card = deck.random_card()
            print(random_card)
            print(deck)
        sleep(0.25)
