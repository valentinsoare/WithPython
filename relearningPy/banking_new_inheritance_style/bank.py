#!/usr/bin/python


from re import match
from time import time
from random import randrange
from numpy.random import randint, seed
from savingsAccount import SavingsAccount
from checkingAccount import CheckingAccount


class Bank:
    def __init__(self, bank_name, country, city, type_of_bank):
        self.bank_name: str = bank_name
        self.country: str = country
        self.city: str = city
        self.type_of_bank: str = type_of_bank
        self._accounts: dict = {}
        self._accounts_as_objects: set = set()

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

    @property
    def accounts(self):
        return self._accounts

    @property
    def accounts_as_objects(self):
        return self._accounts_as_objects

    def open_account(self, type_of_account, owner, initial_balance, account_currency, interest_rate=None, fee_for_transaction=None):
        while True:
            new_account_nr = _generate_new_account_number(name_of_bank=self._bank_name, country_of_bank=self._country,
                                                          city_of_bank=self._city)

            if new_account_nr not in self.accounts.keys():
                if type_of_account == 'savings account':
                    new_account = SavingsAccount(nr_of_the_account=new_account_nr, owner_of_the_account=owner, account_balance=initial_balance,
                                                 currency_for_account=account_currency, interest_rate=interest_rate)
                    self._accounts.update({new_account_nr: {'account_number': new_account_nr,
                                                            'owner': owner,
                                                            'type_of_account': 'savings_account',
                                                            'initial_balance': initial_balance,
                                                            'account_currency': account_currency,
                                                            'interest_rate': interest_rate}})
                    self._accounts_as_objects.update({new_account})

                elif type_of_account == 'checking account':
                    new_account = CheckingAccount(nr_account=new_account_nr, owner=owner, balance=initial_balance,
                                                  currency=account_currency, transaction_fee=fee_for_transaction)
                    self._accounts.update({new_account_nr: {'account_number': new_account_nr,
                                                            'owner': owner,
                                                            'type_of_account': 'checking_account',
                                                            'initial_balance': initial_balance,
                                                            'account_currency': account_currency,
                                                            'transaction_fee': fee_for_transaction}})
                    self._accounts_as_objects.update({new_account})

                return new_account

    def number_of_accounts_open(self):
        return len(self.accounts.keys())

    def search_account(self, account_number=None, owner=None, type_of_account=None, initial_balance=None,
                       account_currency=None, interest_rate=None, transaction_fee=None, search_arguments_number: int = 1):

        search_options: set = {(account_number, 'account_number'), (owner, 'owner'), (type_of_account, "type_of_account"), (initial_balance, "initial_balance"),
                               (account_currency, "account_currency"), (interest_rate, "interest_rate"), (transaction_fee, 'transaction_fee')}
        values_found: dict = {}
        items_to_search: dict = self._accounts

        for i, j in search_options:
            if i:
                for k, l in items_to_search.items():
                    if l[j] == i:
                        values_found.update({k: l})
                search_arguments_number -= 1
                if search_arguments_number == 0:
                    break
                else:
                    items_to_search = values_found
                    values_found.clear()

        return None if len(values_found.keys()) == 0 else values_found

    def __str__(self):
        return f'bank_name: {self.bank_name}\n' \
               f'country: {self.country}\n' \
               f'city: {self.city}\n' \
               f'type_of_bank: {self.type_of_bank}'


def _generate_new_account_number(name_of_bank: str, country_of_bank: str, city_of_bank: str):
    account_number: list = [country_of_bank.upper()[0:2], '01']

    if len(name_of_bank) <= 3:
        account_number.append(name_of_bank.upper())
    else:
        length_name_of_bank = len(name_of_bank)
        seed(length_name_of_bank)

        random_indexes_sorted = sorted(randint(0, length_name_of_bank, 3))
        for index in random_indexes_sorted:
            account_number.append(name_of_bank[index].upper())

    seed(int(time()))
    return ''.join([*account_number, city_of_bank[0].upper(), str(randrange(1000000000, 9999999999))])


def check_str_input(given_value, type_of_input: str):
    if not isinstance(given_value, str) or given_value == '' or match(r'\s+', given_value):
        raise ValueError(f'{type_of_input.capitalize()} input should be a string containing alpha characters.')
