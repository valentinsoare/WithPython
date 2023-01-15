#!/usr/bin/python

from decimal import Decimal
from salaryAccount import SalaryAccount


class CreditCard(SalaryAccount):
    def __init__(self, account_number, owner, balance, currency, credit_card_withdraw_fees, annual_maintenance_fees,
                 type_of_commissions, commission_amount, transaction_fees, type_of_card):
        super().__init__(account_number=account_number, owner=owner, balance=balance, currency=currency,
                         credit_card_withdraw_fees=credit_card_withdraw_fees, annual_maintenance_fees=annual_maintenance_fees,
                         type_of_commissions=type_of_commissions, commission_amount=commission_amount, transaction_fees=transaction_fees)

        self.type_of_card = type_of_card

    @property
    def type_of_card(self):
        return self._type_of_card

    @type_of_card.setter
    def type_of_card(self, card_type):
        if not (card_type and isinstance(card_type, str)) or card_type not in {'regular', 'silver', 'gold', 'platinum'}:
            raise ValueError('Card type should be a str and one of the following: regular, silver, gold or platinum!')

        self._type_of_card = card_type

    def card_withdraw(self, amount):
        if not(amount and isinstance(amount, Decimal)) or (amount + self.credit_card_withdraw_fees) > self.balance or \
               amount <= Decimal('0.00'):
            raise ValueError('Amount to be withdraw must be a decimal, greater than zero '
                             'and not greater than balance + fees!')

        self.balance -= (amount + self.credit_card_withdraw_fees)

    def cash_card_deposit(self, amount):
        if not(amount and isinstance(amount, Decimal)) or amount <= Decimal('0.00') or \
               self.transaction_fees > (self.balance + amount):
            raise ValueError('Deposit amount should be greater than zero and amount + balance should not be '
                             'less than transaction fees')

        self.balance += (amount - self.transaction_fees)

    def __str__(self):
        return f'account_number: {self.account_number}\n' \
               f'owner: {self.owner}\n' \
               f'balance: {self.balance}\n' \
               f'currency: {self.currency}\n' \
               f'credit_card_withdraw_fees: {self.credit_card_withdraw_fees}\n' \
               f'annual_maintenance_fees: {self.annual_maintenance_fees}\n' \
               f'type_of_card: {self.type_of_card}\n'



