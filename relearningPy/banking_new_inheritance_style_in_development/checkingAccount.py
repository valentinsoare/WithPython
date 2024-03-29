#!/usr/bin/python

from decimal import Decimal
from account import Account


class CheckingAccount(Account):
    def __init__(self, *, account_number, owner, balance, currency, transaction_fee, owner_address):
        super().__init__(account_number=account_number, owner=owner,
                         balance=balance, currency=currency, owner_address=owner_address)

        self.transaction_fee: Decimal = transaction_fee

    @property
    def transaction_fee(self) -> Decimal:
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount == Decimal('0.00'):
            raise ValueError('Transaction fee should not be zero or greater than the balance and a decimal value!')

        self._transaction_fee = amount.quantize(Decimal('0.00'))

    def deposit(self, *, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Deposit value should be a decimal greater than zero!')

        self.balance += (amount - self.transaction_fee)
        return self.balance

    def withdraw(self, *, amount: Decimal) -> Decimal:
        if not isinstance(amount, Decimal) or amount + self.transaction_fee > self.balance or amount <= Decimal('0.00'):
            raise ValueError('Withdraw value should be a decimal and withdraw valu + transaction fee should  '
                             'not be greater  than the balance or the sum to be withdraw equal or less than zero!')

        self.balance -= (amount + self.transaction_fee)
        return self.balance

    def __getattr__(self, item):
        if item in {'interest', 'interest_rate', 'calculate_interest', 'type_of_commissions', 'commission_amount',
                    'credit_card_withdraw_fees', 'annual_maintenance_fees', 'transaction_fees'}:
            raise NotImplementedError
        else:
            return getattr(self, item)

    def __repr__(self):
        return f'account_number: {self.account_number}\n' \
                                  f'{Account.__str__(self)}\n' \
                                  f'transaction_fee: {self.transaction_fee:,}\n' \
                                  f'type_of_account: checking_account'

    def __str__(self) -> str:
        return self.__repr__()
