#!/usr/bin/python

from re import match
from savingsAccount import SavingsAccount
from checkingAccount import CheckingAccount


def check_str_input(given_value, type_of_input: str):
    if not isinstance(given_value, str) or given_value == '' or match(r'\s+', given_value):
        raise ValueError(f'{type_of_input.capitalize()} input should be a string containing alpha characters.')


class Bank:
    def __init__(self, bank_name, country, city, type_of_bank):
        self.bank_name: str = bank_name
        self.country: str = country
        self.city: str = city
        self.type_of_bank: str = type_of_bank
        self._accounts_opened: dict = {}

    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        check_str_input(bank_name, 'name of the bank')
        self._bank_name = bank_name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        check_str_input(country, 'country')
        self._country = country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        check_str_input(city, 'city')
        self._city = city

    @property
    def type_of_bank(self):
        return self._type_of_bank

    @type_of_bank.setter
    def type_of_bank(self, type_of_bank):
        check_str_input(type_of_bank, 'type_of_bank')
        self._type_of_bank = type_of_bank

    def open_account(self, type_of_account, owner, initial_balance, account_currency, interest_rate=None, fee_for_transaction=None):
        if type_of_account == 'savings account':
            return SavingsAccount(owner_of_the_account=owner, account_balance=initial_balance,
                                  currency_for_account=account_currency, interest_rate=interest_rate)
        elif type_of_account == 'checking account':
            return CheckingAccount(owner=owner, balance=initial_balance,
                                   currency=account_currency, transaction_fee=fee_for_transaction)

    def __str__(self):
        return f'bank_name: {self.bank_name}\n' \
               f'country: {self.country}\n' \
               f'city: {self.city}\n' \
               f'type_of_bank: {self.type_of_bank}'
