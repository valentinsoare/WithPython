#!/usr/bin/python

import logging
import pprint

from bank import Bank
from decimal import Decimal


def main():
    reiff = Bank(bank_name='reiffeisen', country='Romania', city='Bucharest', type_of_bank='commercial')

    vs = reiff.open_salary_account(owner='Valentin, Soare', balance=Decimal('10_000'), currency='euro', transaction_salary_fees=Decimal('10.00'),
                                   type_of_commission='monthly', commission_amount=Decimal('5.00'), credit_card_withdraw_fees=Decimal('0.00'),
                                   annual_maintenance_fees=Decimal('20.00'), owner_address='Lucreitu Patrascanu, Nr. 9, Bl. Y2, Ap. 21, Bucuresti, Sector 3')
    vs.deposit(amount=Decimal('1_250.50'))
    vs.deposit(amount=Decimal('4_575'))
    vs.deposit(amount=Decimal('6_750'))
    vs.deposit(amount=Decimal('12_652.44'))

    print(reiff.debug())


if __name__ == '__main__':
    main()
