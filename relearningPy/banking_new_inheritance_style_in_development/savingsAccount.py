#!/usr/bin/python

from decimal import Decimal
from account import Account


class SavingsAccount(Account):
    def __init__(self, *, account_number, owner, balance, currency, interest_rate, owner_address):

        super().__init__(account_number=account_number, owner=owner,
                         balance=balance, currency=currency, owner_address=owner_address)

        self.interest_rate: Decimal = interest_rate
        self._interest: Decimal = Decimal('0.00')

    @property
    def interest_rate(self) -> Decimal:
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Interest rate for a savings account should be a float/int value greater than zero!')

        self._interest_rate = amount.quantize(Decimal('0.00'))

    @property
    def interest(self) -> Decimal:
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

    def __repr__(self) -> str:
        message_to_return = f'account_number: {self.account_number}\n' \
                            f'{Account.__str__(self)}\n' \
                            f'interest_rate: {self.interest_rate}%\n' \
                            f'type_of_account: savings_account\n'

        if self.interest != Decimal('0.00'):
            message_to_return += f'interest: {Decimal(self.interest):,}'
        else:
            message_to_return += f'interest: not calculated'

        return message_to_return

    def __str__(self):
        return self.__repr__()
