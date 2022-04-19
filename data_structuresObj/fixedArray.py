#!/usr/bin/python

import dynArray
import stackArray


class FixedArray:
    def __init__(self, given_values=None):
        if isinstance(given_values, int):
            self._fixed_count = 0
            self._fixed_capacity = given_values
            self._fixed_array = [None] * self._fixed_capacity
        elif isinstance(given_values, list):
            self._fixed_count = len(given_values)
            self._fixed_capacity = self._fixed_count
            self._fixed_array = given_values
        elif isinstance(given_values, dynArray.DynamicArray):
            self._fixed_count = given_values.count
            self._fixed_capacity = given_values.capacity
            self._fixed_array = given_values
        elif isinstance(given_values, FixedArray):
            self._fixed_count = given_values.fixed_count
            self._fixed_capacity = given_values.fixed_capacity
            self._fixed_array = given_values
        elif given_values is None:
            self._fixed_count = 0
            self._fixed_capacity = 10
            self._fixed_array = [None] * self._fixed_capacity

        self._iter_limit = self._fixed_count

    @property
    def fixed_count(self):
        return self._fixed_count

    @property
    def fixed_capacity(self):
        return self._fixed_capacity

    @fixed_capacity.setter
    def fixed_capacity(self, fixed_capacity):
        self._fixed_capacity = fixed_capacity

    def __getitem__(self, item):
        if not 0 <= item < self.fixed_count:
            raise IndexError(f'Index not within valid range, 0 - {self.fixed_count - 1}')

        return self._fixed_array[item]

    def __setitem__(self, key, value):
        if not 0 <= key <= self._fixed_count:
            raise IndexError('Index value not valid!')

        self._fixed_array[key] = value

    def __len__(self):
        return self._fixed_count

    def __iter__(self):
        self._iterator_element = 0
        return self._fixed_array

    def __next__(self):
        if self._iterator_element < self._fixed_count:
            to_return = self._fixed_array[self._iterator_element]
            self._iterator_element += 1
            return to_return
        else:
            raise StopIteration

    def get(self, index_for_item):
        return self.__getitem__(index_for_item)

    def make_iter(self):
        return self.__iter__()

    def execute_next(self):
        return self.__next__()

    def fixed_to_dict(self, given_keys=None, to_return=0):
        fixed_to_dict_arr = {}

        if given_keys is None:
            fixed_to_dict_arr = dict([i for i in enumerate(self._fixed_array) if i[1] is not None])
        elif isinstance(given_keys, list) and len(given_keys) != 0:
            fixed_to_dict_arr = {given_keys[i]: self._fixed_array[i] for i in range(self.fixed_count)}

        if to_return == 1:
            return fixed_to_dict_arr
        elif to_return == 0:
            self._fixed_array = fixed_to_dict_arr

    def fixed_to_tuple(self):
        fixed_to_tuple_arr = [i for i in enumerate(self._fixed_array) if i[1] is not None]
        return fixed_to_tuple_arr

    def add_in_descending_sorter_order(self, given_value):
        if self._fixed_count < self._fixed_capacity or given_value > self._fixed_array[self._fixed_count - 1]:
            if self._fixed_count < self._fixed_capacity:
                self._fixed_count += 1

            last_element = self._fixed_count - 1

            while last_element > 0 and self._fixed_array[last_element - 1] < given_value:
                self._fixed_array[last_element] = self._fixed_array[last_element - 1]
                last_element -= 1

            self._fixed_array[last_element] = given_value

    def add_in_ascending_sorter_order(self, value_given):
        if self._fixed_count < self._fixed_capacity or value_given > self._fixed_array[0]:
            if self._fixed_count < self._fixed_capacity:
                self._fixed_count += 1

            last_element = self._fixed_count - 1

            while last_element > 0 and self._fixed_array[last_element - 1] > value_given:
                self._fixed_array[last_element] = self._fixed_array[last_element-1]
                last_element -= 1

            self._fixed_array[last_element] = value_given

    def reverse_the_array_lazy(self):
        reversed_array = FixedArray(self._fixed_count)
        length_to_use = self._fixed_count - 1

        for i in range(self._fixed_count - 1, -1, -1):
            reversed_array[length_to_use - i] = self._fixed_array[i]
            reversed_array._fixed_count += 1

        self._fixed_array = reversed_array

    def reverse_the_array_flash(self, start_index=None, end_index=None):
        if (start_index and end_index) is None:
            start_index = 0
            end_index = self._fixed_count - 1

        while end_index > start_index:
            self._fixed_array[start_index], self._fixed_array[end_index] = self._fixed_array[end_index], self._fixed_array[start_index]
            start_index += 1
            end_index -= 1

    def sort_array(self, reverse=False, to_return=False):
        array_to_work_on = self._fixed_array

        for i in range(1, self._fixed_count):
            j = i
            element_in_outer_loop = array_to_work_on[i]

            if not reverse:
                while j > 0 and array_to_work_on[j - 1] > element_in_outer_loop:
                    array_to_work_on[j] = array_to_work_on[j-1]
                    j -= 1
            else:
                while j > 0 and array_to_work_on[j - 1] < element_in_outer_loop:
                    array_to_work_on[j] = array_to_work_on[j - 1]
                    j -= 1

            array_to_work_on[j] = element_in_outer_loop

        if to_return:
            return FixedArray(array_to_work_on)
        else:
            self._fixed_array = array_to_work_on

    def __str__(self):
        to_return = '['

        for i in range(self.fixed_count):
            if i <= self._fixed_count - 2:
                to_return += str(self._fixed_array[i]) + ', '
            else:
                to_return += str(self._fixed_array[i]) + ']'

        return to_return


def to_fixed_array(given_values):
    new_arr = FixedArray(given_values)
    return new_arr


def to_dyn_array(given_arr):
    arr_to_return = dynArray.DynamicArray(given_arr)
    return arr_to_return


def reverse_order(given_values):
    to_return = FixedArray(given_values)
    to_return.reverse_the_array_flash()

    return to_return


def to_stack(given_values):
    values_to_add = []
    if isinstance(given_values, dict):
        values_to_add = [(i, j) for i, j in given_values.items()]
    elif isinstance(given_values, list) or isinstance(given_values, tuple) or \
            isinstance(given_values, FixedArray) or isinstance(given_values, dynArray.DynamicArray):
        values_to_add = [given_values[k] for k in range(len(given_values))]

    stack_to_return = stackArray.StackArray(values_to_add)

    return stack_to_return
