class Cards:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return 'The card is the {} of {}'.format(self.number, self.suit)


class Deck:
    number_of_cards = 52
    suit = ['Pikes', 'Diamond', 'Clovers', 'Hearts']
    max_number = 13

    def __init__(self):
        self.cards = []
        for suit in self.suit:
            for number in range(1, self.max_number + 1):
                self.cards.append(Cards(number, suit))

    def random_card(self):
        return self.cards.pop(random.choice(range(0, len(self.cards))))

    def __str__(self):
        str_cards = [str(card) for card in self.cards]
        return 'Remains {} cards in the deck'.format(len(self.cards))


class Player:
    score = 0

    def __init__(self, name, score):
        self.score = score
        self.name = name


class Game:
    def __init__(self):
        deck = Deck()


if __name__ == '__main__':
    import random
    from time import sleep
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
