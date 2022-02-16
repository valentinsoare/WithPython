#!/usr/bin/python

import re


def catch_input():
    print('\n\033[1m - > Provide a phrase with extra spaces:\033[0m', end=" ")
    ask_input = input()

    return ask_input


def processing_input_text(given_string):
    number_of_spaces = given_string.count(" ")
    splitting_string = given_string.split()

    if number_of_spaces > (len(splitting_string) - 1):
        final_string_without_extra_spaces = ' '.join(splitting_string)
        to_know = 1
    else:
        to_know = 2
        final_string_without_extra_spaces = given_string

    return final_string_without_extra_spaces, to_know


def main():
    given_text = catch_input()
    text_after_processing, var_know = processing_input_text(given_text)

    if var_know == 1:
        print(f'\n\033[1m{"*Text after removing extra whitespaces:":>41}\033[0m', end=" ")
    else:
        print(f'\n\033[1m {"*No extra whitespaces in the given text:":>41}\033[0m', end=" ")

    print(f"{text_after_processing}")


main()
