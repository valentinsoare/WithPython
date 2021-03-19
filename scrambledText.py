#!/usr/bin/python3

import random


def catch_input():
    input_string = input(f'\n\033[1m -> Enter input string: ')
    return input_string


def scramble_letters(given_word):
    word_as_list = list(given_word)
    list_for_shuffle = word_as_list[1:len(word_as_list)-1]
    random.shuffle(list_for_shuffle)

    if len(word_as_list) > 3:
        while list_for_shuffle == word_as_list[1:len(word_as_list)-1]:
            random.shuffle(list_for_shuffle)

    shuffled_word = ''.join(list_for_shuffle)
    to_processed = [i for i in [word_as_list[0], shuffled_word, word_as_list[-1]]]
    final = ''.join(to_processed)
    return final


def main():
    string_for_processed = catch_input()
    splitting_string = string_for_processed.split()
    list_after_processed = []

    for i in splitting_string:
        if i.isalpha() and len(i) > 1:
            processed_word = scramble_letters(i)
            list_after_processed.append(processed_word)
        else:
            list_after_processed.append(i)

    string_processed = ' '.join(list_after_processed)

    print(f'\n\033[1m ->> OUTPUT AFTER SCRAMBLING LETTERS: {string_processed}\033[0m')


main()
