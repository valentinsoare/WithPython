#!/usr/bin/python

class Empty(Exception):
    pass


class QueueArray:
    _QUEUE_CAP = 10
    _EMPTY_MESSAGE = 'Queue is empty!'

    def __init__(self):
        self._data = [None] * self._QUEUE_CAP
        self._first_element = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _resize(self, capacity):
        old_array = self._data
        self._data = [None] * capacity

        for i in range(self._size):
            self._data[i] = old_array[self._first_element]
            self._first_element = (1 + self._first_element) % len(old_array)

        self._first_element = 0

    def enqueue(self, element):
        if len(self._data) == self._size:
            self._resize(2 * len(self._data))

        next_position_to_add = (self._first_element + self._size) % len(self._data)

        self._data[next_position_to_add] = element
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        value_to_return = self._data[self._first_element]
        self._data[self._first_element] = None

        self._first_element = (1 + self._first_element) % len(self._data)
        self._size -= 1

        if 0 < self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return value_to_return

    def first(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        return self._data[self._first_element]

    def __str__(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        count = 0
        string_to_print = '['
        position = self._first_element

        while count < self._size - 1:
            string_to_print += str(self._data[position]) + ', '
            position = (position + 1) % len(self._data)
            count += 1

        string_to_print += str(self._data[position]) + ']'
        return string_to_print
