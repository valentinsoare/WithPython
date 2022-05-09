#!/usr/bin/python

class Empty(Exception):
    pass


class Deque:
    DEQUE_CAPACITY = 10

    def __init__(self):
        self._array_data = [None] * Deque.DEQUE_CAPACITY
        self._number_of_elements = 0
        self._first_element = 0

    def __len__(self):
        return self._number_of_elements

    @property
    def capacity(self):
        return len(self._array_data)

    @property
    def number_of_elements(self):
        return self._number_of_elements

    def is_empty(self):
        if self._number_of_elements == 0:
            return True
        else:
            return False

    def __iter__(self):
        count = 0
        element_position = self._first_element

        while count < self._number_of_elements:
            yield self._array_data[element_position]
            element_position = (element_position + 1) % len(self._array_data)
            count += 1

    def __setitem__(self, key, value):
        if self.is_empty():
            raise Empty('Deque array is empty!')

        count = 0
        element_selector = self._first_element

        while count < self._number_of_elements:
            if count == key:
                self._array_data[element_selector] = value

            element_selector = (element_selector + 1) % len(self._array_data)
            count += 1

    def first(self):
        if self.is_empty():
            return Empty('Deque is empty!')

        return self._array_data[self._first_element]

    def last(self):
        if self.is_empty():
            return Empty('Deque is empty!')

        last_element = (self._first_element + self._number_of_elements - 1) % len(self._array_data)
        return self._array_data[last_element]

    def __getitem__(self, position):
        if self.is_empty():
            raise Empty('Deque array is empty!')
        elif not 0 <= position < self._number_of_elements:
            raise ValueError(f'Element is not available in this position, size of the '
                             f'deque array is {self._number_of_elements}.')

        element_for_parsing = self._first_element

        count = 0
        while count < self._number_of_elements:
            if count == position:
                return self._array_data[element_for_parsing]

            element_for_parsing = (element_for_parsing + 1) % len(self._array_data)
            count += 1

    def _resize(self, given_capacity):
        old_deque = self._array_data
        self._array_data = [None] * given_capacity

        first = self._first_element

        for i in range(self._number_of_elements):
            self._array_data[i] = old_deque[first]
            first = (self._first_element + 1) % len(self._array_data)

        self._first_element = 0

    def add_first(self, given_element):
        if self._number_of_elements == len(self._array_data):
            self._resize(2 * len(self._array_data))

        self._first_element = (self._first_element - 1) % len(self._array_data)

        self._array_data[self._first_element] = given_element
        self._number_of_elements += 1

    def add_last(self, given_element):
        if self._number_of_elements == len(self._array_data):
            self._resize(2 * len(self._array_data))

        back_element = (self._first_element + self._number_of_elements) % len(self._array_data)

        self._array_data[back_element] = given_element
        self._number_of_elements += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Deque array is empty!')

        value_to_return = self._array_data[self._first_element]

        self._array_data[self._first_element] = None
        self._first_element = (self._first_element + 1) % len(self._array_data)
        self._number_of_elements -= 1

        return value_to_return

    def remove_last(self):
        if self.is_empty():
            raise Empty('Queue array is empty')

        last_element = (self._first_element + self._number_of_elements - 1) % len(self._array_data)
        value_to_return = self._array_data[last_element]
        self._array_data[last_element] = None
        self._number_of_elements -= 1

        return value_to_return

    def __str__(self):
        for_printing = '['
        element_to_print = self._first_element

        count = 0
        while count < self._number_of_elements:
            if count == self._number_of_elements - 1:
                for_printing += str(self._array_data[element_to_print]) + ']'
                return for_printing

            for_printing += str(self._array_data[element_to_print]) + ', '

            element_to_print = (element_to_print + 1) % len(self._array_data)
            count += 1
