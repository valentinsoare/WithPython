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
                                          fee_for_transaction_checking=Decimal('100.00'))

    gabi_account = reiff.open_account(type_of_account='checking account', owner='Gabriela, Manea',
                                      initial_balance=Decimal('400_000'), account_currency='pounds',
                                      fee_for_transaction_checking=Decimal('50.00'))
    andreea_account = reiff.open_account(type_of_account='savings account', owner='Andreea, Popescu',
                                         initial_balance=Decimal('500_000'), account_currency='euro',
                                         interest_rate=Decimal('1'))
    valentin_account_1 = reiff.open_account(type_of_account='checking account', owner='Valentin, Soare',
                                            initial_balance=Decimal('1_000_000'), account_currency='pounds',
                                            fee_for_transaction_checking=Decimal('1_000_000'))
    stelian_account = reiff.open_account(type_of_account='checking account', owner='Stelian, Soare',
                                         initial_balance=Decimal('0.00'), account_currency='pounds',
                                         fee_for_transaction_checking=Decimal('5'))

    valentin_account.deposit(amount=Decimal('35.50'))
    valentin_account.calculate_interest()
    count_accounts = reiff.number_of_accounts_open(account_type='checking_account')

    reiff.credit(account_number=andreea_account.account_number, amount=Decimal('10_000'), period=Decimal('24'), rate=Decimal('3'))
    reiff.credit(account_number=valentin_account.account_number, amount=Decimal('45_000'), period=Decimal('36'),
                 rate=Decimal('10.3'))
    reiff.credit(account_number=valentin_account_1.account_number, amount=Decimal('100_000'), period=Decimal('72'),
                 rate=Decimal('2.17'))
    reiff.credit(account_number=valentin_account.account_number, amount=Decimal('450_000'), period=Decimal('362'),
                 rate=Decimal('9.3'))
    reiff.credit(account_number=tudorina_account.account_number, amount=Decimal('1_450_000'), period=Decimal('12'),
                 rate=Decimal('1.2'))
    reiff.credit(account_number=gabi_account.account_number, amount=Decimal('10_000'), period=Decimal('6'),
                 rate=Decimal('23.44'))

    ax = reiff.search_account(account_currency='pounds')
    ay = reiff.number_of_accounts_open(currency='pounds')
    az = reiff.search_account(owner='Valentin, Soare')

    andreea_account.deposit(amount=Decimal('10_000'))
    andreea_account.deposit(amount=Decimal('10_000'))

    gigel_account = reiff.open_account(type_of_account='salary account', owner='Gigel, Sora', initial_balance=Decimal('4_000'),
                                       account_currency='dollars', transaction_fees_salary=Decimal('2.00'), commissions_type_salary='monthly',
                                       commissions_amount_salary=Decimal('10'), card_withdraw_fees=Decimal('3.5'), annual_fees=Decimal(20.00))
    reiff.create_credit_card(account_number=gigel_account.account_number, owner=gigel_account.owner, balance=gigel_account.balance,
                             currency=gigel_account.currency, credit_card_withdraw_fees=gigel_account.credit_card_withdraw_fees,
                             annual_maintenance_fees=gigel_account.annual_maintenance_fees, card_type='gold', type_of_commissions='monthly',
                             commission_amount=Decimal('10'), transaction_fees=Decimal('3.5'))



    gigel_account.deposit(amount=Decimal('5_000'))
    gigel_account.deposit(amount=Decimal('7_000'))
    gigel_account.deposit(amount=Decimal('4_000'))
    gigel_account.deposit(amount=Decimal('6_000'))
    #print(f'\n{gigel_account}\n')

    gigel_account.overdraft(amount=Decimal('12.00'))

    #print(gigel_account.balance)

    #print(reiff.search_credits(period_of_credit='< 25', interest_rate='== 3'))

    ax = reiff.number_of_accounts_open(currency='pounds')

    print(reiff.credit_cards)


if __name__ == '__main__':
    main()
