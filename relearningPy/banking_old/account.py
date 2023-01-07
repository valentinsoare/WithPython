#!/usr/bin/python

from re import match
from credit import Credit
from decimal import Decimal


class Account:
    def __init__(self, account_number: str, account_owner: str, currency: str, balance=Decimal('0.00'),
                 type_of_account: str ='serlfservice', location_account: str ='Bucharest', available_for_credit: int = 0):

        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance
        self.currency = currency
        self.type_of_account = type_of_account
        self.location_account = location_account

        self.credits_made: dict = {}

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, number_of_the_account):
        if not isinstance(number_of_the_account, str) or number_of_the_account == '':
            raise ValueError('Account number must be a string with a specific pattern!')

        self._account_number = number_of_the_account

    @property
    def account_owner(self):
        return self._account_owner

    @account_owner.setter
    def account_owner(self, name_of_the_owner: str):
        if not isinstance(name_of_the_owner, str) or match(r'\s+', name_of_the_owner) or name_of_the_owner == '':
            raise ValueError('Account owner value must be string with alpha or alphanum characters!')
        elif not name_of_the_owner.isascii():
            raise ValueError('Account owner value should not contain only numerical chars. '
                             'Please use also alphas or alnum chars!')

        self._account_owner = name_of_the_owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance_value: Decimal):
        if balance_value == '' or not isinstance(balance_value, Decimal) or balance_value < Decimal('0.00'):
            raise ValueError('Balance variable needs to be a decimal not less than zero.')

        self._balance = balance_value

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        if not isinstance(currency, str) or currency == '' or match(r'\s+', currency):
            raise ValueError('Currency needs to be a current string that represents a type of coin for the country!')

        self._currency = currency

    @property
    def type_of_account(self):
        return self._type_of_account

    @type_of_account.setter
    def type_of_account(self, account_type: str):
        if not isinstance(account_type, str) or match(r'\s+', account_type) or account_type == '' or not account_type.isalnum():
            raise ValueError('Type of account variable must be a string with alphas or alnum chars!')
        elif account_type not in ['selfservice', 'corporate', 'vip']:
            raise ValueError('Account type must be one of the following values: selfservice, corporate and vip.')

        self._type_of_account = account_type

    @property
    def location_account(self):
        return self._location_account

    @location_account.setter
    def location_account(self, location_for_the_account: str):
        if not isinstance(location_for_the_account, str) or match(r'\s+', location_for_the_account) or location_for_the_account == '' \
                or not location_for_the_account.isascii():
            raise ValueError('Location must be a city with alnum chars or alpha!')

        self._location_account = location_for_the_account

    def deposit(self, amount: Decimal):
        if not isinstance(amount, Decimal) or str(amount) == '' or amount < Decimal(0.00):
            raise ValueError('Deposit amount value should be a decimal type and greater than zero.')

        self._balance += amount

    def withdraw(self, amount: Decimal):
        if not isinstance(amount, Decimal) or str(amount) == '' or amount > self.balance or amount < Decimal('0.00'):
            raise ValueError('Withdraw amount should not be greater than balance amount or less than zero!')

        self._balance -= amount

    def credit(self, amount: Decimal, period: Decimal, rate: Decimal):
        new_credit = Credit(credit_amount=amount, period_of_credit=period, interest_rate=rate)

        profit, per_month, to_be_returned = new_credit.calculate_needed_info()

        self.credits_made.update({len(self.credits_made.keys()): [new_credit.credit_amount.quantize((Decimal('0.00'))),
                                                                  new_credit.period_of_credit.quantize((Decimal('0.00'))),
                                                                  new_credit.interest_rate.quantize(Decimal('0.00')),
                                                                  profit, to_be_returned, per_month]})

        self._balance += new_credit.credit_amount

    def __iter__(self):
        self._array_with_attributes = [self.account_number, self.account_owner, self.balance, self.type_of_account, self.location_account]
        self._length_of_attributes = 0
        return self

    def __next__(self):
        if self._length_of_attributes < len(self._array_with_attributes):
            result = self._array_with_attributes[self._length_of_attributes]
            self._length_of_attributes += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        return f"account_number: {self.account_number}, account_owner: {self.account_owner}," \
               f" balance: {self.balance:,}, currency: {self.currency}, type_of_account: {self.type_of_account}," \
               f" location_account: {self.location_account}"

    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'

