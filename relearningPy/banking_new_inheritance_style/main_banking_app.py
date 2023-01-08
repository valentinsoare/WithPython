#!/usr/bin/python

from bank import Bank
from decimal import Decimal


def main():
    reiff = Bank(bank_name='reiffeisen', country='Romania', city='Bucharest', type_of_bank='commercial')

    valentin_account = reiff.open_account(type_of_account='savings account', owner='Valentin, Soare',
                                          initial_balance=Decimal('25_000'), account_currency='euro',
                                          interest_rate=Decimal('4.20'))

    tudorina_account = reiff.open_account(type_of_account='checking account', owner='Tudorina, Soare',
                                          initial_balance=Decimal('40_000'), account_currency='dollars',
                                          fee_for_transaction=Decimal('100.00'))

    gabi_account = reiff.open_account(type_of_account='checking account', owner='Gabriela, Manea',
                                      initial_balance=Decimal('400_000'), account_currency='pounds',
                                      fee_for_transaction=Decimal('50.00'))

    andreea_account = reiff.open_account(type_of_account='savings account', owner='Andreea, Popescu',
                                         initial_balance=Decimal('500_000'), account_currency='ron',
                                         interest_rate=Decimal('1'))

    valentin_account_1 = reiff.open_account(type_of_account='checking account', owner='Valentin, Soare',
                                            initial_balance=Decimal('1_000_000'), account_currency='pounds',
                                            fee_for_transaction=Decimal('1_000_000'))

    valentin_account.deposit(Decimal('35.50'))
    #print(f"{valentin_account}\n{'-' * 50}")

    valentin_account.calculate_interest()
    #print(f"{valentin_account}")

    count_accounts = reiff.number_of_accounts_open(account_type='checking_account', arguments_number=1)

    print(andreea_account)
    reiff.credit(account_number=andreea_account.account_number, amount=Decimal('10_000'),
                 period=Decimal('24'), rate=Decimal('3'))

    andreea_account.calculate_interest()
    print(andreea_account)


if __name__ == '__main__':
    main()
