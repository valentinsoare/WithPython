#!/usr/bin/python

import random
from card import Card


class DeckOfCards:
    NUMBER_OF_CARDS = 52

    def __init__(self):
        self._current_card = 0
        self._deck = []
        self._hands = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], Card.SUITS[count // 13]))

    def shuffle(self):
        self._current_card = 0
        random.shuffle(self._deck)

    def get_poker_hands(self):
        return self._hands

    def deal_card(self):
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None

    def poker_hands(self):
        hands = 0

        while hands != 2:
            self.shuffle()
            counting = 0

            for i in self._deck:
                self._hands.append(i)

                if counting == 4:
                    print()
                    break
                counting += 1

            hands += 1

    #def printing_poker_hands(self):


    def __str__(self):
        to_print = ''

        for index, card in enumerate(self._deck):
            to_print += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                to_print += '\n'

        return to_print


def main():
    all_cards = DeckOfCards()
    all_cards.poker_hands()




main()
