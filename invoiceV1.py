#!/usr/bin/python

import decimal
import operator
import time
import sys


class Invoice:
    def __init__(self, item, number, description, qty, price):
        self._item = item
        self._number = number
        self._description = description
        self._qty = qty
        self._price = decimal.Decimal(price)

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def qty(self):
        if self._qty < 0:
            raise ValueError('Quantity needs to be greater than or equal to zero.')
        return self._qty

    @qty.setter
    def qty(self, qty):
        self._qty = qty

    @property
    def price(self):
        if self._price < 0:
            raise ValueError('Price of the item needs to be greater than zero.')
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def populate_dict_with_attributes_and_input(self):
        dict_with_attributes = {'item': self.item, 'part number': self.number,
                                'description': self.description, 'quantity': self.qty, 'price': self.price}

        return dict_with_attributes

    def calculate_invoice(self):
        return self.qty * self.price

    def __str__(self):
        return f'Item: {self.item}\nPart number: {self.number}\nDescription: {self.description}\n' \
               f'Quantity: {self.qty}\nPrice per item: {self._price:,.2f}$\n' \
               f'Total invoice: {self.calculate_invoice():,.2f}$\n'


def to_quit(given_input):
    if given_input == '':
        print(f'\n\033[1;31m {"  ERROR - you need to provide a valid answer"}\033[0m')
        time.sleep(1)
        return False
    elif given_input[0].lower() == 'q':
        print(f'\n\033[1;32m{"Quitting...":>18}\033[0m', end="\n\n")
        time.sleep(1)
        sys.exit(0)

    return True


def catch_number_of_invoices():
    given_input = ''
    var_to_continue = 0

    while var_to_continue == 0:
        print(f'\n [1] Enter the number of invoices you want to provide and calculate (q to quit):', end=" ")
        given_input = input()

        if not to_quit(given_input):
            continue

        try:
            given_input = int(given_input)
        except ValueError:
            print(f'\n\033[1;31m {"  ERROR - you need to provide an integer for number of invoices."}\033[0m')
            time.sleep(1)
        else:
            var_to_continue = 1

    return given_input


def catch_item_type():
    given_input = ''
    var_to_continue = 0

    while var_to_continue == 0:
        print(f'{" [2] Provide what type of item was bought (q to quit}:"}', end=" ")
        given_input = input()

        if not to_quit(given_input):
            continue

        if given_input.isnumeric():
            print(f'\n\033[1;31m {"  ERROR - you need to provide a name with letters, numbers in the name for your item."}\033[0m\n')
            time.sleep(1)
        else:
            var_to_continue = 1

    return given_input


def catch_description():
    given_input = ''
    to_continue = 0

    while to_continue == 0:
        print(f' [4] Provide a description for the item (q to quit):', end=" ")
        given_input = input()

        if not to_quit(given_input):
            continue

        if given_input.isnumeric():
            print(f'\n\033[1;31m {"ERROR - you need to use letters and/or digits.":>30}\033[0m\n')
            time.sleep(1)
        else:
            to_continue = 1

    return given_input


def catch_part_number():
    given_input = ''
    to_continue = 0

    while to_continue == 0:
        print(f'{" [3] Please give the part number: (q to quit}:":>30}', end=" ")
        given_input = input()

        if not to_quit(given_input):
            continue

        if not given_input.isalnum():
            print(f'\n\033[1;31m {"ERROR - you need to provide minimum and integer and/or a letter for part number.":>30}\033[0m\n')
            time.sleep(1)
        else:
            to_continue = 1

    return given_input


def catch_qty(item_type):
    given_input = ''
    to_continue = 0

    while to_continue == 0:
        print(f' [5] Provide how many {item_type}/s have you bought (q to quit):', end=" ")
        given_input = input()

        if not to_quit(given_input):
            continue

        try:
            given_input = int(given_input)
        except ValueError:
            print(f'\n\033[1;31m {"ERROR - you need to provide how many have you bought and needs to be an integer.":>30}\033[0m\n')
            time.sleep(1)
        else:
            if given_input < 0:
                print(f'\n\033[1;31m {"ERROR - quantity needs to be greater than zero."}\033[0m\n')
                time.sleep(1)
            else:
                to_continue = 1

    return given_input


def catch_price(item_type):
    to_continue = 0
    given_input = ''

    while to_continue == 0:
        print(f' [6] How much does a {item_type} cost in dollars (q to quit):', end=" ")
        given_input = input()

        if not to_quit(given_input):
            continue

        try:
            given_input = decimal.Decimal(given_input)
        except ValueError:
            print(f'\n\033[1;31m {"ERROR - you need to provide an integer or float for how many items have you bought.":>30}\033[0m\n')
            time.sleep(1)
        else:
            if given_input < 0:
                print(f'\n\033[1;31m{"Price of the item needs to be greater than zero."}\n')
                time.sleep(1)
            else:
                to_continue = 1

    return given_input


def printing_all_invoices_from_list(list_with_invoices):
    print(f'\n{"**ALL REGISTERED ITEMS BOUGHT**":>50}\n')

    for i in list_with_invoices:
        print(f'{i}')


def sort_by_price_from_list(list_with_invoices):
    dict_items_price = {}
    print(f'\n{"**ITEMS BOUGHT SORT BY PRICE**":>60}\n')

    for i in list_with_invoices:
        dict_items_price[i.item] = i.price

    dict_items_price = dict(sorted(dict_items_price.items(), key=operator.itemgetter(1)))
    for i, j in dict_items_price.items():
        print(f'Item: {i}, Price: {j}')




def main():
    list_with_invoices = []
    invoices_counter = 0
    print(f'\n\033[1m{"-"*30:>60}\n{"*GENERATE INVOICES*":>54}\n{"-"*30:>60}\033[0m')

    number_of_inv = catch_number_of_invoices()
    print(f'\n{"-" * 85}\n')

    while invoices_counter < number_of_inv:
        item_name = catch_item_type()
        part_number = catch_part_number()
        description_for_item = catch_description()
        item_qty = catch_qty(item_name)
        item_price = catch_price(item_name)

        if number_of_inv >= 1:
            print(f'\n{"-" * 85}\n')

        list_with_invoices.append(Invoice(item_name, part_number, description_for_item, item_qty, item_price))

        invoices_counter += 1

    printing_all_invoices_from_list(list_with_invoices)
    sort_by_price_from_list(list_with_invoices)


if __name__ == '__main__':
    main()
