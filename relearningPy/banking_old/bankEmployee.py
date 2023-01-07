#!/usr/bin/python

from bank import Bank
from decimal import Decimal


def checking_var(given_attribute, type_of_var):
    if not isinstance(given_attribute, type_of_var):
        raise ValueError(f'{given_attribute} should be a {type_of_var} in order to proceed further!')


class BankEmployee(Bank):
    def __init__(self, country: str, city: str, type_of_bank: str, name_of_bank: str,
                 surname: str, firstname: str, phone_number: int,  contract: str, salary: Decimal, currency: str, bonus_to_take: Decimal):
        super().__init__(country, city, type_of_bank, name_of_bank)

        self.surname = surname
        self.firstname = firstname
        self.phone_number = phone_number
        self.contract = contract
        self.salary = salary
        self.currency = currency
        self.bonus_to_take = bonus_to_take
        self.nr_of_bonuses_until_now: int = 0

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        checking_var(surname, str)
        self._surname = surname

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        checking_var(firstname, str)
        self._firstname = firstname

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if not isinstance(phone_number, int) or phone_number <= 0:
            raise ValueError('For the phone number please use a an integer with multiple digits and greater than zero! ')

        self._phone_number = phone_number

    @property
    def contract(self):
        return self._contract

    @contract.setter
    def contract(self, contract):
        if not isinstance(contract, str) or contract not in ['determined', 'undetermined']:
            raise ValueError('For contact type you need to have determined or undetermined!')

        self._contract = contract

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, Decimal) or salary <= Decimal('0.00'):
            raise ValueError('Salary should be in decimal and greater than zero!')

        self._salary = salary

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        checking_var(currency, str)
        self._currency = currency

    @property
    def bonus_to_take(self):
        return self._bonus_to_take

    @bonus_to_take.setter
    def bonus_to_take(self, bonus):
        if not isinstance(bonus, Decimal) or bonus <= Decimal('0.00'):
            raise ValueError('Bonus should be an integer and greater than zero!')

        self._bonus_to_take = bonus

    def __str__(self):
        return f'surname: {self.surname}, firstname: {self.firstname}, phone_number: {self.phone_number}, contract: {self.contract},' \
               f' salary: {self.salary}, currency: {self.currency}, bonus_to_take: {self.bonus_to_take}, nr_of_bonuses_until_now: {self.nr_of_bonuses_until_now}, ' \
               f'country: {self.country}, city: {self.city}, name_of_bank: {self.name_of_bank}, type_of_bank: {self.type_of_bank}'
