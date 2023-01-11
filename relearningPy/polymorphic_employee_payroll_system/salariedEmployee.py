#!/usr/bin/python

import decimal
from employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, social_security, weekly_salary):
        super().__init__(first_name, last_name, social_security)

        self.weekly_salary: decimal.Decimal = weekly_salary

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, weekly_salary):
        if not isinstance(weekly_salary, decimal.Decimal) or weekly_salary < decimal.Decimal('0.00'):
            raise ValueError('Weekly salary should be a decimal greater than zero!')

        self._weekly_salary = weekly_salary

    def __repr__(self):
        return f'SalariedEmployee: {Employee.first_name}, {Employee.last_name}; ' \
               f'{Employee.social_security}; {self.weekly_salary}'
