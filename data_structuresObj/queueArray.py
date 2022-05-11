#!/usr/bin/python

class Empty(Exception):
    pass


class QueueArray:
    DEFAULT_CAP = 10
    __slots__ = '_data', '_size', '_first_element'

    def __init__(self):
        self._data = [None] * QueueArray.DEFAULT_CAP
        self._size = 0
        self._first_element = 0

    def __len__(self):
        return self._size

    @property
    def capacity(self):
        return len(self._data)

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty!')

        return self._data[self._first_element]

    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity

        front_element = self._first_element

        for i in range(self._size):
            self._data[i] = old[front_element]
            front_element = (1 + front_element) % len(old)

        self._first_element = 0

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        to_add_position = (self._first_element + self._size) % len(self._data)

        self._data[to_add_position] = element
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return Empty('Queue is empty!')

        value_to_return = self._data[self._first_element]

        self._data[self._first_element] = None
        self._first_element = (self._first_element + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return value_to_return

    def __str__(self):
        variable_to_return = '['
        f = self._first_element
        counting = 0

        while counting < self._size:
            variable_to_return += str(self._data[f])
            f = (f + 1) % len(self._data)

            if counting == self._size - 1:
                variable_to_return += ']'
                return variable_to_return

            variable_to_return += ', '
            counting += 1

        return variable_to_return





