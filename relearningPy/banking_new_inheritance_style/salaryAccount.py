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
        return self._commission_amount

    @commission_amount.setter
    def commission_amount(self, amount):
        check_decimal_values(amount, 'Commission amount')
        self._commission_amount = amount.quantize(Decimal("0.00"))

    @property
    def credit_card_withdraw_fees(self):
        return self._credit_card_withdraw_fees

    @credit_card_withdraw_fees.setter
    def credit_card_withdraw_fees(self, amount):
        check_decimal_values(amount, 'Credit card withdraw fees')
        self._credit_card_withdraw_fees = amount.quantize(Decimal('0.00'))

    @property
    def annual_maintenance_fees(self):
        return self._annual_maintenance_fees

    @annual_maintenance_fees.setter
    def annual_maintenance_fees(self, amount):
        check_decimal_values(amount, 'Annual maintenance fees')
        self._annual_maintenance_fees = amount.quantize(Decimal('0.00'))

    @property
    def transaction_fees(self):
        return self._transaction_fees

    @transaction_fees.setter
    def transaction_fees(self, amount):
        check_decimal_values(amount, 'Transaction fees')
        self._transaction_fees = amount.quantize(Decimal('0.00'))

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

        if len(self._registered_salary_for_three_months) == 3:
            self._registered_salary_for_three_months.append(calculated)
            self._registered_salary_for_three_months.pop(0)
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

    def trial_period(self):
        return self.__bool__()

    def __bool__(self):
        return True if len(self._registered_salary_for_three_months) != 3 else False

    def __iter__(self):
        dict_with_properties = {'account_number': self.account_number, 'owner': self.owner, 'balance': self.balance,
                                'currency': self.type_of_commissions, 'commission_amount': self.commission_amount,
                                'credit_card_withdraw_fees': self.credit_card_withdraw_fees, 'annual_maintenance_fees': self.annual_maintenance_fees,
                                'transaction_fees': self.transaction_fees, 'registered_salary_for_three_months': self.registered_salary_for_three_months()}
        return iter(dict_with_properties.items())

    def __getattr__(self, item):
        if item in {'transaction_fee', 'interest_rate', 'interest', 'calculate_interest'}:
            raise NotImplementedError
        else:
            return getattr(self, item)

    def __str__(self):
        return f'account_number: {self.account_number}\n' \
               f'owner: {self.owner}\n' \
               f'balance: {self.balance}\n' \
               f'currency: {self.currency}\n' \
               f'type_of_commissions: {self.type_of_commissions}\n' \
               f'commission_amount: {self.commission_amount}\n' \
               f'credit_card_withdraw_fees: {self.credit_card_withdraw_fees}\n' \
               f'annual_maintenance_fees: {self.annual_maintenance_fees}\n' \
               f'transaction_fees: {self.transaction_fees}\n' \
               f'registered_salary_for_three_months: {self.registered_salary_for_three_months()}\n'


def check_decimal_values(given_value_amount, type_of_variable):
    if not isinstance(given_value_amount, Decimal) or given_value_amount < Decimal('0.00'):
        raise ValueError(f'{type_of_variable} should be a decimal and greater or equal to zero!')