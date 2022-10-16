#!/usr/bin/python

"""We calculate the change using the fewest number of coins when we pay with one dollar bill (100 cents)
Change is in pennies, nickels, dimes and quarters.
 1 mills  = 0.1 cents
 5 mills = 0.5 (half cent)
 1 penny = 1 cent
 1 nickel = 5 cents
 1 dimes = 10 cents
 1 quarters = 25 cents"""

import os


def header(message):
    processed_message = ''

    for i in message:
        processed_message += '*' + i

    length_of_the_message = len(processed_message)

    print(f"\n{' ' * 5}{' ' * (length_of_the_message // 2 - 1)}{processed_message}")
    print(f"{ ' ' * 5}{'-' * (length_of_the_message * 2)}")


def ask_for_input_price():
    processed_price = ''
    error = 0

    while True:
        header("Calculating Change")
        print(f"\n{' ' * 4} ** Please provide the purchase price (q to quit):", end=" ")
        answer_input = input()

        if answer_input.lower()[0] == 'q':
            print(f"Exiting..")
            os.system('sleep 1')
            exit(0)

        try:
            processed_price = int(answer_input)
        except ValueError:
            try:
                processed_price = float(answer_input)
            except ValueError:
                error = 1

        if error == 1 or processed_price < 0:
            print(f"\n{' ' * 4}\033[1;31mERROR\033[0m Bad input value. We need positive values, integers or floats.")
            os.system('sleep 1')
            os.system('clear')
        else:
            return processed_price

        error = 0


def calculating_rest_of_1_dollar_bill(input_ask_price):
    list_with_values_of_coins = [('quarters', 25), ('dimes', 10), ('nickels', 5), ('pennies', 1), ('half-cent', 0.5), ('mills', 0.1)]
    give_change = []
    rest_to_give = 100 - input_ask_price
    change_to_give = rest_to_give

    for i in list_with_values_of_coins:
        if rest_to_give >= i[1]:
            how_many_times = rest_to_give // i[1]
            give_change.append((i[0], how_many_times))
            rest_to_give = rest_to_give - (how_many_times * i[1])

    return give_change, change_to_give


def print_result(purchase_price, change_to_give_as_a_list, rest_to_give):
    print(f"\n{' ' * 4} *** Purchase price was {purchase_price} cents, rest to give {rest_to_give} cents:")

    for i in change_to_give_as_a_list:
        print(f"{' ' * 6} - {int(i[1])} {i[0]}")


def main():
    input_price = ask_for_input_price()
    rest_as_a_list, give_rest = calculating_rest_of_1_dollar_bill(input_price)

    print_result(input_price, rest_as_a_list, give_rest)


if __name__ == "__main__":
    main()
