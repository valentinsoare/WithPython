#!/usr/bin/python


from time import sleep
from typing import Union
from collections import namedtuple
from .variousCheckings import _check_if_numeric, _for_name_checking, _check_address


class Student:
    def __init__(self, name,  age, address, id, employed):
        self.name = name
        self.age: Union[int, float] = age
        self.address: namedtuple = address
        self.id = id
        self.employed: bool = employed
        self._grades_per_student: dict = {}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = _for_name_checking(name)

    @property
    def age(self) -> Union[float, int]:
        return self._age

    @age.setter
    def age(self, age: Union[int, float]):
        self._age = _check_if_numeric(age)

    @property
    def address(self) -> namedtuple:
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = _check_address(address)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_number):
        self._id = id_number

    @property
    def employed(self):
        return self._employed

    @employed.setter
    def employed(self, employed):
        if not isinstance(employed, bool):
            print(f"\n{' ' * 3} \033[31mPOL1009 - Employed value should be a boolean!\033[0m\n")
            sleep(2)
        self._employed = employed

    @property
    def grades_per_student(self):
        return self._grades_per_student

    def __repr__(self):
        return self._name

