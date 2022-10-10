#!/usr/bin/python

import os


def header(given_message):
    length_of_message = len(given_message)
    print(f"\n{' ' * 5}{' ' * (length_of_message // 2)}{given_message}")
    print(f"{' ' * 5}{'-' * (length_of_message * 2)}")


def catch_number():
    processing_number = ''
    output_error = 0

    while not isinstance(processing_number, int):
        os.system('clear')
        header('Conversion | binary < - > decimal')
        print(f"\n ** Please give me an integer you want to convert, like a binary or decimal:", end=" ")
        input_answer = input()

        try:
            processing_number = int(input_answer)
        except ValueError:
            output_error = 1

        if output_error == 1 or processing_number < 0:
            print(f"\n \033[1;31mERROR\033[0m Please use only integers of type decimal or binary.")
            os.system('sleep 1')

    return processing_number


def determine_type(number_from_the_user):
    binary_type = True

    while number_from_the_user > 0:
        after_processed = number_from_the_user % 10

        if after_processed != 1 and after_processed != 0:
            binary_type = False

        number_from_the_user = number_from_the_user // 10

        if number_from_the_user == 0:
            return binary_type


def from_binary_to_decimal(given_value):
    given_value = str(given_value)
    length_of_binary = len(given_value)
    list_wit_values_to_use = []
    number_in_decimal = 0

    for i in range(length_of_binary - 1, -1, -1):
        list_wit_values_to_use.append(2 ** i)

    for j in range(length_of_binary):
        if int(given_value[j]) != 0:
            number_in_decimal += list_wit_values_to_use[j]

    return number_in_decimal

#def from_decimal_to_binary(given_number):


def main():
    number_from_user = catch_number()
    if_binary = determine_type(number_from_user)

    if if_binary:
        number_in_decimal_after_conversion = from_binary_to_decimal(number_from_user)


if __name__ == '__main__':
    main()
