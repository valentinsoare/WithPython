#!/usr/bin/python

import os


def header(message_to_print):
    chars_to_replace = {'u': '|_|', 's': '5', 'a': '@', 'o': '0', 'e': '3'}
    processed_message = ' ### '
    list_with_keys_for_message = chars_to_replace.keys()

    for i in message_to_print:
        if i in list_with_keys_for_message:
            processed_message += ' ' + chars_to_replace[i]
        else:
            processed_message += ' ' + i

    processed_message += ' ### '
    length_of_message = len(processed_message)

    print(f"\n{' ' * int(length_of_message * 0.5)}{processed_message}")
    print(f"{' ' * int(length_of_message * 0.25)}{'-' * int(length_of_message * 1.5)}")


def ask_user_for_value():
    processed_answer = ''
    error = 0

    while not isinstance(processed_answer, int) and not isinstance(processed_answer, float):
        header('check amount word equivalent')
        print(f"\n{' ' * 20} * Give us an amount less than 1000$ (q to quit):", end=" ")

        answer = input()

        if answer[0].lower() == 'q':
            print(f"\n{' ' * 23} Exiting...")
            os.system('sleep 1')
            exit(0)

        try:
            processed_answer = int(answer)
        except ValueError:
            try:
                processed_answer = float(answer)
            except ValueError:
                error = 1

        if error == 1 or processed_answer < 0:
            print(f"\n{' ' * 23} ERROR give us a float or int value greater than zero.")
            os.system('sleep 1')
            error = 0
            processed_answer = ''

    return f"{processed_answer:.2f}"


def processing_value_from_user(from_user_value):

    splitting_input = from_user_value.split('.')

    if int(splitting_input[1]) > 0:
        value_to_return_int_part = int(splitting_input[0])
        value_if_float_part = int(splitting_input[1])
    else:
        value_to_return_int_part = int(splitting_input[0])
        value_if_float_part = None

    return value_to_return_int_part, value_if_float_part


def check_analyse_value(int_part, float_part, digit_values):
    reversed_dict_keys = list(reversed(digit_values.keys()))
    list_with_values_integers = []

    for i in reversed_dict_keys:
        if i <= int_part:
            count = 0
            while int_part >= i:
                int_part -= i
                count += 1

            list_with_values_integers.append(count * i)

    list_with_values_floats = [float_part, 100]

    return list_with_values_integers, list_with_values_floats


def printing_digits_into_words(*args):
    list_with_integers, list_with_floats, dict_values = args
    to_print_string = ''

    count = 1
    list_values = list(reversed(dict_values.keys()))

    for i in range(len(list_with_integers)):
        for j in list_values:
            if count - i == 2:
                break

            if list_with_integers[i] >= j and len(str(list_with_integers[i])) == 3:
                calc = int(list_with_integers[i]/j)
                to_print_string += f"{dict_values[calc]}{dict_values[j]}"
                count += 1
            elif list_with_integers[i] >= j and len(str(i)) != 3:
                to_print_string += f"{dict_values[j]}"
                count += 1

    if isinstance(list_with_floats[0], int):
        print(f"\n{' ' * 20} * Converted to letters: {to_print_string} and {list_with_floats[0]/list_with_floats[1]} dollars")
    else:
        print(f"\n{' ' * 20} * Converted to letters: {to_print_string} dollars")


def main():
    digit_values = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: "Five", 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'One Thousand'
    }

    numeric_value_from_user = ask_user_for_value()
    int_part, float_part = processing_value_from_user(numeric_value_from_user)
    list_integers, list_floats = check_analyse_value(int_part, float_part, digit_values)

    printing_digits_into_words(list_integers, list_floats, digit_values)


if __name__ == '__main__':
    main()
