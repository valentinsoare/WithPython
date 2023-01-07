#!/usr/bin/python

from typing import Union
from decimal import Decimal
from account import Account


class SavingsAccount(Account):
    def __init__(self, owner_of_the_account, account_balance, currency_for_account, interest_rate):

        super().__init__(owner=owner_of_the_account, balance=account_balance, currency=currency_for_account)

        self.interest_rate: Union[int, float] = interest_rate
        self._interest: Decimal = Decimal('0.00')

    @property
    def interest_rate(self):
        return self._interest_rate

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, amount):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Interest should be a decimal and greater than zero!')

        self._interest = amount

    @interest_rate.setter
    def interest_rate(self, amount: Union[int, float]):
        if not isinstance(amount, Union[int, float]) or amount <= 0:
            raise ValueError('Interest rate for a savings account should be a float/int value greater than zero!')

        self._interest_rate = amount

    def calculate_interest(self):
        self.interest = self.balance * self.interest_rate
        return self.interest

    def __str__(self):
        message_to_return = f'owner: {self.owner}\n' \
                            f'balance: {Decimal(self.balance):,}\n' \
                            f'currency: {self.currency}\n' \
                            f'interest_rate: {self.interest_rate}%\n'
        if self.interest != Decimal('0.00'):
            message_to_return += f'interest: {Decimal(self.interest):,}'
        else:
            message_to_return += f'interest: not calculated'

        return message_to_return


