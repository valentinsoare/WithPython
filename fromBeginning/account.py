#!/usre/bin/python

import csv
import json
from decimal import Decimal
from typing import List, Dict, Tuple, Union


class Account:
    def __init__(self, account_number: Decimal, customer_name: str, balance:
                 Decimal = Decimal('0.00'), type_of_customer: str = 'self service', location_city: str = 'Bucharest'):
        if balance < 0:
            raise ValueError('Initial balance must be greater or equal to zero!')

        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = balance
        self._type_of_customer = type_of_customer
        self._location_city = location_city

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, number_of_the_account):
        if type(number_of_the_account) is not Decimal:
            raise ValueError('You need to use a Decimal value for the account number also.')
        elif number_of_the_account <= Decimal('0.00'):
            raise ValueError('Account number must be greater than zero!')

        self._account_number = number_of_the_account

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, name_of_customer: str):
        customer_name = name_of_customer.strip()

        if not customer_name.isascii():
            raise ValueError('Please input here the customer name which will be the owner of the account.')

        self._customer_name = customer_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: Decimal):
        if balance < Decimal('0.00'):
            raise ValueError('When settings balance value you need to have a value equal or greater than zero!')

        self._balance = balance

    @property
    def type_of_customer(self):
        return self._type_of_customer

    @property
    def location_city(self):
        return self._location_city

    def deposit(self, amount: Decimal):
        if amount < Decimal('0.00'):
            raise ValueError('Deposit amount must pe a positive value!')

        self.balance += amount

    def withdraw(self, amount: Decimal):
        if amount < Decimal('0.00'):
            raise ValueError('Withdraw amount must be greater than or equal to zero.')
        elif amount > self.balance:
            raise ValueError('Withdraw amount must not be greater than the account balance.')

        self.balance -= amount