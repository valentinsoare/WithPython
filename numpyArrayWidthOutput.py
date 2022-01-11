#!/usr/bin/python

import numpy as np


def prepare_for_printing(given_array_as_list):
    given_array = np.array(given_array_as_list)
    length_of_large_element = len(str(np.max(given_array)))
    converted_array = given_array.reshape((2, 5))

    return length_of_large_element, converted_array


def printing_array_like_np(given_array, given_length):
    for row in given_array:
        for column in row:
            print(f"{column:>{given_length}}", end=" ")
        print()


def main():
    given_list = [2, 3, 5, 7, 124, 11, 13, 17, 19, 23]
    length_of_item, conv_array = prepare_for_printing(given_list)

    printing_array_like_np(conv_array, length_of_item)


main()

