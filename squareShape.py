#!/usr/bin/python

import math


class Square:
    def __init__(self, side_length):
        self._side_length = side_length
        self._all_properties = {}
        self._validate_all_prop = 0

    @property
    def side_length(self):
        return self._side_length

    @property
    def perimeter(self):
        return self.side_length * 4

    @property
    def area(self):
        return self.side_length * self.side_length

    @property
    def diagonal(self):
        return math.sqrt(2 * self.side_length ** 2)

    def populate_properties(self):
        self._all_properties = {'side': self.side_length, 'perimeter': self.perimeter, 'area': self.area, 'diagonal': self.diagonal}
        self._validate_all_prop = 1

    @property
    def all_properties(self):
        if self._validate_all_prop == 1:
            return self._all_properties
        else:
            return f'\033[1;31m\nERROR - A list was not made with all properties from the square class.\033[0m\n'

    def __str__(self):
        return f'Side length: {self.side_length:,.2f}\nPerimeter: {self.perimeter:,.2f}\nArea: {self.area:,.2f}\nDiagonal: {self.diagonal:,.2f}'


def main():
    given_square = Square(4)
    #print(given_square)

    given_square.populate_properties()
    given_square_all_properties_dict = given_square.all_properties

    if isinstance(given_square_all_properties_dict, dict):
        for i, j in given_square_all_properties_dict.items():
            print(f"{i.title()}: {j:,.2f}")
    else:
        print(f'\n\033[1;31m ERROR Properties on the square object are not in a dict.\033[0m\n')


if __name__ == '__main__':
    main()
