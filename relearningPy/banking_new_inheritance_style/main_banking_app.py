#!/usre/bin/python

import csv
from bank import Bank
from re import split, sub
from decimal import Decimal


def main():
    ing = Bank(bank_name='ING', country='Romania', city='Bucharest', type_of_bank='commercial')
    valentin_account = ing.open_account(type_of_account='savings account', owner='Valentin, Soare',
                                        initial_balance=Decimal('25_000'), account_currency='euro',
                                        interest_rate=5)

    print(f"\n{' * First instance of the account: '}\n{valentin_account}\n{'-' * 35}")

    valentin_account.deposit(Decimal('125_000'))
    valentin_account.calculate_interest()
    print(f"\n{' * Account after deposit and calculated interest: '}\n{valentin_account}\n{'-' * 35}")

    tudorina_account = ing.open_account(type_of_account='checking account', owner='Tudorina, Soare', initial_balance=Decimal('40_000'),
                                        account_currency='dollars', fee_for_transaction=Decimal('25.44'))

    tudorina_account.deposit(Decimal('25_000'))

    print(f"\n{' * After deposit:'}\n{tudorina_account}")


if __name__ == '__main__':
    main()
