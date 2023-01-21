#!/usr/bin/python


import operator
from re import match
from time import time
from typing import Union
from credit import Credit
from decimal import Decimal
from random import randrange
from functools import partial
from creditCard import CreditCard
from numpy.random import randint, seed
from salaryAccount import SalaryAccount
from savingsAccount import SavingsAccount
from checkingAccount import CheckingAccount


class Bank:
    _COMPARISON_OPERATORS = {'>': operator.gt, '<': operator.lt, '>=': operator.ge,
                             '<=': operator.le, '==': operator.eq, '!=': operator.ne}

    def __init__(self, *, bank_name, country, city, type_of_bank):
        self.bank_name: str = bank_name
        self.country: str = country
        self.city: str = city
        self.type_of_bank: str = type_of_bank
        self._accounts: dict = {}
        self._accounts_as_objects: dict = {}
        self._credits_made: dict = {}
        self._credits_as_objects: dict = {}
        self._credit_cards: dict = {}
        self._credit_cards_as_objects: dict = {}

    @property
    def bank_name(self) -> str:
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name: str):
        check_str_input(given_value=bank_name, type_of_input='Name of the bank')
        self._bank_name = bank_name.capitalize()

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str):
        check_str_input(given_value=country, type_of_input='Country')
        self._country = country.capitalize()

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        check_str_input(given_value=city, type_of_input='City')
        self._city = city.capitalize()

    @property
    def type_of_bank(self) -> str:
        return self._type_of_bank

    @type_of_bank.setter
    def type_of_bank(self, type_of_bank: str):
        check_str_input(given_value=type_of_bank, type_of_input='Type_of_bank')
        self._type_of_bank = type_of_bank

    @property
    def accounts(self) -> dict:
        return self._accounts

    @property
    def accounts_as_objects(self) -> dict:
        return self._accounts_as_objects

    @property
    def credits_made(self) -> dict:
        return self._credits_made

    @property
    def credits_as_objects(self) -> dict:
        return self._credits_as_objects

    @property
    def credit_cards(self) -> dict:
        return self._credit_cards

    @property
    def credit_cards_as_objects(self) -> dict:
        return self._credit_cards_as_objects

    def open_savings_account(self, owner, balance, currency, interest_rate, owner_address):
        return self._open_account(owner=owner, balance=balance, currency=currency, interest_rate=interest_rate,
                                  owner_address=owner_address, account_type='savings_account')

    def open_checking_account(self, owner, balance, currency, transaction_fee, owner_address):
        return self._open_account(owner=owner, balance=balance, currency=currency,
                                  transaction_fee=transaction_fee, owner_address=owner_address, account_type='checking_account')

    def open_salary_account(self, owner, balance, currency, transaction_salary_fees, type_of_commission, commission_amount,
                            credit_card_withdraw_fees, annual_maintenance_fees, owner_address):
        opening = partial(self._open_account, account_type='salary_account')

        return opening(owner=owner, balance=balance, currency=currency, transaction_salary_fees=transaction_salary_fees,
                       type_of_commission=type_of_commission, commission_amount=commission_amount,
                       credit_card_withdraw_fees=credit_card_withdraw_fees, annual_maintenance_fees=annual_maintenance_fees,
                       owner_address=owner_address)

    def _open_account(self, *, account_type: str, owner: str, balance: Decimal, currency: str, owner_address: str, interest_rate: Decimal = Decimal('0.00'),
                      transaction_fee: Decimal = Decimal('0.00'), transaction_salary_fees: Decimal = Decimal('0.00'), type_of_commission: str = 'monthly',
                      commission_amount: Decimal = Decimal('0.00'), credit_card_withdraw_fees: Decimal = Decimal('0.00'), annual_maintenance_fees = Decimal('0.00')) -> Union[SavingsAccount, CheckingAccount, SalaryAccount]:

        while True:
            new_account_nr = _generate_new_account_number(name_of_bank=self._bank_name, country_of_bank=self._country, city_of_bank=self._city)

            if new_account_nr not in self.accounts.keys():
                if account_type == 'savings_account':
                    new_account = SavingsAccount(account_number=new_account_nr, owner=owner, balance=balance,
                                                 currency=currency, interest_rate=interest_rate, owner_address=owner_address)
                    self._accounts.update({new_account_nr: {'account_number': new_account_nr,
                                                            'owner': owner,
                                                            'account_type': account_type,
                                                            'balance': balance,
                                                            'currency': currency,
                                                            'interest_rate': interest_rate,
                                                            'owner_address': owner_address}})
                    self._accounts_as_objects.update({new_account_nr: new_account})
                elif account_type == 'checking_account':
                    new_account = CheckingAccount(account_number=new_account_nr, owner=owner, balance=balance,
                                                  currency=currency, transaction_fee=transaction_fee,
                                                  owner_address=owner_address)
                    self._accounts.update({new_account_nr: {'account_number': new_account_nr,
                                                            'owner': owner,
                                                            'type_of_account': account_type,
                                                            'balance': balance,
                                                            'account_currency': currency,
                                                            'transaction_fee': transaction_fee,
                                                            'owner_address': owner_address}})
                    self._accounts_as_objects.update({new_account_nr: new_account})
                elif account_type == 'salary_account':
                    new_account = SalaryAccount(account_number=new_account_nr, owner=owner, balance=balance,
                                                currency=currency, transaction_salary_fees=transaction_salary_fees,
                                                type_of_commission=type_of_commission, commission_amount=commission_amount,
                                                credit_card_withdraw_fees=credit_card_withdraw_fees, annual_maintenance_fees=annual_maintenance_fees, owner_address=owner_address)
                    self._accounts.update({new_account_nr: {'account_number': new_account_nr,
                                                            'owner': owner,
                                                            'type_of_account': account_type,
                                                            'balance': balance,
                                                            'currency': currency,
                                                            'transaction_salary_fees': transaction_salary_fees,
                                                            'type_of_commission': type_of_commission,
                                                            'commission_amount': commission_amount,
                                                            'credit_card_withdraw_fees': credit_card_withdraw_fees,
                                                            'annual_maintenance_fees': annual_maintenance_fees,
                                                            'owner_address': owner_address}})
                    self._accounts_as_objects.update({new_account_nr: new_account})

                return new_account

    def search_credits_by_owner(self, *, number_account: str = None, owner_account: str = None, account_type: str = None,
                                currency_on_account: str = None) -> Union[dict, None]:

        credits_to_returned: dict = {}
        value_to_search_by = self.search_account(account_number=number_account, owner=owner_account, type_of_account=account_type,
                                                 account_currency=currency_on_account)

        if not value_to_search_by:
            return None

        for i in value_to_search_by.keys():
            credits_to_returned.update({k: l for k, l in self.credits_made.items() if i == l['account_number']})

        return credits_to_returned

    def search_account(self, *, account_number=None, owner=None, type_of_account=None, account_currency=None) -> Union[dict, None]:

        search_options: set = {(account_number, 'account_number'), (owner, 'owner'), (type_of_account, "type_of_account"),
                               (account_currency, "account_currency")}

        arguments_given: set = {(i, j) for i, j in search_options if i}
        number_of_arguments_given: int = len(arguments_given)
        values_found: dict = {}

        for i, j in self._accounts.items():
            count: int = 0
            for k, l in arguments_given:
                if l in j and j[l] == k:
                    count += 1
                if number_of_arguments_given == count:
                    values_found.update({i: j})

        return None if not values_found else values_found

    def search_account_numerical_values(self, *, initial_balance=None, interest_rate=None, transaction_fee=None) -> Union[dict, None]:

        search_options: set = {(initial_balance, "initial_balance"), (interest_rate, "interest_rate"), (transaction_fee, 'transaction_fee')}

        parse_args_given = {(i, j) for i, j in search_options if i}
        nr_args = len(parse_args_given)
        found_values: dict = {}

        for i, j in self.accounts.items():
            count: int = 0
            for k, l in parse_args_given:
                operator_to_use, compare_amount = k.split()

                if l in j and self._COMPARISON_OPERATORS[operator_to_use](j[l], Decimal(compare_amount)):
                    count += 1

                if count == nr_args:
                    found_values.update({i: j})

        return None if not found_values else found_values

    def credit(self, *, account_number: str, amount: Decimal, period: Decimal, rate: Decimal) -> Credit:
        new_credit = Credit(account_for_credit=account_number, credit_amount=amount,
                            period_of_credit=period, interest_rate=rate)

        profit, per_month, to_be_returned = new_credit.calculate_needed_info()

        self.credits_made.update({len(self.credits_made.keys()): {'account_number': new_credit.account_for_credit,
                                                                  'credit_amount': new_credit.credit_amount.quantize((Decimal('0.00'))),
                                                                  'credit_period' : new_credit.period_of_credit.quantize((Decimal('0.00'))),
                                                                  'credit_interest_rate': new_credit.interest_rate.quantize(Decimal('0.00')),
                                                                  'bank_profit': profit,
                                                                  'money_to_be_returned': to_be_returned,
                                                                  'payment_per_month': per_month}})

        self._credits_as_objects.update({len(self.credits_as_objects.keys()): new_credit})
        self._accounts_as_objects[account_number].deposit(amount=new_credit.credit_amount)
        return new_credit

    def create_credit_card(self, account_number, owner, balance, currency, credit_card_withdraw_fees, annual_maintenance_fees, card_type,
                           type_of_commissions, commission_amount, transaction_fees, serial_number, expiration_date, **kwargs) -> CreditCard:
        new_credit_card = CreditCard(account_number=account_number,
                                     owner=owner,
                                     balance=balance,
                                     currency=currency,
                                     credit_card_withdraw_fees=credit_card_withdraw_fees,
                                     annual_maintenance_fees=annual_maintenance_fees,
                                     type_of_card=card_type,
                                     type_of_commissions=type_of_commissions,
                                     commission_amount=commission_amount,
                                     transaction_fees=transaction_fees,
                                     serial_number=serial_number,
                                     expiration_date=expiration_date,
                                     cvv=kwargs['cvv'],
                                     address=kwargs['address'])
        self._credit_cards.update({account_number: {(len(self._credit_cards) + 1): {'account_number': account_number, 'owner': owner,
                                                                                    'balance': balance, 'currency': currency,
                                                                                    'credit_card_withdraw_fees': credit_card_withdraw_fees,
                                                                                    'annual_maintenance_fees': annual_maintenance_fees,
                                                                                    'type_of_card': card_type,
                                                                                    'type_of_commissions': type_of_commissions,
                                                                                    'commission_amount': commission_amount,
                                                                                    'transaction_fees': transaction_fees,
                                                                                    'serial_number': serial_number,
                                                                                    'expiration_date': expiration_date,
                                                                                    'cvv': kwargs['cvv'],
                                                                                    'address': kwargs['address']}}})
        self._credit_cards_as_objects.update({new_credit_card.account_number: {(len(self._credit_cards_as_objects) + 1): new_credit_card}})
        return new_credit_card

    def search_credits(self, *, credit_amount=None, period_of_credit=None, interest_rate=None, bank_profit=None,
                       value_to_be_returned=None, how_much_per_month=None) -> Union[None, dict]:
        credits_found: dict = {}

        arguments_to_search: set = {(credit_amount, 'credit_amount'), (period_of_credit, 'credit_period',),
                                    (interest_rate, 'credit_interest_rate'), (bank_profit, 'bank_profit'),
                                    (value_to_be_returned, 'money_to_be_returned'), (how_much_per_month, 'payment_per_month')}

        arguments_we_have: set = set((i, j) for i, j in arguments_to_search if i)
        number_of_arguments_given = len(arguments_we_have)

        for i, j in self.credits_made.items():
            count: int = 0
            for k, l in arguments_we_have:
                operator_to_use, amount_to_compare = k.split()

                if self._COMPARISON_OPERATORS[operator_to_use](j[l], Decimal(amount_to_compare)):
                    count += 1

                if count == number_of_arguments_given:
                    credits_found.update({i: j})

        return None if not credits_found else credits_found

    def __str__(self):
        return f'bank_name: {self.bank_name}\n' \
               f'country: {self.country}\n' \
               f'city: {self.city}\n' \
               f'type_of_bank: {self.type_of_bank}'


def _generate_new_account_number(*, name_of_bank: str, country_of_bank: str, city_of_bank: str) -> str:
    account_number: list = [country_of_bank.upper()[0:2], '01']

    if len(name_of_bank) <= 3:
        account_number.append(name_of_bank.upper())
    else:
        length_name_of_bank: int = len(name_of_bank)
        seed(length_name_of_bank)

        random_indexes_sorted: list = sorted(randint(0, length_name_of_bank, 3))
        for index in random_indexes_sorted:
            account_number.append(name_of_bank[index].upper())

    seed(int(time()))
    return ''.join([*account_number, city_of_bank[0].upper(), str(randrange(100000000, 999999999))])


def check_str_input(*, given_value: str, type_of_input: str) -> None:
    if not (given_value and isinstance(given_value, str)) or match(r'\s+', given_value):
        raise ValueError(f'{type_of_input} input should be a string containing alpha characters.')
