#!/usr/bin/python

import os
import operator
from decimal import Decimal


def header_message_prep(given_message_for_header):
    message_to_use = '* '
    count_white_spaces = 0

    for i in given_message_for_header:
        if i == ' ' and count_white_spaces == 1:
            message_to_use += ' ' + '#' + ' '
        elif i == ' ':
            count_white_spaces += 1
            message_to_use += ' '
        else:
            message_to_use += i

    message_to_use += ' *'
    return message_to_use


def header_printing(given_message):
    length_of_message = len(given_message)

    print(f"\n{' ' * 14}{' ' * (length_of_message // 2 - 1)}{given_message}")
    print(f"{' ' * 14}{' ' * (length_of_message // 2 - 1)}{'#' * length_of_message}")
    print(f"{' ' * 14}{'-' * (length_of_message * 2)}")


def printing_output(list_to_print, category):
    print(f"\n{' ' * 16} * Sort the list by {category}:\n")
    price_per_category_all_items = []

    for i in list_to_print:
        print(f"{' ' * 16} -  part number: {i[0]:2f}   description: {i[1]:<15}   quantity: {i[2]:<7.2f}   price per item: {i[3]:.2f}$")
        price_per_category_all_items.append((i[1], i[2], (i[2] * i[3])))

    print(f"\n{' ' * 16} ** Total price per purchase/item in sorted order:\n")

    for j in price_per_category_all_items:
        print(f"{' ' * 16} - description: {j[0]:<15}   quantity: {j[1]:<7.2f}   total price {j[2]:.2f}$")

    all_items = sum(list((k[2] for k in price_per_category_all_items)))

    print(f"\n{' ' * 16} ** Total per all items: {all_items:.2f}$\n")

    os.system('sleep 10')
    os.system('clear')


def sort_items_from_list(given_list_with_items):
    message_was_processed = header_message_prep('Nea\' Gigelu\' Hardware Store')
    sorting_criteria = ['part number', 'part description', 'quantity', 'price per item']
    error = 0
    processed_answer = ''

    while True:
        header_printing(message_was_processed)
        print(f"{' ' * 13} * Tell me the criteria you want to use for sorting the list:\n")

        for i in range(len(sorting_criteria)):
            print(f"{' ' * 20}[{i + 1}] {sorting_criteria[i]}")

        print(f"\n{' ' * 13} ** Answer (q to quit):", end=" ")
        given_answer = input()

        if given_answer.lower()[0] == 'q':
            print(f"\n{' ' * 16} Exiting...")
            os.system('sleep 1')
            exit(1)

        try:
            processed_answer = int(given_answer)
        except ValueError:
            error = 1

        if processed_answer not in [1, 2, 3, 4] or error == 1:
            print(f"\n{' ' * 16}\033[1;31m ERROR \033[0m Use only integers between 1 and 4.")
            os.system('sleep 2')
            error = 0
            os.system('clear')
        else:
            items_to_be_print = sorted(given_list_with_items, key=operator.itemgetter((processed_answer - 1)))
            criteria_sorting = sorting_criteria[(processed_answer - 1)]

            printing_output(items_to_be_print, criteria_sorting)


def main():
    #(part number, part description, qty, price per item)

    list_with_acquisitions = [(Decimal(83), 'Electric sander', Decimal(7), Decimal(57.98)),
                              (Decimal(24), 'Power saw', Decimal(18), Decimal(99.99)),
                              (Decimal(7), 'Sledge Hammer', Decimal(11), Decimal(21.50)),
                              (Decimal(77), 'Hammer', Decimal(76), Decimal(11.99)),
                              (Decimal(39), 'Jig saw', Decimal(3), Decimal(79.50))]

    sort_items_from_list(list_with_acquisitions)


if __name__ == '__main__':
    main()
