#!/usr/bin/python


from re import match
from numpy import random
from decimal import Decimal
from account import Account
from typing import List, Dict, Tuple, Union


def _account_number_generator(accounts, name_of_the_bank: str, country: str, city: str):
    account_pattern: str = ''

    while True:
        nr_gen = random.randint(1, 2**32, 1, dtype=int)
        for i in range(nr_gen.size):
            account_pattern += f'{country[0:2].upper()}{name_of_the_bank[0:2].upper()}{city[0].upper()}{nr_gen[i]}'
            if account_pattern not in accounts.keys():
                return account_pattern


def validate_variable_string(given_value: str):
    if not isinstance(given_value, str) or given_value == '' or match(r'\s+', given_value):
        raise ValueError('Name of the bank should be a string with letters/digits!')


class Bank:
    def __init__(self, country: str, city: str, type_of_bank: str,
                 name_of_bank: str, social_capital):
        self.country = country
        self.city = city
        self.type_of_bank = type_of_bank
        self.name_of_bank = name_of_bank
        self.social_capital = social_capital
        self.accounts: Dict = {}

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, name_of_country: str):
        validate_variable_string(name_of_country)
        self._country = name_of_country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, name_of_city: str):
        validate_variable_string(name_of_city)
        self._city = name_of_city

    @property
    def type_of_bank(self):
        return self._type_of_bank

    @type_of_bank.setter
    def type_of_bank(self, bank_type: str):
        validate_variable_string(bank_type)
        self._type_of_bank = bank_type

    @property
    def social_capital(self):
        return self._social_capital

    @social_capital.setter
    def social_capital(self, social_value: Decimal):
        if social_value:
            if not isinstance(social_value, Decimal) or social_value <= Decimal('0.00'):
                raise ValueError('Social capital must be greater than zero.')

        self._social_capital = social_value

    @property
    def name_of_bank(self):
        return self._name_of_bank

    @name_of_bank.setter
    def name_of_bank(self, bank_name: str):
        validate_variable_string(bank_name)
        self._name_of_bank = bank_name

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts: Dict):
        if not isinstance(accounts, Dict):
            raise ValueError('When assigned an account please use a dictionary will all the key: value pair.')

        self._accounts = accounts

    def create_account(self, owner_of_the_account: str, account_currency: str, given_balance=Decimal('0.00'), account_type='serlfservice'):
        number_for_the_account = _account_number_generator(self.accounts, self.name_of_bank, self.country, self.city)

        new_account = Account(account_number=number_for_the_account, account_owner=owner_of_the_account, currency=account_currency,
                              balance=given_balance, type_of_account=account_type, location_account=self.city)

        account: list = str(new_account).split(', ')
        to_add_into_list_account: Dict = {}

        for i in account:
            j = i.split(': ')
            to_add_into_list_account[j[0]] = j[1]

        self.accounts.update({to_add_into_list_account['account_number']: to_add_into_list_account})
        return new_account

    def search_account(self, name: str = None, number: int = None, balance: Decimal = None,
                       currency: str = None, type_of_account: str = None, location: str = None):
        list_with_vars_for_search = [(name, "name"), (number, "number"), (balance, "balance"),
                                     (type_of_account, "type_of_account"), (location, "location"), (currency, "currency")]

        for i, j in list_with_vars_for_search:
            if i:
                for k, l in self.accounts.items():
                    if l[j] == i:
                        yield l




