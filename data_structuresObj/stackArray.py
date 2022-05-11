#!/usr/bin/python

import dynArray
import fixedArray


class Empty(Exception):
    pass


class StackArray:

    __slots__ = '_data'

    def __init__(self, data=None):
        if isinstance(data, list):
            self._data = data
        elif isinstance(data, dict):
            self._data = [(i, j) for i, j in data.items()]
        else:
            self._data = []

    @property
    def data(self):
        return self._data

    @property
    def length(self):
        return len(self._data)

    def __getitem__(self, item):
        if self.length == 0:
            raise Empty('Stack is empty.')

        return self._data[item]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        self._iter_element = 0
        return self._data

    def __next__(self):
        if self._iter_element < self.length:
            element_to_return = self._data[self._iter_element]
            self._iter_element += 1
        else:
            raise StopIteration

        return element_to_return

    def is_empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def push(self, element_to_add):
        self._data.append(element_to_add)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        return self._data[-1]

    def __str__(self):
        if not self.is_empty():
            return f'{self._data}'
        else:
            return f''


def to_fixed_array(given_arr):
    new_arr_to_swap = fixedArray.FixedArray(list(given_arr))
    return new_arr_to_swap
