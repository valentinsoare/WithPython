#!/usr/bin/python

import itertools
import string
import time

given_phone_number = '0722853840'


def mapping_digits_letters():
    letters_alphabet = list(filter(lambda i: i not in ['q', 'z'], string.ascii_lowercase))
    numeric_phone_digits = list((filter(lambda i: i not in ['0', '1'], string.digits)))
    number_map_letters = []
    k = 0
    j = 3

    while k < len(numeric_phone_digits):
        number_map_letters += [(numeric_phone_digits[k], letters_alphabet[j-3:j])]
        k += 1
        j += 3

    return number_map_letters


def numeric_zero_and_ones(phone_number):
    phone_number_for_processing = list(phone_number)
    extracted_numbers = ['X'] * 10
    length_phone_number = len(phone_number)

    for i in range(length_phone_number):
        if phone_number_for_processing[i] in ['0', '1']:
            extracted_numbers[i] = phone_number_for_processing[i]

    return extracted_numbers, phone_number_for_processing


def from_digits_to_letters_mapping(numeric_phone):
    phone_number = list(numeric_phone)
    phone_number_to_process = list(filter(lambda j: j not in ['0', '1'], phone_number))
    map_digit_letters = mapping_digits_letters()
    mapping_phone_letter = []
    mapping_only_letter = []

    for i in phone_number_to_process:
        for j, k in map_digit_letters:
            if i == j:
                mapping_phone_letter += [(j, k)]

    for i in mapping_phone_letter:
        mapping_only_letter.append(tuple(i[1]))

    return mapping_phone_letter, mapping_only_letter


def phone_number_processing(phone_number):
    digits_letters, only_letters = from_digits_to_letters_mapping(phone_number)
    cartesian_product = list(itertools.product(*only_letters))

    return digits_letters, only_letters, cartesian_product


def combine_them():
    extracted_digits_letters, extracted_only_letters, cartesian_product = phone_number_processing(given_phone_number)
    only_zero_and_ones, number_processing = numeric_zero_and_ones(given_phone_number)
    combine = ['Y'] * len(given_phone_number)

    for i in range(len(number_processing)):
        for k, j in extracted_digits_letters:
            if number_processing[i] == k:
                combine[i] = j

    for j in range(len(only_zero_and_ones)):
        if only_zero_and_ones[j] in ['0', '1']:
            combine[j] = only_zero_and_ones[j]

    cartesian_product = list(map(lambda m: list(m), cartesian_product))

    return cartesian_product, combine


def from_number_to_letter_conversion():
    cartesian, combine = combine_them()
    with_zeros_and_letter_product = []

    for i in range(len(cartesian)):
        for j in range(len(combine)):
            if combine[j] in ['1', '0']:
                cartesian[i].insert(j, combine[j])

        with_zeros_and_letter_product.append(''.join(cartesian[i]))

    print(f'\n\033[1m - > Phone number: "{given_phone_number}" to letters:\033[0m', end="\n")

    for i in range(len(with_zeros_and_letter_product)):
        if i % 10 == 0:
            print()
        else:
            print(f"\033[1;32m{with_zeros_and_letter_product[i]}\033[0m", end="  ")

    print("\n\n\033[1;31m Exiting...\033[0m", end="\n\n")
    time.sleep(0.5)


def main():
    from_number_to_letter_conversion()


main()

