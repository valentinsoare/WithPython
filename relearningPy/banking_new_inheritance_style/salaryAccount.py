#!/usr/bin/python

from decimal import Decimal
from account import Account


class SalaryAccount(Account):
    def __init__(self, account_number, owner, balance, currency, type_of_commissions,
                 commission_amount, credit_card_withdraw_fees, annual_maintenance_fees, transaction_fees):
        super().__init__(account_number, owner, balance, currency)

        self.type_of_commissions = type_of_commissions
        self.commission_amount = commission_amount
        self.credit_card_withdraw_fees = credit_card_withdraw_fees
        self.annual_maintenance_fees = annual_maintenance_fees
        self.transaction_fees = transaction_fees
        self._registered_salary_for_three_months: list = []

    @property
    def type_of_commissions(self):
        return self._type_of_commissions

    @type_of_commissions.setter
    def type_of_commissions(self, type_of_commissions):
        if not (isinstance(type_of_commissions, str) and type_of_commissions.isalpha()) or \
                type_of_commissions not in ['weekly', 'daily', 'monthly', 'annually']:
            raise ValueError('Commissions type should be a str and one of '
                             'the following type: daily, weekly, monthly or annually!')

        self._type_of_commissions = type_of_commissions

    @property
    def commission_amount(self):
        return self.commission_amount

    @commission_amount.setter
    def commission_amount(self, amount):
        check_decimal_values(amount, 'Commission amount')
        self._commission_amount = amount

    @property
    def credit_card_withdraw_fees(self):
        return self._credit_card_withdraw_fees

    @credit_card_withdraw_fees.setter
    def credit_card_withdraw_fees(self, amount):
        check_decimal_values(amount, 'Credit card withdraw fees')
        self._credit_card_withdraw_fees = amount

    @property
    def annual_maintenance_fees(self):
        return self._annual_maintenance_fees

    @annual_maintenance_fees.setter
    def annual_maintenance_fees(self, amount):
        check_decimal_values(amount, 'Annual maintenance fees')
        self._annual_maintenance_fees = amount

    @property
    def transaction_fees(self):
        return self._transaction_fees

    @transaction_fees.setter
    def transaction_fees(self, amount):
        check_decimal_values(amount, 'Transaction fees')
        self._transaction_fees = amount

    def withdraw(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00') or amount + self.transaction_fees > self.balance:
            raise ValueError('Withdraw value shoud be a decimal grreater or equal to '
                             'zero and not bigger than the current balance!')
        self.balance -= (amount + self.transaction_fees)
        return self.balance

    def deposit(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00') or self.transaction_fees > amount + self.balance:
            raise ValueError('Deposit amount should be a decimal, not less or equal to zero '
                             'and amount of transaction + balance should be greater than transaction fees!')

        calculated: Decimal = (amount - self.transaction_fees)

        if len(self._registered_salary_for_three_months) == 6:
            self._registered_salary_for_three_months.append(calculated)
            self._registered_salary_for_three_months.pop()
        else:
            self._registered_salary_for_three_months.append(calculated)

        self.balance += calculated
    
    def registered_salary_for_three_months(self):
        return self._registered_salary_for_three_months

    def overdraft(self, amount):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Overdraft should be a decimal value greater than zero!')

        overdraft_accepted: Decimal = (amount * sum(self._registered_salary_for_three_months) / Decimal('6')) - self.transaction_fees
        self.balance += overdraft_accepted

        return overdraft_accepted

    def __getattr__(self, item):
        if item in {'transaction_fee', 'interest_rate', 'interest', 'calculate_interest'}:
            raise NotImplementedError
        else:
            return getattr(self, item)


def check_decimal_values(given_value_amount, type_of_variable):
    if not isinstance(given_value_amount, Decimal) or given_value_amount < Decimal('0.00'):
        raise ValueError(f'{type_of_variable} should be a decimal and greater or equal to zero!')