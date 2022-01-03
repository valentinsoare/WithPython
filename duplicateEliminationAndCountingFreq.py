#!/usr/bin/python

import random
import numpy as np


def generate_list():
    generated_list = [random.randrange(1, (10 + 1)) for i in range(50)]
    return generated_list


def get_uniq_values_and_freq(given_list_of_numbers):
    uniq_list, frequencies = np.unique(given_list_of_numbers, return_counts=True)
    return uniq_list, frequencies


def main():
    list_of_numbers = generate_list()
    uniq_values, freq = get_uniq_values_and_freq(list_of_numbers)

    print(f"\n\033[1m - > Unique values and count number of appearances:\033[0m ", end="\n\n")

    for i, j in zip(uniq_values, freq):
        print(f"\tValue: {i},  Count: {j}", end="\n")


main()

