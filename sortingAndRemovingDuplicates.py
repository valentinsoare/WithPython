#!/usr/bin/python

import string
import random
import numpy as np


def prepare_data_to_process():
    letters = string.ascii_lowercase
    list_of_letters = []
    count = letters.index('g')

    j = 0
    list_of_letters += letters[0:count]

    while j < count:
        generated_letter = random.randrange(0, count)
        list_of_letters += letters[generated_letter]
        j += 1

    return list_of_letters


def sorting_and_uniq(given_list, order_to_sort, eliminate_duplicates):
    processed_list = []

    if eliminate_duplicates == 0:
        if order_to_sort == 0:
            processed_list = sorted(given_list)  # ascending sort
        elif order_to_sort == 1:
            processed_list = sorted(given_list, reverse=True)   # descending sort
    elif eliminate_duplicates == 1:
        processed_list = np.unique(given_list)

    return processed_list


def main():
    list_to_be_sorted = prepare_data_to_process()
    sorted_list_ascending = sorting_and_uniq(list_to_be_sorted, 0, 0)
    sorted_list_descending = sorting_and_uniq(list_to_be_sorted, 1, 0)
    sorted_list_ascending_uniq = sorting_and_uniq(list_to_be_sorted, 0, 1)

    print(f"\n\033[1m -- > Generated list to be process:\033[0m\n {list_to_be_sorted}", end="\n")
    print(f"\n\033[1m -- > Sorted list in ascending order:\033[0m\n {sorted_list_ascending}", end="\n")
    print(f"\n\033[1m -- > Sorted list in descending order:\033[0m\n {sorted_list_descending}", end="\n")
    print(f"\n\033[1m -- > Sorted list with unique elements in ascending order:\033[0m\n {sorted_list_ascending_uniq}", end="\n")


main()
