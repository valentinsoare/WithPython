#!/usr/bin/python


from decimal import Decimal
from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, cnp, hours_worked, wage_per_hour):
        super().__init__(first_name, last_name, cnp)

        self.hours_worked: Decimal = hours_worked
        self.wage_per_hour: Decimal = wage_per_hour
        self._attributes = {'first_name': self.first_name, 'last_name': self.last_name,
                            'cnp': self.cnp, 'hours_worked': self.hours_worked, 'wage_per_hour': self.wage_per_hour}

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, hours_worked):
        if not isinstance(hours_worked, Decimal) or hours_worked < Decimal('0.00'):
            raise ValueError('Hours worked should be a decimal value greater or equal to zero!')

        self._hours_worked = hours_worked

    @property
    def wage_per_hour(self):
        return self._wage_per_hour

    @wage_per_hour.setter
    def wage_per_hour(self, wage_per_hour):
        if not isinstance(wage_per_hour, Decimal) or wage_per_hour <= Decimal('0.00'):
            raise ValueError('Wage per hour should be a decinal value greater than zero!')

        self._wage_per_hour = wage_per_hour

    def earnings(self):
        return Decimal((self.hours_worked * self.wage_per_hour))

    def __iter__(self):
        return iter(self._attributes.items())

    def __len__(self):
        return len(self._attributes)

    def __bool__(self):
        return True if self.hours_worked >= Decimal('20.00') else False

    def __repr__(self):
        return f'HourlyEmployee: {Employee.__repr__(self)}; Weekly earnings: {self.earnings():,} ron'

    def __str__(self):
        return f'{self.__repr__()}'
