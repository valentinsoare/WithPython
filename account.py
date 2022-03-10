#!/usr/bin/python

from decimal import Decimal


class Account:
    def __init__(self, name, balance):
        self._name = name

        balance = Decimal(balance)

        if balance < 0:
            raise ValueError('Balance needs to be greater or equal to zero.')
        else:
            self._balance = balance

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        var_to_return = f'\033[1mName:\033[0m \033[1;31m{self.name}\033[0m' \
                        f'\n\033[1mBalance:\033[0m \033[1;32m{self.balance}$\033[0m'
        return var_to_return

    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'


if __name__ == '__main__':
    andreea_account = Account('Andreea', 900)
    print(andreea_account)
