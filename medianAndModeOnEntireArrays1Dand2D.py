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


def determine_median(given_array):
    array_for_get = np.array(given_array)

    if len(given_array.shape) == 2:
        given_array = given_array.ravel()
        location = int(str(len(given_array) / 2 - 1).removesuffix('.0'))

        element_from_that_location = given_array[location]
        location_inside_initial_array = np.where(array_for_get == element_from_that_location)
        row, column = location_inside_initial_array
        print(f'\n\033[1m - > Median of the giving array is at the following location: Row: {row[0]}, '
              f'Column: {column[0]}, Element: {element_from_that_location}', end="\n\n")

    else:
        length_of_array = len(given_array)
        position_of_element = (length_of_array // 2 + 1)

        print(f'\n\033[1m - > Median of the giving array is at the following index: {position_of_element} '
              f'in the 1d array with element: {given_array[position_of_element]}', end="\n\n")


def determine_mode(given_array):
    arr_to_find = given_array

    if len(given_array.shape) == 2:
        given_array = given_array.ravel()

    uniq_values, indexes_of_uniq_array, freq = np.unique(given_array, return_inverse=True, return_counts=True)
    max_freq = max(freq)
    element_mode_indexes_uniq_array = np.where(freq == max_freq)[0]

    print(f"\n\033[1m - > Given array:\n {arr_to_find}\033[0m")

    if max_freq != 1:
        print(f"\n\033[1m - > Values with the most appearances (mode): ", end="")
    else:
        print(f"\n\033[1m - >  Only one instance from each value in the given array.\033[0m", end="\n\n")
        sys.exit(1)

    most_freq_elements = list(map(lambda k: uniq_values[k], element_mode_indexes_uniq_array))

    if len(arr_to_find.shape) == 1:
        print(f"{most_freq_elements}", end=" ")
        locations_indexes = [i for i in range(len(arr_to_find)) for j in element_mode_indexes_uniq_array if uniq_values[j] == arr_to_find[i]]
        print(f"with the following indexes: {locations_indexes}", end="\n\n")
    else:
        print()
        for element in most_freq_elements:
            print(f"\t\tElement: {element}", end="")
            row, column = np.where(arr_to_find == element)
            indexes_from_initial = [(row[i], column[i]) for i in range(len(row))]
            print(f", Locations (row, column): {indexes_from_initial}")

        print()



def main():
    #### 2d array
    array_to_process = np.array(np.random.randint(1, 100, 12).reshape(2, 6))

    #### 1d array
    #array_to_process = np.array([4, 9, 2, 2, 9, 1, 8, 5, 6, 2, 9, 10, 123, 2, 1, 9])
    #array_to_process = np.array(np.random.randint(1, 100, 8))

    #### this function supports as an argument a 1d array and it will give you all possible 2d arrays
    #return_arrays = all_possible_2d_arrays(array_to_process)

    ### print median for 1d and 2d arrays
    #determine_median(array_to_process)

    ### print mode for 1d and 2d arrays
    determine_mode(array_to_process)


main()
