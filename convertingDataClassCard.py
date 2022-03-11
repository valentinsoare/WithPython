#!/usr/bin/python

import dataclasses
import random
from typing import ClassVar, List


@dataclasses.dataclass
class Card:
    FACES: ClassVar[List[str]] = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS: ClassVar[List[str]] = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    face: str
    suit: str

    def __str__(self):
        return f'{self.face} of {self.suit}'

    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'


def generate_deck_cards():
    number_of_cards = 52
    deck_of_cards = []

    for i in range(number_of_cards):
        card = Card(Card.FACES[i % 13], Card.SUITS[i // 13])
        deck_of_cards.append(card)

    return deck_of_cards


def shuffle_deck_of_cards(deck_of_cards):
    random.shuffle(deck_of_cards)
    return deck_of_cards


def printing_deck_of_cards(deck_cards):
    for i in range(0, len(deck_cards)):
        print(f'{deck_cards[i]:<19}', end=" ")
        if (i + 1) % 4 == 0:
            print()


def converting_from_card_obj_to_tuples_dicts(deck_of_cards, option=0):
    list_with_tuples = []
    list_with_dicts = []

    if option == 0:
        for i in deck_of_cards:
            list_with_tuples.append(dataclasses.astuple(i))

        return list_with_tuples

    elif option == 1:
        for i in deck_of_cards:
            list_with_dicts.append(dataclasses.asdict(i))

        return list_with_dicts


def main():
    deck_of_cards = generate_deck_cards()
    shuffled_deck = shuffle_deck_of_cards(deck_of_cards)

    printing_deck_of_cards(shuffled_deck)

    obj_to_dict = converting_from_card_obj_to_tuples_dicts(shuffled_deck, 1)
    obj_to_tuples = converting_from_card_obj_to_tuples_dicts(shuffled_deck, 0)

    #print(obj_to_dict)
    #print(obj_to_tuples)


if __name__ == '__main__':
    main()
