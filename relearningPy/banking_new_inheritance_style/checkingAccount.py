#!/usr/bin/python

from decimal import Decimal
from account import Account


class CheckingAccount(Account):
    def __init__(self, owner, balance, currency, transaction_fee):
        super().__init__(owner, balance, currency)

        self.transaction_fee: Decimal = transaction_fee

    @property
    def transaction_fee(self):
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount > self.balance or amount == Decimal('0.00'):
            raise ValueError('Transaction fee should not be zero or greater than the balance and a decimal value!')

        self._transaction_fee = amount

    def deposit(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Deposit value should be a decimal greater than zero!')

        self.balance += (amount - self.transaction_fee)

    def withdraw(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount + self.transaction_fee > self.balance or amount <= Decimal('0.00'):
            raise ValueError('Withdraw value should be a decimal and withdraw valu + transaction fee should  not be greater '
                             'than the balance or the sum to be withdraw equal or less than zero!')

        self.balance -= (amount + self.transaction_fee)

    def __str__(self):
        message_to_be_returned: str = f'owner: {self.owner}\n' \
                                      f'balance: {self.balance:,}\n' \
                                      f'currency: {self.currency}\n' \
                                      f'transaction_fee: {self.transaction_fee:,}'

        return message_to_be_returned
