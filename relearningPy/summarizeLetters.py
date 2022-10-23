#!/usr/bin/python

import string


def summarize_letters(given_string):
    all_letters = string.ascii_lowercase
    lowered_string_list = list(given_string.lower())
    list_with_uniq = []
    counting_list = []

    for letter in lowered_string_list:
        if letter not in list_with_uniq:
            list_with_uniq.append(letter)

    for second_letter in list_with_uniq:
        counting_list.append((second_letter, lowered_string_list.count(second_letter)))

    if len(counting_list) == len(all_letters):
        return counting_list, 1
    else:
        return counting_list, 0


def main():
    list_with_count, if_all_letters_alphabet = summarize_letters('Nebunie')

    if if_all_letters_alphabet == 1:
        print(f"\n - > Words with freq: {list_with_count}\n * String has all the letters from the alphabet.")
    else:
        print(f"\n - > Words with freq: {list_with_count}\n * String has not all the letters from the alphabet.")


if __name__ == '__main__':
    main()
