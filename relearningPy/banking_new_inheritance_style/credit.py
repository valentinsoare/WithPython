#!/usr/bin/python

from re import match
from decimal import Decimal


class Credit:
    def __init__(self, account_for_credit, credit_amount, period_of_credit, interest_rate):
        self.account_for_credit = account_for_credit
        self.credit_amount = credit_amount
        self.period_of_credit = period_of_credit
        self.interest_rate = interest_rate
        self._bank_profit = None
        self._value_to_be_returned = None
        self._how_much_per_month = None

    @property
    def account_for_credit(self):
        return self._account_for_credit

    @account_for_credit.setter
    def account_for_credit(self, account_number):
        if not (isinstance(account_number, str) or account_number.isalnum()) or account_number == '' or match(r'\s+', account_number):
            raise ValueError('Account number should be a string with alpha numerical characters!')

        self._account_for_credit = account_number

    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount: Decimal):
        if not isinstance(credit_amount, Decimal) or credit_amount <= Decimal('0.00'):
            raise ValueError('Credit amount should be a decimal value and greater than zero.')

        self._credit_amount = credit_amount

    @property
    def period_of_credit(self):
        return self._period_of_credit

    @period_of_credit.setter
    def period_of_credit(self, how_many_months):
        if not isinstance(how_many_months, Decimal) or how_many_months <= 0:
            raise ValueError('Period of credit should be a decimal value and greater than zero!')

        self._period_of_credit = how_many_months

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_amount: Decimal):
        if not isinstance(interest_amount, Decimal) or interest_amount <= Decimal(0.00) or interest_amount > Decimal(
                100.00):
            raise ValueError('Interest rate should be a decimal between 0 and 100!')

        self._interest_rate = interest_amount

    @property
    def bank_profit(self):
        return self._bank_profit

    @bank_profit.setter
    def bank_profit(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Bank profit should be a decimal and greater than zero!')

        self._bank_profit = amount

    @property
    def value_to_be_returned(self):
        return self._value_to_be_returned

    @value_to_be_returned.setter
    def value_to_be_returned(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00') or amount < self.credit_amount:
            raise ValueError('credit + interest should be a decimal value greater than the credit that was taken!')

        self._value_to_be_returned = amount

    @property
    def how_much_per_month(self):
        return self._how_much_per_month

    @how_much_per_month.setter
    def how_much_per_month(self, amount: Decimal):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('How much we pay per month should be a decimal value greater than zero!')

        self._how_much_per_month = amount

    def calculate_needed_info(self):
        profit_for_credit = (self.credit_amount * self.interest_rate * self.period_of_credit) / 100
        self.bank_profit = profit_for_credit

        self.value_to_be_returned = self.bank_profit + self.credit_amount
        self.how_much_per_month = Decimal((self.value_to_be_returned / self.period_of_credit)).quantize(Decimal('0.00'))

        return self.bank_profit.quantize(Decimal('0.00')), self.how_much_per_month.quantize(
            Decimal('0.00')), self.value_to_be_returned.quantize(Decimal('0.00'))

    def __str__(self):
        return f'account_for_credit: {self.account_for_credit}\n' \
               f'credit_amount: {self.credit_amount}\n' \
               f'period_of_credit: {self.period_of_credit}\n' \
               f'interest_rate: {self.interest_rate}\n' \
               f'bank_profit: {self.bank_profit}\n' \
               f'value_to_be_returned: {self.value_to_be_returned}\n' \
               f'how_much_per_month: {self.how_much_per_month}'
