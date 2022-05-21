#!/usr/bin/python

class Empty(Exception):
    pass


class DequeArray:
    _ARRAY_CAPACITY = 10
    _EMPTY_MESSAGE = 'Double queue is empty!'

    def __init__(self):
        self._data = [None] * self._ARRAY_CAPACITY
        self._first_element = 0
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        count = 0
        f = self._first_element

        while count < self._size:
            yield self._data[f]
            f = (f + 1) % len(self._data)
            count += 1

    def first(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        return self._data[self._first_element]

    def last(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        last_position = (self._first_element + self._size - 1) % len(self._data)
        return self._data[last_position]

    def _resize(self, capacity_value):
        old_array = self._data
        self._data = [None] * capacity_value

        for i in range(self._size):
            self._data[i] = old_array[self._first_element]
            self._first_element = (self._first_element + 1) % len(self._data)

        self._first_element = 0

    def add_last(self, element_to_add):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        position_to_add = (self._size + self._first_element) % len(self._data)
        self._data[position_to_add] = element_to_add
        self._size += 1

    def add_first(self, element_to_add):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        self._first_element = (self._first_element - 1) % len(self._data)
        self._data[self._first_element] = element_to_add
        self._size += 1

    def remove_last(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        position_to_remove = (self._size + self._first_element - 1) % len(self._data)
        element_to_return = self._data[position_to_remove]
        self._data[position_to_remove] = None
        self._size -= 1

        if 0 < self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return element_to_return

    def remove_first(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        first_value_for_return = self._data[self._first_element]
        self._data[self._first_element] = None
        self._first_element = (self._first_element + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return first_value_for_return

    def rotate(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        first = self._data[self._first_element]
        self._data[(self._size + self._first_element) % len(self._data)] = first
        self._data[self._first_element] = None
        self._first_element = (self._first_element + 1) % len(self._data)

    def __str__(self):
        counting = 0
        string_to_print = '['
        i = self._first_element

        while counting < self._size - 1:
            string_to_print += str(self._data[i]) + ', '
            i = (i + 1) % len(self._data)
            counting += 1

        string_to_print += str(self._data[i]) + ']'
        return string_to_print
