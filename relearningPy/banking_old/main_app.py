#!/usr/bin/python

import csv
import json
import collections
from bank import Bank
from decimal import Decimal


def main():
    bcr = Bank('Romania', 'Bucharest', 'commercial', 'Banca Comerciala Romana', Decimal('500_000'))
    vali = bcr.create_account('Valentin', 'leu', Decimal('0.00'), 'selfservice')
    andreea = bcr.create_account('Andreea', 'leu', Decimal('0.00'), 'vip')
    vali.credit(amount=Decimal('5_000'), period=Decimal('12'), rate=Decimal('4.6'))
    andreea.credit(amount=Decimal('1_000_000'), period=Decimal('36'), rate=Decimal('4.8'))


if __name__ == '__main__':
    main()
