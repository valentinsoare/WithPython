#!/usr/bin/python

import operator
import numpy as np


def printing_simple_array(given_array):
    count = 0

    print(f'\n\033[1m{"GIVING":>20}\n{"ARRAY":>19}\033[0m', end="\n\n")
    for i in range(len(given_array)):
        print(f'{" ":>10}', end="")
        for j in range(len(given_array[i])):
            print(f"{given_array[i][j]}", end=" ")

            count += 1

            if count == 5:
                count = 0
                print()


def printing_dict_counting(given_dict):
    count = 0
    given_dict = dict(given_dict)

    print(f'{"-" * 50}', end="\n")
    for value, freq in given_dict.items():
        print(f'[ {value}: {freq} ]', end=" ")

        count += 1

        if count == 5:
            count = 0
            print(f'\n{"-" * 50}', end="\n")

    print("\n")


def main():
    given_array = np.array(np.random.randint(0, 99, 25).reshape(5, 5))
    given_array_reshaped = np.bincount(given_array.reshape(25))
    print(f"{given_array_reshaped}")
    length_given_array_reshaped = len(given_array_reshaped)
    dict_after_process = {}

    for value in range(length_given_array_reshaped):
        if given_array_reshaped[value] != 0:
            dict_after_process[value] = given_array_reshaped[value]

    to_sorting_and_printing = sorted(filter(lambda i: operator.itemgetter(0), dict_after_process.items()))

    printing_simple_array(given_array)
    print(f'\n\033[1m{"DIGIT":>13}: {"<frequency>"}\033[0m\n')
    printing_dict_counting(to_sorting_and_printing)


main()
