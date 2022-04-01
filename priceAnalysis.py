#!/usr/bin/python

import ctypes
import random


class ArrayDynamic:
    def __init__(self):
        self._count = 0
        self._capacity = 1
        self._low_level_array = self._new_low_level_array_c(self._capacity)

    @property
    def count(self):
        return self._count

    @property
    def capacity(self):
        return self._capacity

    def __getitem__(self, item):
        if isinstance(item, slice):
            first = item.start
            end = item.stop
        elif not (0 <= item < self.count):
            raise IndexError('Index value not valid!')
        else:
            return self._low_level_array[item]

        if item.step is None:
            step = 1
        elif item.step < 0:
            step = item.step * -1

        if first < 0 and end < 0:
            end = item.stop * -1
            first = item.start * -1
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

    def append(self, value):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        self._low_level_array[self.count] = value
        self._count += 1

    def insert_at(self, index, item):
        if self._count == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._count, index, -1):
            self._low_level_array[i] = self._low_level_array[i - 1]

        self._low_level_array[index] = item
        self._count += 1

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


def main():
    default_array = ArrayDynamic()

    i = 0
    while i < 5:
        default_array.append(random.randrange(1, 10))
        i += 1

    default_array.insert_at(1, 7)
    print(default_array)

    reversed_element = reversing(default_array)
    print(reversed_element)


if __name__ == '__main__':
    main()
