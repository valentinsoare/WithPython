#!/usr/bin/python

from decimal import Decimal
from random import randrange
from dataclasses import dataclass
from typing import ClassVar, List, Dict, Tuple


def set_known_for(PRESENT_STATUS):
    value = randrange(len(PRESENT_STATUS))
    return PRESENT_STATUS[value]


@dataclass(order=True)
class InvestmentFund:
    _PRESENT_STATUS: ClassVar[List[str]] = ['Acquisition', 'Takeover', 'Selling Frenzy', 'Killing']

    name_of_fund: str
    social_capital: Decimal
    currency: str
    city: str
    country: str
    known_for = set_known_for(_PRESENT_STATUS)


def __str__(self):
    return f"name_of_fund: {self.name_of_fund}, social_capital: {self.social_capital}, city: {self.city}," \
           f"city: {self.city}, known_for: {self.known_for}"


def __format__(self, given_format):
    return f'{str(self): {given_format}}'

