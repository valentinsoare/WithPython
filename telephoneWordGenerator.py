#!/usr/bin/python

import itertools
import string
import time


def mapping_digits_letters():
    letters_alphabet = list(filter(lambda i: i not in ['q', 'z'], string.ascii_lowercase))
    numeric_phone_digits = list((filter(lambda i: i not in ['0', '1'], string.digits)))
    number_map_letters = []
    k = 0
    j = 3

    length_numeric_phone_digits = len(numeric_phone_digits)

    # we can do something like this with zip, but it is more sexy this way :D

    while k < length_numeric_phone_digits:
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
    extracted_digits_letters, extracted_only_letters, cartesian_product = phone_number_processing(given_input)
    only_zero_and_ones, number_processing = numeric_zero_and_ones(given_input)
    combine = ['Y'] * len(given_input)

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

    print(f'\n\033[1;1;42m - > Phone number: "{given_input}" to letters: \033[0m', end="\n")

    for i in range(len(with_zeros_and_letter_product)):
        if i % 10 == 0:
            print()
        else:
            print(f"\033[1;32m{with_zeros_and_letter_product[i]}\033[0m", end="  ")

    print("\n\n\033[1;31m Exiting...\033[0m", end="\n\n")
    time.sleep(0.5)


def mapping_text_to_int(given_text):
    map_digit_letters = mapping_digits_letters()
    from_letters_to_numbers = ''
    given_text = list(given_text)

    for i in given_text:
        for digit, letters in map_digit_letters:
            if i in letters:
                from_letters_to_numbers += ' '.join(digit)

    return from_letters_to_numbers


def main(input_given):
    if input_given.isnumeric():
        from_number_to_letter_conversion()
    else:
        phone_number = mapping_text_to_int(input_given)
        print(f"\n\033[1;32m - >  From letters to numbers: {phone_number} \033[0m", end="\n\n")


given_input = input("\n\033[1m - > Enter your phone number/text: \033[0m")
main(given_input)
