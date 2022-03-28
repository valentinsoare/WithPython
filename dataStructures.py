#!/usr/bin/python

import ctypes
import sys


def list_length_size():
    given_list = []

    for i in range(20):
        a = len(given_list)
        b = sys.getsizeof(given_list)
        print(f'Length: {a:>3d}, Size: {b:>3d} bytes')
        given_list.append(i)


def extend_array_under_list():
    given_A = [4, 10, 20, 100, 401, 1001, 23, 67]
    given_B = [0] * 16

    for i in range(len(given_A)):
       given_B[i] = given_A[i]

    given_A = given_B

    print(given_A)


class DynamicArray:
    def __init__(self):
        self._count = 0
        self._capacity = 1
        self._low_level_array = self._new_array(self._capacity)

    @property
    def capacity(self):
        return self._capacity

    @property
    def count(self):
        return self._count

    def __getitem__(self, index_k):
        if not 0 <= index_k < self._count:
            raise IndexError('Invalid index provided')

        return self._low_level_array[index_k]

    def append(self, obj):
        if self._count == self.capacity:
            self._resize(2 * self.capacity)
        self._low_level_array[self._count] = obj
        self._count += 1

    def extend(self, iterable_obj):
        iterable_size = len(iterable_obj)

        if (self.capacity - self.count) <= iterable_size:
            self._resize(2 * iterable_size * self._capacity)

        for i in range(iterable_size):
            self._low_level_array[self._count] = iterable_obj[i]
            self._count += 1

    def remove_from_index(self, index_of):
        if self.count == 0:
            print(f'Array is empty!')
            return 1
        elif index_of < 0 or index_of >= self.count:
            return IndexError('Index out of bounds!')
        elif index_of == self.count - 1:
            self._low_level_array[index_of] = 0
            self._count -= 1
            return 0

        for i in range(index_of, self.count-1):
            self._low_level_array[i] = self._low_level_array[i+1]

        self._low_level_array[self.count - 1] = 0
        self._count -= 1

    def _resize(self, given_capacity):
        new_array = self._new_array(given_capacity)

        for i in range(self._count):
            new_array[i] = self._low_level_array[i]

        self._low_level_array = new_array
        self._capacity = given_capacity

    def _new_array(self, given_capacity):
        return (given_capacity * ctypes.py_object)()


def init_array_class_and_print():
    init_array = DynamicArray()

    init_array.append(20)
    init_array.append('Lux')
    init_array.extend(['si', 'opulenta,', 'parfumat', 'dimanchat'])

    for i in range(init_array.count):
        print(f'{init_array[i]}', end=" ")

    init_array.remove_from_index(2)

    print()
    for i in range(init_array.count):
        print(f'{init_array[i]}', end=" ")


def main():
    #list_length_size()
    #extend_array_under_list()
    init_array_class_and_print()


if __name__ == '__main__':
    main()

