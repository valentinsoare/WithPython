# course.py

from typing import Union
from collections import namedtuple
from .variousCheckings import _check_if_str, _check_if_numeric, _for_name_checking


class Course:
    def __init__(self, name_of_course, min_grade, max_grade, teacher_name):
        self.name_of_course: str = name_of_course
        self.min_grade: Union[float, int] = min_grade
        self.max_grade: Union[float, int] = max_grade
        self.teacher_name: str = teacher_name

    @property
    def name_of_course(self) -> str:
        return self._name_of_course

    @name_of_course.setter
    def name_of_course(self, name_of_course) -> None:
        self._name_of_course = _check_if_str(name_of_course)

    @property
    def min_grade(self) -> Union[str, int, float]:
        return self._min_grade

    @min_grade.setter
    def min_grade(self, min_grade: int = 1) -> None:
        self._min_grade = _check_if_numeric(min_grade)

    @property
    def max_grade(self) -> Union[str, float, int]:
        return self._max_grade

    @max_grade.setter
    def max_grade(self, max_grade: int = 10) -> None:
        self._max_grade = _check_if_numeric(max_grade)

    @property
    def teacher_name(self) -> namedtuple:
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name) -> None:
        self._teacher_name = _for_name_checking(teacher_name)

    def __repr__(self):
        return self.name_of_course
