#!/usr/bin/python

import os
import time
import random
from itertools import permutations


def show_header(given_message_from_user):
    processed_message = ' ##'
    tokenize_message = given_message_from_user.split()

    for i in range(len(tokenize_message)):
        word = ''
        for j in range(len(tokenize_message[i])):
            location = random.randrange(0, (len(tokenize_message[i]) - 1))
            if j == location:
                word += tokenize_message[i][j].upper()
            else:
                word += tokenize_message[i][j]

        processed_message += f" {word}"
    processed_message += ' ##'

    line_bellow_message = f"{'-' * (2 * len(processed_message))}"

    print(f"\n{' ' * 10}{processed_message:^{len(line_bellow_message)}}")
    print(f"{' ' * 10}{line_bellow_message}")


def catch_input(number_of_chars):
    error = 1

    while error == 1:
        os.system('clear')
        show_header('three-letter strings from five-letter word')

        print(f"{' * please give us as input at least '}{number_of_chars}{' chars word/numeric value:'}", end=" ")
        answer = input()

        if len(answer) < number_of_chars:
            print(f"\n{' ' * 3}{'ERROR please use only at least '}{number_of_chars} chars word/numeric value.")
            time.sleep(2)
        else:
            return answer


def creating_new_string(given_word, length_of_new_string):
    tokenized_word = list(given_word)
    new_word = permutations(tokenized_word, length_of_new_string)
    list_with_new_strings = []

    for i in list(new_word):
        list_with_new_strings.append([''.join(i)])

    list_with_new_strings = set([i[0] for i in list_with_new_strings])
    return list_with_new_strings


def printing_new_word(given_list_with_strings, length_of_new_string):
    print(f"\n{' ** unique strings with '}{length_of_new_string}{' chars length generated from input:'}")
    given_list_with_strings = list(given_list_with_strings)

    print(f"{' ' * 4}", end="")
    for i in range(len(given_list_with_strings)):
        if (i + 1) % 15 == 0:
            print(f"\n{' ' * 4 }", end="")
        else:
            print(f"{given_list_with_strings[i]}", end=" ")


def main():
    number_of_chars_for_input_word = 5
    number_of_chars_for_output_word = 3

    word_from_user = catch_input(number_of_chars_for_input_word)
    list_with_words_new = creating_new_string(word_from_user, number_of_chars_for_output_word)
    printing_new_word(list_with_words_new, number_of_chars_for_output_word)


if __name__ == '__main__':
    main()
