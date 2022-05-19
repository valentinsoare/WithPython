#!/usr/bin/python

class Empty(Exception):
    pass


class StacksArray:
    _EMPTY_STACK = 'Stack is empty!'

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise Empty(self._EMPTY_STACK)

        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty(self._EMPTY_STACK)

        return self._data[-1]

    def __str__(self):
        value_for_returning = '['

        for i in range(len(self._data) - 1):
            value_for_returning += str(self._data[i]) + ', '

        value_for_returning += str(self._data[-1]) + ']'
        return value_for_returning
