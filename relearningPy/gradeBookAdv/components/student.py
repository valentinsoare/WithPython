# student.py

from typing import Union
from collections import namedtuple
from .variousCheckings import _check_if_numeric, _for_name_checking, _check_address, _check_if_bool


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
    def name(self, name: str) -> None:
        self._name = _for_name_checking(name)

    @property
    def age(self) -> Union[float, int]:
        return self._age

    @age.setter
    def age(self, age: Union[int, float]) -> None:
        self._age = _check_if_numeric(age)

    @property
    def address(self) -> namedtuple:
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        self._address = _check_address(address)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_number) -> None:
        self._id = id_number

    @property
    def employed(self) -> str:
        return self._employed

    @employed.setter
    def employed(self, employed) -> None:
        self._employed = _check_if_bool(employed)

    @property
    def grades_per_student(self) -> dict:
        return self._grades_per_student

    def __repr__(self) -> str:
        return self._name
