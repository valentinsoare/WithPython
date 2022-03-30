#!/usr/bin/python

import random


def to_add_in_a_list_and_maintain_sorter_order(value_to_add, given_list, count_elements):

    if count_elements < len(given_list) or value_to_add > given_list[-1]:
        if count_elements < len(given_list):
            count_elements += 1

        last = count_elements - 1

        while last > 0 and given_list[last - 1] < value_to_add:
            given_list[last] = given_list[last - 1]
            last -= 1

        given_list[last] = value_to_add

        return given_list, count_elements


def insertion_sort(given_list):
    for i in range(1, len(given_list)):
        j = i
        current_element_in_outer_loop = given_list[i]

        while j > 0 and given_list[j - 1] > current_element_in_outer_loop:
            given_list[j] = given_list[j - 1]
            j -= 1

        given_list[j] = current_element_in_outer_loop

    return given_list


def main():
    given_list = [None] * 10

    i = 0
    count_elements = 0
    while i < 10:
        number = random.randrange(0, 20)
        given_list, count_elements = to_add_in_a_list_and_maintain_sorter_order(number, given_list, count_elements)
        i += 1

    print(given_list)

    second_list_for_sort = [4, 10, 8, 5, 2, 9, 12]
    sorted_list_with_insertion = insertion_sort(second_list_for_sort)

    print(sorted_list_with_insertion)


if __name__ == '__main__':
    main()
