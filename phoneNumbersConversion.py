#!/usr/bin/python3

import itertools
import sys


def digits_and_letters(letters):
    number = 3
    traverse = 0
    group_letters = []

    while number <= len(letters):
        group_letters.append([])
        for i in range(number - 3, number):
            group_letters[traverse].append(letters[i])
        traverse += 1
        number += 3

    numbers_letters = list(enumerate(group_letters, start=2))
    return numbers_letters


def from_word_to_numbers(given_string):
    list_for_processed = list(filter(lambda i: i, given_string.lower()))
    letters = list('abcdefghijklmnoprstuvwxy')
    to_be_processed = digits_and_letters(letters)
    output_string = []

    for i in range(len(list_for_processed)):
        for value, letters in to_be_processed:
            if list_for_processed[i] in letters:
                output_string.append(value)

    to_print = ''.join([str(i) for i in output_string])
    print(f'\n * Conversion from letters to corresponding digits on the phone keyboard: {given_string} -> {to_print}')


def from_numbers_to_words(given_string):
    processed_string = list(filter(lambda x: x, given_string))
    letters = list('abcdefghijklmnoprstuvwxy')
    final_version = []
    numbers_letters = digits_and_letters(letters)
    count = 0

    for i in processed_string:
        for j in range(len(numbers_letters)):
            if int(i) == numbers_letters[j][0]:
                final_version.append(numbers_letters[j][1])

    print(f'\n-> List with possible combinations from given input ({given_string}) using phone keyboard:', end='\n\n')
    for i in itertools.product(*final_version):
        string_for_print = ''.join(i)
        print(f'{string_for_print}', end=' ')
        count += 1
        if count % 10 == 0:
            print()


def main(given_string):
    if given_string.isnumeric():
        return from_numbers_to_words(given_string)
    else:
        from_word_to_numbers(given_string)


main(sys.argv[1])
print()
