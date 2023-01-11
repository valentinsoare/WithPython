#!/usr/bin/python


import decimal
from employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, cnp, weekly_salary, trial_period):
        super().__init__(first_name, last_name, cnp)

        self.weekly_salary: decimal.Decimal = weekly_salary
        self.trial_period = trial_period
        self._object_properties = {'first_name': self.first_name, 'last_name': self.last_name,
                                   'cnp': self.cnp, 'weekly_salary': self.weekly_salary,
                                   'trial_period': self.trial_period}

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, weekly_salary):
        if not isinstance(weekly_salary, decimal.Decimal) or weekly_salary < decimal.Decimal('0.00'):
            raise ValueError('Weekly salary should be a decimal greater than zero!')

        self._weekly_salary = weekly_salary

    @property
    def trial_period(self):
        return self._trial_period

    @trial_period.setter
    def trial_period(self, trial_period):
        if not isinstance(trial_period, int) or trial_period < 2:
            raise ValueError('Trial period value should be a float and greater or equal to 2 weeks!')

        self._trial_period = trial_period

    def earnings(self):
        return NotImplementedError

    def __iter__(self):
        return iter(self._object_properties.items())

    def __bool__(self):
        return True if self.trial_period >= 2 else False

    def __repr__(self):
        return f'SalariedEmployee: {Employee.__repr__(self)}; Weekly salary: {self.weekly_salary:,} ron;' \
               f' Trial period: {self.trial_period} weeks'

    def __str__(self):
        return f'{self.__repr__()}'
