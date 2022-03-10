#!/usr/bin/python

import random
from card import Card
#from cardDataClass import Card


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
        counting = 0
        self.shuffle()

        for i in self._deck:
            self._hands.append(i)

            if counting == 9:
                break

            counting += 1

    def printing_poker_hands(self):
        counter = 0

        print(f'\nFirst hand: ', end=" ")

        for i in range(len(self._hands)):
            if counter == 5:
                print(f'\nSecond hand: ', end=" ")

            print(f'{self._hands[i]:<15}', end=" ")
            counter += 1

        print("\n")

    def __str__(self):
        to_print = ''

        for index, card in enumerate(self._deck):
            to_print += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                to_print += '\n'

        return to_print
