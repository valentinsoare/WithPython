#!/usr/bin/python

import dataclasses
from decimal import Decimal


@dataclasses.dataclass(frozen=True)
class Student:
    name: str = 'none'
    mathematics: Decimal() = 0
    english: Decimal() = 0
    physics: Decimal() = 0

    def __str__(self):
        return f'Student name: {self.name}\nMathematics: {self.mathematics}\nEnglish: {self.english}\nPhysics: {self.physics}'


def main():
    first_student = Student(name='Valentin Soare', mathematics=8, english=4, physics=10)
    print(first_student)


if __name__ == '__main__':
    main()
