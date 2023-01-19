#!/usr/bin/python

from bank import Bank
from decimal import Decimal


def main():
    reiff = Bank(bank_name='reiffeisen', country='Romania', city='Bucharest', type_of_bank='commercial')

    reiff.open_account(type_of_account='salary account', owner='Valentin, Soare', initial_balance=Decimal('50_000'),
                       account_currency='euros', owner_address='Lucretu Patrascanu, Nr. 9', commissions_type_salary='daily')

    print(reiff.accounts)


if __name__ == '__main__':
    main()
