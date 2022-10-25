#!/usr/bin/python

import os
import string
import itertools


def printing_header(message):
    length_message = len(message)
    print(f"\n{' ' * 12}{' ' * (length_message // 2)}{message}")
    print(f"{' ' * 12}{'-' * (length_message * 2)}")


def ask_a_question():
    processed_answer = ''
    error = 0
    answer = ''

    while not isinstance(processed_answer, int):
        os.system('clear')
        printing_header('Letters from phone number')
        print(f"{' ' * 11} - > Please give us the phone number with 7 digits or more:", end=" ")
        answer = input()

        try:
            processed_answer = int(answer)
        except ValueError:
            error = 1

        if error == 1 or processed_answer < 0 or len(str(processed_answer)) < 7:
            print(f"\n{' ' * 7} \033[1;31m ERROR \033[0m - please give us another number, positive with 7 digits or more.")
            os.system('sleep 2')
            error = 0

    if answer[0] == '0':
        to_return = answer[0] + answer[1:len(answer)]
        return to_return
    else:
        return str(processed_answer)


def map_digits_letters():
    left = 0
    right = 3
    count = 2
    list_with_mapping = []
    given_letters_list = list(string.ascii_letters)

    while count != 10:
        if count == 7 or count == 9:
            right += 1
            list_with_mapping.append([count, tuple(given_letters_list[left:right])])
            left += 1
        else:
            list_with_mapping.append([count, tuple(given_letters_list[left:right])])

        left += 3
        right += 3
        count += 1

    return list_with_mapping


def extract_letters_by_digits(given_list_letters_digits, phone_number):
    list_to_work_with = []

    for i in str(phone_number):
        if i in ['0', '1']:
            list_to_work_with.append(i)
        for j in given_list_letters_digits:
            if i == str(j[0]):
                list_to_work_with.append(j[1])

    return list_to_work_with


def combine_letters(given_list_with_letters):
    list_from_product = list(''.join(i) for i in itertools.product(*given_list_with_letters))
    return list_from_product


def printing_result(list_with_combinations):
    length_of_an_element = len(list_with_combinations[0])

    print(f"\n - >  All possible combinations of letters:")

    for i in range(len(list_with_combinations)):
        if i % 10 == 0:
            print(f"\n{' ' * length_of_an_element}", end="")
        else:
            print(f"{list_with_combinations[i]}", end=" ")


def main():
    mapping_digits_letters = map_digits_letters()
    number_to_work_on = ask_a_question()

    letters_to_work_with = extract_letters_by_digits(mapping_digits_letters, number_to_work_on)

    all_possible_combinations = combine_letters(letters_to_work_with)

    printing_result(all_possible_combinations)


if __name__ == '__main__':
    main()
