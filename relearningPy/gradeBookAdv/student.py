#!/usr/bin/python


from re import split
from typing import Union
from collections import namedtuple


def check_first_and_last_name(value):
    if not isinstance(value, str):
        raise ValueError('First name and last name should be strings!')


def check_boolean(employed):
    if not isinstance(employed, bool):
        raise ValueError('Employed value should be a boolean, true or false!')


class Student:
    def __init__(self, first_name, last_name,  age, address, employed):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: Union[int, float] = age
        self.address: namedtuple = address
        self.employed: bool = employed
        self._grades_per_student: set = set()

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        check_first_and_last_name(first_name)
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        check_first_and_last_name(last_name)
        self._last_name = last_name

    @property
    def age(self) -> Union[float, int]:
        return self._age

    @age.setter
    def age(self, age: Union[int, float]):
        if not (isinstance(age, int) or isinstance(age, float)):
            raise ValueError('Age should be an integer or float!')
        self._age = age

    @property
    def address(self) -> namedtuple:
        return self._address

    @address.setter
    def address(self, address: str):
        print_message = """Address should be a string containing at least the name of the street and number
                             separated by a comma and space or just a comma!"""

        split_address = split(r',\s*', address)
        if not isinstance(address, str) or len(split_address) < 2:
            raise ValueError(print_message)

        address_ = namedtuple(typename='address', field_names=['street', 'house number', 'other',
                                                               'city', 'country', 'zipcode'])
        address_.__new__.__defaults__ = (None, ) * len(address_._fields)

        current_address = address_(*split_address)
        self._address = current_address

    @property
    def employed(self):
        return self._employed

    @employed.setter
    def employed(self, employed):
        check_boolean(employed)
        self._employed = employed

    @property
    def grades_per_student(self):
        return self._grades_per_student

