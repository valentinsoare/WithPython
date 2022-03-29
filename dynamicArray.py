#!/usr/bin/python

import ctypes
import time
import sys


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
            raise IndexError(f'Invalid index provided!')

        return self._low_level_array[index_k]

    def append(self, obj):
        if self._count == self.capacity:
            self._resize(2 * self.capacity)
        self._low_level_array[self._count] = obj
        self._count += 1

    def extend(self, iterable_obj):
        iterable_size = len(iterable_obj)

        if (self.capacity - self.count) <= iterable_size:
            self._resize(self._capacity * iterable_size)

        for i in range(iterable_size):
            self._low_level_array[self._count] = iterable_obj[i]
            self._count += 1

    def insert(self, index, item):
        if index < 0 or index > self.count:
            print(f'You need to use a proper index value.')
            return 1

        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.count, index, -1):
            self._low_level_array[i] = self._low_level_array[i-1]

        self._low_level_array[index] = item
        self._count += 1

    def delete_from_end(self):
        if self.count == 0:
            print(f'We have an empty array!')

        self._low_level_array[self.count - 1] = 0
        self._count -= 1

    def remove_from_index(self, index_of):
        if self.count == 0:
            print(f'Array is empty!')
            return 1
        elif index_of < 0 or index_of >= self.count:
            return IndexError(f'Index not in range!')
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

    #start_time = time.time()

    #for k in range(300):
    #    init_array.extend([0] * 40)

    #print(f'{init_array.count} and {init_array.capacity}')
    #end_time = time.time()

    #print(f'{(end_time - start_time) / 150}')

    #------------------
    init_array.extend([10, 40, 100, 23, 51])

    for i in init_array:
        print(f'{i}', end=" ")

    print()
    init_array.insert(2, 1000)

    for i in init_array:
        print(f'{i}', end=" ")
    print()


def main():
    init_array_class_and_print()


if __name__ == '__main__':
    main()
