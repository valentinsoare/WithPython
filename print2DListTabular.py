#!/usr/bin/python

import operator


def display_table(given_list_of_grades):
    list_of_lists = list(map(operator.itemgetter(1), given_list_of_grades))
    length_list_of_lists = list(map(lambda l: len(l), list_of_lists))
    maximum = max(length_list_of_lists)

    print(f'{" ":<17}', end="")
    for i in range(maximum):
        print(f'{i + 1:<4}', end="")
    print()

    for index, item in list(enumerate(given_list_of_grades)):
        j, k = item

        print(f"{index + 1}. {j:<14}", end="")

        for i in k:
            print(f"{i:<2}", end="  ")
        print()


def main():
    list_of_grades = [['Chemistry', [10, 8, 2, 10, 7]], ['English', [8, 7, 5, 9, 10, 3]],
                                           ['Math', [10, 9, 8, 5]]]
    display_table(list_of_grades)


main()
