#!/usr/bin/python


import abc


class Employee(abc.ABC):
    def __init__(self, first_name, last_name, cnp):
        self._first_name: str = first_name
        self._last_name: str = last_name
        self.cnp: int = cnp
        self._properties_set = {self.first_name, self.last_name, self.cnp}

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str) or not (first_name.isalpha() or first_name.isalnum()):
            raise ValueError('First name should be a string with alpha chars or alnum chars!')

        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str) or not (last_name.isalpha() or last_name.isalnum()):
            raise ValueError('last name should be a string with alpha chars or alnum chars!')

        self._last_name = last_name

    @property
    def cnp(self):
        return self._cnp

    @cnp.setter
    def cnp(self, cnp):
        if not isinstance(cnp, int) or cnp <= 0 or len(str(cnp)) < 12:
            raise ValueError('CNP should be an integer greater than zero with 12 digits!')

        self._cnp = cnp

    @abc.abstractmethod
    def earnings(self):
        raise NotImplementedError

    @property
    def properties_set(self):
        return self._properties_set

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}; CNP: {self.cnp}'

    def __str__(self):
        return f'{self.__repr__()}'

