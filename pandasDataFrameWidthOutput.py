#!/usr/bin/python

import numpy as np


def prepare_series():
    given_array = np.array(np.random.randint(5, 150, 15))
    reshape_array = np.array(given_array.reshape(3, 5))
    return reshape_array


def determine_max_length_column(given_array):
    length_of_large_element_per_column = len(str(np.max(given_array)))
    return length_of_large_element_per_column


def populate_column_array_length(given_array):
    length_array = np.empty(0)

    for column in given_array.transpose():
        length_of_item = determine_max_length_column(column)
        length_array = np.append(length_array, str(length_of_item))

    return length_array


def main():
    given_array = prepare_series()
    length_per_column = populate_column_array_length(given_array)

    for i in range(len(given_array)):
        for j in range(len(given_array[i])):
            print(f'{given_array[i][j]:>{length_per_column[int(j)]}}', end=" ")
        print()


main()
