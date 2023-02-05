#!/usr/bin/python

from re import match
from decimal import Decimal
from salaryAccount import SalaryAccount


class CreditCard(SalaryAccount):
    def __init__(self, account_number, owner, balance, currency, credit_card_withdraw_fees, annual_maintenance_fees,
                 type_of_commission, commission_amount, transaction_salary_fees, type_of_card, serial_number, expiration_date, **kwargs):
        super().__init__(account_number=account_number, owner=owner, balance=balance, currency=currency,
                         credit_card_withdraw_fees=credit_card_withdraw_fees, annual_maintenance_fees=annual_maintenance_fees,
                         type_of_commission=type_of_commission, commission_amount=commission_amount, transaction_salary_fees=transaction_salary_fees)

        self.type_of_card: str = type_of_card
        self.serial_number: str = serial_number
        self.expiration_date: str = expiration_date
        self.cvv: str = kwargs['cvv']
        self.address: str = kwargs['address']

    @property
    def type_of_card(self) -> str:
        return self._type_of_card

    @type_of_card.setter
    def type_of_card(self, card_type: str):
        if not (card_type and isinstance(card_type, str)) or card_type not in {'maestro', 'visa', 'mastercard'}:
            raise ValueError('Card type should be a str and one of the following: regular, silver, gold or platinum!')

        self._type_of_card = card_type

    @property
    def serial_number(self) -> str:
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number: str):
        if not (isinstance(serial_number, str) and match(r'(\d{4}-){3}(\d{4})', serial_number)):
            raise ValueError('Serial number should be formed of four groups of 4 digits limited by a dash!')

        self._serial_number = serial_number

    @property
    def expiration_date(self) -> str:
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: str):
        if not (isinstance(expiration_date, str) and match(r'(0[1-9]/\d{2})|(1[0-2]/\d{2})', expiration_date)):
            raise ValueError('Expiration date should be in the form of 01/23 and it must be a string.')

        self._expiration_date = expiration_date

    @property
    def cvv(self) -> str:
        return self._cvv

    @cvv.setter
    def cvv(self, cvv: str):
        if not isinstance(cvv, str) or len(str(cvv)) != 3:
            raise ValueError('CVV value should be an integer from of 3 digits!')

        self._cvv = cvv

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    def card_withdraw(self, amount: Decimal):
        if not(amount and isinstance(amount, Decimal)) or (amount + self.credit_card_withdraw_fees) > self.balance or \
               amount <= Decimal('0.00'):
            raise ValueError('Amount to be withdraw must be a decimal, greater than zero '
                             'and not greater than balance + fees!')

        self.balance -= (amount + self.credit_card_withdraw_fees)

    def cash_card_deposit(self, amount: Decimal):
        if not(amount and isinstance(amount, Decimal)) or amount <= Decimal('0.00') or \
               self.transaction_fees > (self.balance + amount):
            raise ValueError('Deposit amount should be greater than zero and amount + balance should not be '
                             'less than transaction fees')

        self.balance += (amount - self.transaction_fees)

    def __repr__(self):
        return f'account_number: {self.account_number}\n' \
               f'owner: {self.owner}\n' \
               f'balance: {self.balance}\n' \
               f'currency: {self.currency}\n' \
               f'credit_card_withdraw_fees: {self.credit_card_withdraw_fees}\n' \
               f'annual_maintenance_fees: {self.annual_maintenance_fees}\n' \
               f'type_of_card: {self.type_of_card}'

    def __str__(self):
        return self.__repr__()
