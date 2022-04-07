#!/usr/bin/python

import ctypes


class ArrayDynamic:
    def __init__(self, given_values=[]):
        if isinstance(given_values, list) and len(given_values) > 0:
            self._count = 0
            self._capacity = len(given_values) * 2
            self._low_level_array = self._new_low_level_array_c(self._capacity)
            self.extend(given_values)
        else:
            self._count = 0
            self._capacity = 1
            self._low_level_array = self._new_low_level_array_c(self._capacity)

    @property
    def count(self):
        return self._count

    @property
    def capacity(self):
        return self._capacity

    def __getitem__(self, index_value):
        if isinstance(index_value, slice):
            first = index_value.start
            end = index_value.stop
            step = index_value.step
        elif not (0 <= index_value < self._count):
            raise IndexError('Index value not valid!')
        else:
            return self._low_level_array[index_value]

        if index_value.step is None:
            step = 1
        elif index_value.step < 0:
            step = index_value.step * -1

        if first < 0 and end < 0:
            end = index_value.stop * -1
            first = index_value.start * -1
            new_arr = self._new_low_level_array_c(self._count)

            length_of = self._count - 1

            for i in range(self._count - 1, -1, -1):
                new_arr[length_of - i] = self._low_level_array[i]

            if step == 1:
                return new_arr[(end - 1):(first - 1):step]
            else:
                return new_arr[(end - 1):first:step]

        elif not ((0 <= first < self._count - 1) and (0 < end <= self._count)):
            raise IndexError('Index value not valid!')
        elif step:
            return self._low_level_array[first:end:step]
        else:
            return self._low_level_array[first:end]

    def __setitem__(self, key, value):
        if not 0 <= key < self._count:
            raise IndexError('Index value not valid!')

        self._low_level_array[key] = value

    def append(self, value):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        self._low_level_array[self.count] = value
        self._count += 1

    def insert_at(self, index, item):
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        elif index >= self._count or index < 0:
            raise IndexError('Index out of range!')

        for i in range(self._count, index, -1):
            self._low_level_array[i] = self._low_level_array[i - 1]

        self._low_level_array[index] = item
        self._count += 1

    def extend(self, iter_array):
        size_array = len(iter_array)

        if self.capacity == 1:
            self._resize(size_array * 3)
        elif (self.capacity - self.count) <= size_array:
            self._resize(2 * self._capacity + size_array)

        for i in range(size_array):
            self._low_level_array[self._count] = iter_array[i]
            self._count += 1

    def like_pop(self, index=None):

        if (index == self._count - 1) or (index is None):

            for_return = self._low_level_array[self._count - 1]
            self._low_level_array[self._count - 1] = None
            self._count -= 1

            if self._count == self._capacity // 4:
                self._resize(self._capacity // 2)

            return for_return

        elif index >= self._count or index < 0:
            raise IndexError('Out of range Index')

        value_to_remember = self._low_level_array[index]

        for i in range(index, self._count-1):
            self._low_level_array[i] = self._low_level_array[i+1]

        self._count -= 1
        self._low_level_array[self._count] = None

        if self._count == self._capacity // 4:
            self._resize(self._capacity // 2)

        return value_to_remember

    def remove(self, value):
        if_find = 0
        count = 0

        for i in range(self._count):
            if self._low_level_array[i] == value:
                if_find = 1
                count += 1
                for j in range(i, self._count - 1):
                    self._low_level_array[j] = self._low_level_array[j+1]

                self._low_level_array[self._count - 1] = None
                self._count -= 1
            if count == 1:
                if self._count == self._capacity // 4:
                    self._resize(self._capacity // 2)
                return 1

        if if_find == 0:
            raise ValueError('Value not found!')

    def find_index(self, value):
        for i in range(self._count):
            if self._low_level_array[i] == value:
                return i

    def reverse_the_array(self):
        array_for_reverse = self._new_low_level_array_c(self._capacity)

        j = self._count - 1
        for i in range(self._count - 1, -1, -1):
            array_for_reverse[j - i] = self._low_level_array[i]

        self._low_level_array = array_for_reverse

    def _resize(self, given_capacity):
        new_array_for_swap = self._new_low_level_array_c(given_capacity)

        for i in range(self._count):
            new_array_for_swap[i] = self._low_level_array[i]

        self._low_level_array = new_array_for_swap
        self._capacity = given_capacity

    def _new_low_level_array_c(self, capacity_given):
        return (capacity_given * ctypes.py_object)()

    def __str__(self):
        string_to_return = '['
        for i in range(self._count):
            if 0 < i < self._count:
                string_to_return += ', ' + str(self._low_level_array[i])
            else:
                string_to_return += str(self._low_level_array[i])

        return string_to_return + ']'


def reversing(given_element):
    reversed_array = ArrayDynamic()
    for i in range(given_element.count - 1, -1, -1):
        reversed_array.append(given_element[i])

    return reversed_array
