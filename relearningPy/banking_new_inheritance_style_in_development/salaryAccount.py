#!/usr/bin/python

from decimal import Decimal
from account import Account


class SalaryAccount(Account):
    def __init__(self, *, account_number, owner, balance, currency, owner_address, type_of_commission,
                 commission_amount, credit_card_withdraw_fees, annual_maintenance_fees,
                 transaction_salary_fees):
        super().__init__(account_number=account_number, owner=owner, balance=balance,
                         currency=currency, owner_address=owner_address)

        self.type_of_commission: str = type_of_commission
        self.commission_amount: Decimal = commission_amount
        self.credit_card_withdraw_fees: Decimal = credit_card_withdraw_fees
        self.annual_maintenance_fees: Decimal = annual_maintenance_fees
        self.transaction_salary_fees: Decimal = transaction_salary_fees
        self._registered_salary_for_three_months: list = []

    @property
    def type_of_commission(self) -> str:
        return self._type_of_commission

    @type_of_commission.setter
    def type_of_commission(self, type_of_commission):
        if not isinstance(type_of_commission, str) or type_of_commission not in ['weekly', 'daily', 'monthly', 'annually', 'no']:
            raise ValueError('Commissions type should be a str and one of '
                             'the following type: daily, weekly, monthly or annually!')

        self._type_of_commission = type_of_commission

    @property
    def commission_amount(self) -> Decimal:
        return self._commission_amount

    @commission_amount.setter
    def commission_amount(self, amount):
        check_decimal_values(given_value_amount=amount, type_of_variable='Commission amount')
        self._commission_amount = amount.quantize(Decimal("0.00"))

    @property
    def credit_card_withdraw_fees(self) -> Decimal:
        return self._credit_card_withdraw_fees

    @credit_card_withdraw_fees.setter
    def credit_card_withdraw_fees(self, amount):
        check_decimal_values(given_value_amount=amount, type_of_variable='Credit card withdraw fees')
        self._credit_card_withdraw_fees = amount.quantize(Decimal('0.00'))

    @property
    def annual_maintenance_fees(self) -> Decimal:
        return self._annual_maintenance_fees

    @annual_maintenance_fees.setter
    def annual_maintenance_fees(self, amount):
        check_decimal_values(given_value_amount=amount, type_of_variable='Annual maintenance fees')
        self._annual_maintenance_fees = amount.quantize(Decimal('0.00'))

    @property
    def transaction_salary_fees(self) -> Decimal:
        return self._transaction_salary_fees

    @transaction_salary_fees.setter
    def transaction_salary_fees(self, amount: Decimal):
        check_decimal_values(given_value_amount=amount, type_of_variable='Transaction fees')
        self._transaction_salary_fees = amount.quantize(Decimal('0.00'))

    def withdraw(self, *, amount) -> Decimal:
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00') or amount + self.transaction_salary_fees > self.balance:
            raise ValueError('Withdraw value should be a decimal greater or equal to '
                             'zero and not bigger than the current balance!')
        self.balance -= (amount + self.transaction_salary_fees)
        return self.balance

    def deposit(self, *, amount):
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00') or self.transaction_salary_fees > amount + self.balance:
            raise ValueError('Deposit amount should be a decimal, not less or equal to zero '
                             'and amount of transaction + balance should be greater than transaction fees!')

        calculated: Decimal = (amount - self.transaction_salary_fees)

        if len(self._registered_salary_for_three_months) == 3:
            self._registered_salary_for_three_months.append(calculated)
            self._registered_salary_for_three_months.pop(0)
        else:
            self._registered_salary_for_three_months.append(calculated)

        self.balance += calculated
    
    def registered_salary_for_three_months(self) -> list:
        return self._registered_salary_for_three_months

    def overdraft(self, *, amount) -> Decimal:
        if not isinstance(amount, Decimal) or amount <= Decimal('0.00'):
            raise ValueError('Overdraft should be a decimal value greater than zero!')

        overdraft_accepted: Decimal = (amount * (sum(self._registered_salary_for_three_months) / Decimal('6'))) - self.transaction_salary_fees
        self.balance += overdraft_accepted

        return overdraft_accepted

    def trial_period(self) -> bool:
        return self.__bool__()

    def __bool__(self) -> bool:
        return True if len(self._registered_salary_for_three_months) != 3 else False

    def __iter__(self) -> iter:
        dict_with_properties = {'account_number': self.account_number, 'owner': self.owner, 'balance': self.balance, 'currency': self.currency,
                                'type_of_commission': self.type_of_commission, 'commission_amount': self.commission_amount, 'owner_address': self.owner_address,
                                'credit_card_withdraw_fees': self.credit_card_withdraw_fees, 'annual_maintenance_fees': self.annual_maintenance_fees,
                                'transaction_salary_fees': self.transaction_salary_fees, 'registered_salary_for_three_months': self.registered_salary_for_three_months()}
        return iter(dict_with_properties.items())

    def __getattr__(self, item):
        if item in {'transaction_fee', 'interest_rate', 'interest', 'calculate_interest'}:
            raise NotImplementedError
        else:
            return getattr(self, item)

    def __str__(self):
        return f'account_number: {self.account_number}\n' \
               f'{Account.__str__(self)}\n' \
               f'type_of_commission: {self.type_of_commission}\n' \
               f'commission_amount: {self.commission_amount}\n' \
               f'credit_card_withdraw_fees: {self.credit_card_withdraw_fees}\n' \
               f'annual_maintenance_fees: {self.annual_maintenance_fees}\n' \
               f'transaction_salary_fees: {self.transaction_salary_fees}\n' \
               f'type_of_account: salary_account\n' \
               f'registered_salary_for_three_months: {self.registered_salary_for_three_months()}\n'


def check_decimal_values(*, given_value_amount, type_of_variable):
    if not isinstance(given_value_amount, Decimal) or given_value_amount < Decimal('0.00'):
        raise ValueError(f'{type_of_variable} should be a decimal and greater or equal to zero!')