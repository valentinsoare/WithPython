#!/usr/bin/python

import decimal


def interest_rate_validation(given_interest):
    if given_interest <= 0:
        raise ValueError('Interest rate should be greater than zero.')
    else:
        given_interest = decimal.Decimal(given_interest)
        return given_interest


def name_validation(given_name):
    if given_name.lstrip('-+').isdigit():
        raise ValueError('Error you need to have alpha numerical characters for name.')
    else:
        return given_name


def determine_account_type(type_of_account):
    chooser = ['basic', 'silver', 'gold', 'platinum']

    if type_of_account not in chooser:
        raise ValueError("Error account type doesn't exists.")
    else:
        return type_of_account


class Account:
    def __init__(self, name, account_type, balance):

        self._name = name_validation(name)

        if balance < 0:
            raise ValueError('Balance needs to be greater or equal to zero.')
        else:
            self._balance = decimal.Decimal(balance)

        self._account_type = determine_account_type(account_type)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_of_owner):
        self._name = name_validation(name_of_owner)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount_balance):
        if amount_balance >= 0:
            self._balance = decimal.Decimal(amount_balance)
        else:
            raise ValueError('Balance value must be greater than or equal to 0.')

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, type_of_account):
        self._account_type = determine_account_type(type_of_account)

    def withdraw(self, amount):
        amount = decimal.Decimal(amount)

        if amount > self.balance:
            raise ValueError(f'You cannot withdraw more money that you have in your bank account.')
        elif amount < 0:
            return ValueError(f'Withdraw amount should be zero or greater.')
        else:
            self.balance = self.balance - amount

    def deposit(self, amount):
        amount = decimal.Decimal(amount)
        if amount < 0:
            raise ValueError('Deposit amount should be zero or greater than zero, not a negative amount')
        else:
            self.balance = self.balance + amount

    def __str__(self):
        var_to_return = f'{self.name.title()}, {self._account_type.title()}, {self.balance}'
        return var_to_return

    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'


class SavingsAccount(Account):
    def __init__(self, name, account_type, balance, interest_rate):
        super().__init__(name, account_type, balance)
        self._interest_rate = interest_rate_validation(interest_rate)

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, amount):
        amount = interest_rate_validation(amount)
        self._interest_rate = amount

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def __str__(self):
        return f'{super().__str__()}, {self.interest_rate}%'

    def __format__(self, format_spec):
        return f'{str(super().__str__()), self.interest_rate}: {format_spec}'


def main():
    andreea_account = Account('Andreea', 'silver', 800)
    monica_account = SavingsAccount('Monica', 'gold', 600, 0.25)

    print(monica_account)

    
if __name__ == '__main__':
    main()
