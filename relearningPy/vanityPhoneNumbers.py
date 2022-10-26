#!/usr/bin/python

import os
import string


def prepare_message_for_header(given_message):
    word = ''
    list_with_header = []
    message_to_display = ''

    for i in given_message:
        if i == ' ':
            list_with_header.append(word)
            word = ''
        else:
            word += i

    list_with_header.append(word)

    for i in list_with_header:
        message_to_display += ' ' + '*' + ' ' + i

    message_to_display += ' ' + '*'
    return message_to_display


def printing_header(given_message):
    length_of_message = len(given_message)
    print(f"\n\n{' ' * 12}{' ' * (length_of_message // 2 - 1)}{given_message}")
    print(f"{' ' * 12}{'-' * (length_of_message * 2)}")


def map_letters_digit():
    count = 2
    left = 0
    right = 3
    letters_from_alphabet = list(string.ascii_lowercase)
    letters_mapped = []

    while count < 10:
        if count == 7 or count == 9:
            right += 1
            letters_mapped.append([count, (letters_from_alphabet[left:right])])
            left += 1
        else:
            letters_mapped.append([count, tuple(letters_from_alphabet[left:right])])

        left += 3
        right += 3
        count += 1

    return letters_mapped


def ask_a_question():
    error = 1
    processing_answer = ''
    message_to_print = prepare_message_for_header('Vanity Phone Numbers')

    while error == 1:
        os.system('clear')
        printing_header(message_to_print)

        print(f"{' ' * 11} * You want to give a string to convert to digits (q to quit):", end=" ")
        answer = input()

        if answer.lower()[0] == 'q':
            print(f"\n{' ' * 14} Exiting...")
            os.system('sleep 1')
            exit(1)

        try:
            processing_answer = int(answer)
        except ValueError:
            error = 0
            processing_answer = answer.lower()

        if error == 1:
            print(f"\n{' ' * 5} \033[1;31m ERROR - Please do not use integers/floats. We need alpha characters. \033[0m")
            os.system('sleep 2')

    return processing_answer


def from_string_to_digit(list_mappings, given_string):
    number_after_conversion = ''.join(list(str(j[0]) for i in given_string for j in list_mappings if i in j[1]))
    return number_after_conversion


def print_the_result(given_string, converted_string):
    os.system('sleep 0.5')
    print(f"\n{' ' * 11} * \033[1;32mSUCCESS\033[0m From \"{given_string}\" converted to \"{converted_string}\"\n")
    exit(1)


def main():
    list_with_mappings = map_letters_digit()
    value_from_the_user = ask_a_question()

    value_after_conversion = from_string_to_digit(list_with_mappings, value_from_the_user)
    print_the_result(value_from_the_user, value_after_conversion)


if __name__ == '__main__':
    main()
