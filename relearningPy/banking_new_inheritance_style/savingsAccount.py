#!/usr/bin/python

from decimal import Decimal
from account import Account


class SavingsAccount(Account):
    def __init__(self, *, nr_of_the_account, owner_of_the_account, account_balance, currency_for_account, interest_rate):

        super().__init__(account_number=nr_of_the_account, owner=owner_of_the_account,
                         balance=account_balance, currency=currency_for_account)

        self.interest_rate: Decimal = interest_rate
        self._interest: Decimal = Decimal('0.00')

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Interest rate for a savings account should be a float/int value greater than zero!')

        self._interest_rate = amount.quantize(Decimal('0.00'))

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, amount):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Interest should be a decimal and greater than zero!')

        self._interest = amount.quantize(Decimal('0.00'))

    def calculate_interest(self):
        self.interest = (self.balance * self.interest_rate) / 100
        self.deposit(amount=self.interest)

    def __getattr__(self, item):
        if item in {'transaction_fee', 'type_of_commissions', 'commission_amount', 'credit_card_withdraw_fees',
                    'annual_maintenance_fees', 'transaction_fees'}:
            raise NotImplementedError
        else:
            return getattr(self, item)

    def __str__(self):
        message_to_return = f'account_number: {self.account_number}\n' \
                            f'{Account.__str__(self)}\n' \
                            f'interest_rate: {self.interest_rate}%\n'

        if self.interest != Decimal('0.00'):
            message_to_return += f'interest: {Decimal(self.interest):,}'
        else:
            message_to_return += f'interest: not calculated'

        return message_to_return


