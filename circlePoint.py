#!/usr/bin/python

from decimal import (Decimal, InvalidOperation)
from sys import exit


class Point:
    def __init__(self, x=0, y=0):

        try:
            x = Decimal(x)
            y = Decimal(y)
        except InvalidOperation:
            print(f'\033[1;31m ERROR - X and Y should be integers or float type.')
            exit(1)
        else:
            self._x = x
            self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        try:
            x = Decimal(x)
        except InvalidOperation:
            print(f'\033[1;31m ERROR - X and Y should be integers or float type.')
            exit(1)
        else:
            self._x = x

    @y.setter
    def y(self, y):
        try:
            y = Decimal(y)
        except InvalidOperation:
            print(f'\033[1;31m ERROR - X and Y should be integers or float type.')
            exit(1)
        else:
            self._y = y

    def move(self, x=0, y=0):
        try:
            x = Decimal(x)
            y = Decimal(y)
        except InvalidOperation:
            print(f'\033[1;31m ERROR - X and Y should be integers or float type.')
            exit(1)
        else:
            self.x = x
            self.y = y

    def __str__(self):
        return f'x={self.x}, y={self.y}'


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        try:
            radius = Decimal(radius)
            x = Decimal(x)
            y = Decimal(y)
        except InvalidOperation:
            print(f'\033[1;31m ERROR - radius, x, y should be integers or float type.')
            exit(1)
        else:
            self._point = super().__init__(x, y)
            self._radius = Decimal(radius)

    def move(self, x=0, y=0):
        return super().move(x, y)

    @property
    def radius(self):
        return self._radius

    @property
    def point(self):
        return self._point

    def __str__(self):
        return f'{super().__str__()}, radius: {self.radius}'


if __name__ == '__main__':
    #given_point = Point(x=4.23, y=10.23)

    circle_point = Circle(60)
    print(circle_point)

    circle_point.move(4, 10)
    print(circle_point)
