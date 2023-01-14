#!/usr/bin/python


import operator
from re import match
from time import time
from credit import Credit
from decimal import Decimal
from random import randrange
from numpy.random import randint, seed
from salaryAccount import SalaryAccount
from savingsAccount import SavingsAccount
from checkingAccount import CheckingAccount



class Bank:
    def __init__(self, bank_name, country, city, type_of_bank):
        self.bank_name: str = bank_name
        self.country: str = country
        self.city: str = city
        self.type_of_bank: str = type_of_bank
        self._accounts: dict = {}
        self._accounts_as_objects: dict = {}
        self._credits_made: dict = {}
        self._credits_as_objects: dict = {}

    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        check_str_input(bank_name, 'Name of the bank')
        self._bank_name = bank_name.capitalize()

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        check_str_input(country, 'Country')
        self._country = country.capitalize()

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        check_str_input(city, 'City')
        self._city = city.capitalize()

    @property
    def type_of_bank(self):
        return self._type_of_bank

    @type_of_bank.setter
    def type_of_bank(self, type_of_bank):
        check_str_input(type_of_bank, 'Type_of_bank')
        self._type_of_bank = type_of_bank

    @property
    def accounts(self):
        return self._accounts

    @property
    def accounts_as_objects(self):
        return self._accounts_as_objects

    @property
    def credits_made(self):
        return self._credits_made

    @property
    def credits_as_objects(self):
        return self._credits_as_objects

    def open_account(self, type_of_account, owner, initial_balance, account_currency, interest_rate=None, fee_for_transaction_checking=None,
                     transaction_fees_salary=None, commissions_type_salary=None, commissions_amount_salary=None, card_withdraw_fees=None,
                     annual_fees=None):
        while True:
            new_account_nr = _generate_new_account_number(name_of_bank=self._bank_name, country_of_bank=self._country, city_of_bank=self._city)

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
                    self._accounts_as_objects.update({new_account_nr: new_account})

                elif type_of_account == 'checking account':
                    new_account = CheckingAccount(nr_account=new_account_nr, owner=owner, balance=initial_balance,
                                                  currency=account_currency, transaction_fee=fee_for_transaction_checking)
                    self._accounts.update({new_account_nr: {'account_number': new_account_nr,
                                                            'owner': owner,
                                                            'type_of_account': 'checking_account',
                                                            'initial_balance': initial_balance,
                                                            'account_currency': account_currency,
                                                            'transaction_fee': fee_for_transaction_checking}})
                    self._accounts_as_objects.update({new_account_nr: new_account})
                elif type_of_account == 'salary account':
                    new_account = SalaryAccount(account_number=new_account_nr, owner=owner, balance=initial_balance,
                                                currency=account_currency, transaction_fees=transaction_fees_salary,
                                                type_of_commissions=commissions_type_salary, commission_amount=commissions_amount_salary,
                                                credit_card_withdraw_fees=card_withdraw_fees, annual_maintenance_fees=annual_fees)
                    self._accounts.update({new_account_nr: {'account_number': new_account_nr,
                                                            'owner': owner,
                                                            'type_of_account': 'salary_account',
                                                            'initial_balance': initial_balance,
                                                            'account_currency': account_currency,
                                                            'transaction_fees': transaction_fees_salary,
                                                            'type_of_commissions': commissions_type_salary,
                                                            'commissions_amount': commissions_amount_salary,
                                                            'card_withdraw_fees': card_withdraw_fees,
                                                            'annual_maintenance_fees': annual_fees}})
                    self._accounts_as_objects.update({new_account_nr: new_account})

                return new_account

    def search_credits_by_owner(self, number_account=None, owner_account=None, account_type=None, balance_initial=None,
                                currency_on_account=None, fee_transaction=None, interest_rate_on_account=None):

        credits_to_returned: dict = {}
        value_to_search_by = self.search_account(account_number=number_account, owner=owner_account, type_of_account=account_type,
                                                 initial_balance=balance_initial, account_currency=currency_on_account,
                                                 interest_rate=interest_rate_on_account, transaction_fee=fee_transaction)
        if not value_to_search_by:
            return None

        for i in value_to_search_by.keys():
            credits_to_returned.update({k: l for k, l in self.credits_made.items() if i == l['account_number']})

        return credits_to_returned

    #def search_credits_by_values(self, amount=None, period=None, rate=None,
                                 #bank_profit=None, value_to_be_returned=None, per_month=None):


    def number_of_accounts_open(self, number_account=None, owner_account=None, account_type=None, balance=None, currency=None, rate=None, fee_for_transaction=None):

        value_to_return = self.search_account(account_number=number_account, owner=owner_account, type_of_account=account_type, initial_balance=balance,
                                              account_currency=currency, interest_rate=rate, transaction_fee=fee_for_transaction)

        if value_to_return:
            return len(value_to_return)
        else:
            return len(self.accounts.keys())

    def search_account(self, account_number=None, owner=None, type_of_account=None, initial_balance=None,
                       account_currency=None, interest_rate=None, transaction_fee=None):

        search_options: set = {(account_number, 'account_number'), (owner, 'owner'), (type_of_account, "type_of_account"), (initial_balance, "initial_balance"),
                               (account_currency, "account_currency"), (interest_rate, "interest_rate"), (transaction_fee, 'transaction_fee')}

        arguments_given = {(i, j) for i, j in search_options if i}
        number_of_arguments_given: int = len(arguments_given)
        values_found: dict = {}

        for i, j in self._accounts.items():
            count: int = 0
            for k, l in arguments_given:
                if j[l] == k:
                    count += 1
                if number_of_arguments_given == count:
                    values_found.update({i: j})

        return None if not values_found else values_found

    def credit(self, account_number: str, amount: Decimal, period: Decimal, rate: Decimal):
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
        self._accounts_as_objects[account_number].deposit(new_credit.credit_amount)

    def search_credits(self, credit_amount=None, period_of_credit=None, interest_rate=None, bank_profit=None
                       , value_to_be_returned=None, how_much_per_month=None):
        credits_found: dict = {}
        comparison_operators = {'>': operator.gt,
                                '<': operator.lt,
                                '>=': operator.ge,
                                '<=': operator.le,
                                '==': operator.eq,
                                '!=': operator.ne}

        arguments_to_search: set = {(credit_amount, 'credit_amount'), (period_of_credit, 'credit_period',),
                                    (interest_rate, 'credit_interest_rate'), (bank_profit, 'bank_profit'),
                                    (value_to_be_returned, 'money_to_be_returned'), (how_much_per_month, 'payment_per_month')}

        arguments_we_have: set = {(i, j) for i, j in arguments_to_search if i}
        number_of_arguments_given = len(arguments_we_have)

        for i, j in self.credits_made.items():
            count: int = 0
            for k, l in arguments_we_have:
                operator_to_use, amount_to_compare = k.split()
                #if comparison_operators[operator_to_use](getattr(j, l), Decimal(amount_to_compare)):
                #    count += 1

                if comparison_operators[operator_to_use](j[l], Decimal(amount_to_compare)):
                    count += 1

                if count == number_of_arguments_given:
                    credits_found.update({i: j})

        return None if not credits_found else credits_found

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
    return ''.join([*account_number, city_of_bank[0].upper(), str(randrange(100000000, 999999999))])


def check_str_input(given_value, type_of_input: str):
    if not (given_value and isinstance(given_value, str)) or match(r'\s+', given_value):
        raise ValueError(f'{type_of_input} input should be a string containing alpha characters.')
