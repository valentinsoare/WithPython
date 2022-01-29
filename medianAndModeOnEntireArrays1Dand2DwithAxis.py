#!/usr/bin/python

import sys
import numpy as np


def all_possible_2d_arrays(digits_array):
    size = len(digits_array)
    values_after_divide = []

    for i in range(2, size):
        value_to_add = str(size / i)
        value_to_add = value_to_add.removesuffix('.0')
        if value_to_add.isdigit():
            values_after_divide += [value_to_add]

    combinations = [(int(values_after_divide[i]), int(values_after_divide[j])) for i in range(len(values_after_divide))
                    for j in range(i+1, len(values_after_divide)) if int(values_after_divide[i]) * int(values_after_divide[j]) == size]

    possible_arrays = []
    combinations = dict(combinations)

    for i, j in combinations.items():
        possible_arrays += [np.array(digits_array.reshape(i, j))]
        possible_arrays += [np.array(digits_array.reshape(j, i))]

    return possible_arrays


def generating_rr_cc(given_array, axis):
    if axis == 0:
        transposed_array = np.swapaxes(given_array, 0, 1)
        column_by_column_array = np.array(transposed_array.flatten())
        return column_by_column_array
    else:
        row_by_row_array = np.array(given_array.flatten())
        return row_by_row_array


def determine_median(given_array, axis=1):
    array_for_get = given_array

    if given_array.ndim == 2:
        if axis == 0:
            given_array = generating_rr_cc(given_array, axis=0)
        else:
            given_array = generating_rr_cc(given_array, axis=1)

        location = int(str(len(given_array) / 2 - 1).removesuffix('.0'))
        element_from_that_location = given_array[location]
        location_inside_initial_array = np.where(array_for_get == element_from_that_location)
        row, column = location_inside_initial_array

        print(f"\n\033[1;31m- > Given array:\033[0m\n\033[1m {array_for_get}\033[0m")
        print(f'\n\033[1;31m - > Median of the giving array is at the following location:\033[0m\033[1m Row: {row[0]},'
              f'Column: {column[0]}, Element: {element_from_that_location}\033[0m', end="\n\n")
    else:
        length_of_array = len(given_array)
        position_of_element = (length_of_array // 2 + 1)

        print(f'\n\033[1;31m- > Median of the giving array is at the following index:\033[0m\033[1;31m {position_of_element} '
              f'in the 1d array with element: {given_array[position_of_element]}\033[0m', end="\n\n")


def determine_mode(given_array, axis=1):
    arr_to_find = given_array

    if given_array.ndim == 2:
        if axis == 0:
            given_array = generating_rr_cc(given_array, axis=0)
        else:
            given_array = generating_rr_cc(given_array, axis=1)

    uniq_values, indexes_of_uniq_array, freq = np.unique(given_array, return_inverse=True, return_counts=True)
    max_freq = max(freq)
    element_mode_indexes_uniq_array = np.where(freq == max_freq)[0]

    print(f"\n\033[1;31m- > Given array:\033[0m\n\033[1m {arr_to_find}\033[0m")

    if max_freq != 1:
        print(f"\n\033[1;31m- > Values with the most appearances (mode):\033[0m ", end="")
    else:
        print(f"\n\033[1;31m - >  Only one instance from each value in the given array.\033[0m", end="\n\n")
        sys.exit(1)

    most_freq_elements = list(map(lambda k: uniq_values[k], element_mode_indexes_uniq_array))

    if len(arr_to_find.shape) == 1:
        print(f"\033[1m{most_freq_elements}\033[0m", end=" ")
        locations_indexes = [i for i in range(len(arr_to_find)) for j in element_mode_indexes_uniq_array
                             if uniq_values[j] == arr_to_find[i]]
        print(f"\033[1mwith the following indexes: {locations_indexes}\033[0m", end="\n\n")
    else:
        print()
        for element in most_freq_elements:
            print(f"\t\033[1mElement: {element}", end="")
            row, column = np.where(arr_to_find == element)
            indexes_from_initial = [(row[i], column[i]) for i in range(len(row))]
            print(f", Locations (row, column): {indexes_from_initial}\033[0m")

        print()


def print_2d_arrays(return_arrays):
    print(f"\n\033[1;31m- > All possible 2D arrays:\033[0m", end="\n\n")
    for i in return_arrays:
        print(f"\033[1m{i}\033[0m", end="\n")
        print(f'{"-" * 35}')
    print()


def main():
    #### 2d array
    array_to_process = np.array(np.random.randint(1, 100, 60).reshape(6, 10))

    #### 1d array
    #array_to_process = np.array([4, 9, 2, 2, 9, 1, 8, 5, 6, 2, 9, 10, 123, 2, 1, 9])
    #array_to_process = np.array(np.random.randint(1, 100, 40))

    #### this function supports as an argument a 1d array and it will give you all possible 2d arrays
    #return_arrays = all_possible_2d_arrays(array_to_process)

    ### print generated 2d arrays form given 1d
    #print_2d_arrays(return_arrays)

    ### print median for 1d and 2d arrays
    determine_median(array_to_process, 1)

    ### print mode for 1d and 2d arrays
    #determine_mode(array_to_process, 0)


main()
