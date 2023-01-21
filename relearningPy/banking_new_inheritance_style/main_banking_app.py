#!/usr/bin/python


from bank import Bank
from decimal import Decimal


def main():
    reiff = Bank(bank_name='reiffeisen', country='Romania', city='Bucharest', type_of_bank='commercial')

    vs = reiff.open_salary_account(owner='Valentin, Soare', balance=Decimal('10_000'), currency='euro', transaction_salary_fees=Decimal('10.00'),
                                   type_of_commission='monthly', commission_amount=Decimal('5.00'), credit_card_withdraw_fees=Decimal('0.00'),
                                   annual_maintenance_fees=Decimal('20.00'), owner_address='Lucreitu Patrascanu, Nr. 9, Bl. Y2, Ap. 21, Bucuresti, Sector 3')
    print(vs)



if __name__ == '__main__':
    main()
