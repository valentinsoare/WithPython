#!/usr/bin/python

from dataclasses import dataclass
from typing import ClassVar, List


@dataclass
class Card:
    FACES: ClassVar[List[str]] = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS: ClassVar[List[str]] = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    face: str
    suit: str

    def __str__(self):
        return f'{self.face} of {self.suit}'

    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'







