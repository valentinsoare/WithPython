#!/usr/bin/python


import random


def processing_list_eliminates_duplicates(given_list):
    sorted_list = sorted(given_list)
    list_sorted_without_duplicates = []

    element_to_check = 0

    for i in sorted_list:
        if i != element_to_check and sorted_list.count(i) == 1:
            element_to_check = i
            list_sorted_without_duplicates.append(i)

    if len(list_sorted_without_duplicates) == 0:
        list_sorted_without_duplicates = 'No uniq values in the list'

    return list_sorted_without_duplicates


def main():
    list_to_process = [random.randrange(1, 10) for i in range(20)]
    print(f"\n - > Given List: {list_to_process}")

    processed_list = processing_list_eliminates_duplicates(list_to_process)

    print(f" - > List after processing, uniq values and sorted: {processed_list}")


if __name__ == '__main__':
    main()
