#!/usr/bin/python


from typing import Union
from datetime import date


def check_if_str(given_value):
    if not isinstance(given_value, str):
        raise ValueError(f'Name of the course should be a string!')


def check_if_numeric(given_value):
    if not (isinstance(given_value, float) or isinstance(given_value, int)):
        raise ValueError('Min grade and max grade should be a numeric instance, float or integer!')


class Course:
    def __init__(self, name_of_course, min_grade, max_grade):
        self.name_of_course: str = name_of_course
        self.min_grade: Union[float, int] = min_grade
        self.max_grade: Union[float, int] = max_grade
        self._grades_per_course: dict = {}

    @property
    def name_of_course(self) -> str:
        return self._name_of_course

    @name_of_course.setter
    def name_of_course(self, name_of_course):
        check_if_str(name_of_course)
        self._name_of_course = name_of_course

    @property
    def min_grade(self) -> Union[str, int, float]:
        return self._min_grade

    @min_grade.setter
    def min_grade(self, min_grade):
        check_if_numeric(min_grade)
        self._min_grade = min_grade

    @property
    def max_grade(self) -> Union[str, float, int]:
        return self._max_grade

    @max_grade.setter
    def max_grade(self, max_grade):
        check_if_numeric(max_grade)
        self._max_grade = max_grade

    @property
    def grades_per_course(self) -> dict:
        return self._grades_per_course

    def add_grade_per_course(self, *args):
        if len(args) > 1:
            args: list = list(map(float, args))
        else:
            if isinstance(args[0], str):
                args: list = list(map(float, args[0].split()))
            else:
                args: list = list(map(float, args[0]))

        if str(date.today()) not in self._grades_per_course.keys():
            self._grades_per_course.update({str(date.today()): args})
        else:
            self._grades_per_course[str(date.today())].extend(args)

    def edit_grade_per_course(self, old_grade: Union[float, int], new_grade: Union[float, int],
                              index_grade: int = None, date_grade: str = None, repetitions: int = 1):
        to_modify = None

        if old_grade and index_grade:
            to_modify = f'-1'
        elif new_grade and date_grade and index_grade:
            to_modify = self.grades_per_course.get(date_grade, '-2')

            if index_grade > len(to_modify) - 1:
                return f'-3'

            to_modify[index_grade] = float(new_grade)
            self._grades_per_course.update({date_grade: to_modify})
        elif old_grade and new_grade and date_grade:
            count_mod: int = 0
            to_modify = self._grades_per_course.get(date_grade, '-2')

            for i, j in enumerate(to_modify):
                if j == float(old_grade):
                    to_modify[i] = new_grade
                    count_mod += 1
                if count_mod == repetitions:
                    self._grades_per_course.update({new_grade: to_modify})
                    break

            to_modify = f'-4'

        return f'{to_modify}'

    def __repr__(self):
        return f'{self.name_of_course}: {self._grades_per_course}'

    def __str__(self):
        return self.__repr__()

