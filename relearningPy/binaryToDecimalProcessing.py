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
        print(f"\n ** Please give me an integer you want to convert, like a binary or decimal (q to quit):", end=" ")
        input_answer = input()

        if input_answer.lower()[0] == "q":
            print(f"\n{' ' * 5}Exiting...")
            os.system('sleep 1')
            exit(0)

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


def from_decimal_to_binary(given_number):
    count = 0
    list_to_process = []
    list_with_binary = []

    while True:
        processing_value = 2 ** count

        if given_number >= processing_value:
            list_to_process.append(processing_value)
        else:
            break

        count += 1

    list_to_process = list(reversed(list_to_process))

    for i in range(len(list_to_process)):
        if given_number >= list_to_process[i]:
            given_number = given_number - list_to_process[i]
            list_with_binary.append('1')
        else:
            list_with_binary.append('0')

    return ''.join(list_with_binary)


def main():
    number_from_user = catch_number()
    if_binary = determine_type(number_from_user)

    if if_binary:
        number_in_decimal_after_conversion = from_binary_to_decimal(number_from_user)
        print(f"\n - > Number that you gave was in binary \"{number_from_user}\" and converted in decimal is: \"{number_in_decimal_after_conversion}\" ")
    else:
        numbering = from_decimal_to_binary(number_from_user)
        print(f"\n - > Number that you gave was in decimal \"{number_from_user}\" and converted in binary is: \"{numbering}\" ")


if __name__ == '__main__':
    main()
