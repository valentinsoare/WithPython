#!/usr/bin/python


from re import match, split
from decimal import Decimal
from collections import namedtuple


class Account:
    def __init__(self, *, account_number, owner, balance, currency, owner_address):
        self.account_number: str = account_number
        self.owner: namedtuple = owner
        self.balance: Decimal = balance
        self.currency: str = currency
        self.owner_address: str = owner_address

    @property
    def account_number(self) -> str:
        return self._account_number

    @account_number.setter
    def account_number(self, value_of_account: str):
        if not (isinstance(value_of_account, str) and value_of_account.isalnum()):
            raise ValueError('Account number should contain letters and digits, that is it!')

        self._account_number = value_of_account

    @property
    def owner(self) -> str:
        return self._owner

    @owner.setter
    def owner(self, owner_name: str):
        split_owner_name = split(r',\s?', owner_name)
        
        if not isinstance(owner_name, str) or len(split_owner_name) != 2 or (len(split_owner_name[0]) or len(split_owner_name[1])) == 0 or \
                match(r'\s.*', split_owner_name[0]) or match(r'\s.*', split_owner_name[1]):
            raise ValueError('Owner name should contains first name and last name in this order separated by a comma!')

        owner = namedtuple('owner', {'first_name', 'last_name'})
        account_owner = owner(first_name=split_owner_name[0], last_name=split_owner_name[1])

        self._owner = f'{account_owner.first_name}, {account_owner.last_name}'

    @property
    def balance(self) -> Decimal:
        return self._balance

    @balance.setter
    def balance(self, balance_amount: Decimal):
        if not isinstance(balance_amount, Decimal) or balance_amount < Decimal('0.00'):
            raise ValueError('Account value needs to be a decimal value greater or equal to zero!')

        self._balance = balance_amount.quantize(Decimal('0.00'))

    @property
    def currency(self) -> str:
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        if not (currency and isinstance(currency, str)) or match(r'\s+', currency):
            raise ValueError('Currency should be a string containing alphas characters!')

        self._currency = currency

    @property
    def owner_address(self) -> str:
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address: str) :
        if not (owner_address and isinstance(owner_address, str)) or len(split(r',\s*', owner_address)) < 2:
            raise ValueError('Owner address should be a string with a street '
                             'name and number at least separatet by a comma!')

        self._owner_address = owner_address

    def deposit(self, *, amount: Decimal) -> Decimal:
        if not (amount and isinstance(amount, Decimal)) or amount <= Decimal('0.00'):
            raise ValueError('Deposit amount should be a decimal value greater than zero!')

        self.balance += amount
        return self.balance

    def withdraw(self, *, amount: Decimal) -> Decimal:
        if not (amount and isinstance(amount, Decimal)) or amount > self.balance:
            raise ValueError('Withdraw amount should be a decimal value and not greater than the balance!')

        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f'owner: {self.owner}\n' \
               f'balance: {self.balance:,}\n' \
               f'currency: {self.currency}\n' \
               f'owner_address: {self.owner_address}'

    def __str__(self):
        return self.__repr__()


