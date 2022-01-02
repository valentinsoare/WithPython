#!/usr/bin/python

import operator
import sys


def generate_sample_hw_data(*args):
    sample_data = []
    part_number, part_description, quantity, price = args

    for i in range(5):
        sample_data.append((part_number[i], part_description[i], quantity[i], price[i]))

    return sample_data


def sort_given_list_tuples(given_list_of_tuples, element_of_sort):
    if element_of_sort == 1:
        sorted_by_description = sorted(given_list_of_tuples, key=operator.itemgetter(1))
        print(f"\n\033[1m - > Sorted invoices by description:\033[0m \n{sorted_by_description}", end="\n")
    elif element_of_sort == 3:
        sorted_by_price = sorted(given_list_of_tuples, key=operator.itemgetter(3), reverse=True)
        print(f"\n\033[1m - > Sorted invoices by price: \033[0m \n{sorted_by_price}", end="\n")


def mapping_to_description_and_quantity(given_list_invoices):
    mapping_to = operator.itemgetter(1, 2)

    list_of_description_qty = sorted(list(map(mapping_to, given_list_invoices)), key=operator.itemgetter(1))
    print(f"\n\033[1m - > List from description and quantity and then sort by quantity:\033[0m\n {list_of_description_qty}", end="\n")


def mapping_to_description_invoice_value(given_list_invoices, starting=0, stopping=0):
    mapping_to_value = operator.itemgetter(1, 2, 3)
    list_of_description_and_invoice_value = list(map(mapping_to_value, given_list_invoices))
    final_after_product = []

    for i, j, k in list_of_description_and_invoice_value:
        if starting < 0 or stopping < 0:
            print(f"\n\nERROR\n\n")
            sys.exit(0)
        elif starting == 0 and stopping == 0:
            final_after_product += [(i, j * k), ]
        else:
            if starting < j * k < stopping:
                final_after_product += [(i, j * k), ]

    sorted_by_invoice_value = sorted(final_after_product, key=operator.itemgetter(1), reverse=True)

    return sorted_by_invoice_value


def calculate_total_invoices(given_data_invoices):
    total = 0

    for i in given_data_invoices:
        j, k = i
        total += k

    print(f"\n - > Total of all invoices is: {total}", end="\n")


def main():
    part_number = [83, 24, 7, 77, 39]
    part_description = ['electric sander', 'power saw', 'sledge hammer', 'hammer', 'jig saw']
    quantity = [7, 18, 11, 76, 3]
    price = [57.98, 99.99, 21.50, 11.99, 79.50]

    hw_data = generate_sample_hw_data(part_number, part_description, quantity, price)

    print(f"\n\033[1m**Pattern in the tuples from the list of tuples: part_number, part_description, quantity, price\033[0m"
          , end="\n")

    #sort by description
    sort_given_list_tuples(hw_data, 1)

    #sort by price
    sort_given_list_tuples(hw_data, 3)

    #description and quantity and sort by qty
    mapping_to_description_and_quantity(hw_data)

    #mapping description and invoice values and sort by invoice value
    sort_by_all_invoice_values = mapping_to_description_invoice_value(hw_data, 0, 0)
    print(f"\n\033[1m - > Description and invoice values and sort by invoice in descending:\033[0m\n {sort_by_all_invoice_values}", end="\n")

    #description and invoice value but invoice value in a given range
    given_range_to_print = mapping_to_description_invoice_value(hw_data, 0, 1000)
    print(f"\n\033[1m - > Description and invoice in descending order in a given range:\033[0m\n {given_range_to_print}", end="\n")

    given_data_invoices = mapping_to_description_invoice_value(hw_data, 0, 0)
    calculate_total_invoices(given_data_invoices)


main()

