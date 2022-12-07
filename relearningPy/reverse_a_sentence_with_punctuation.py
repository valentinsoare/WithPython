#!/usr/bin/python

import os
import re
import string
import time


def printing_message_header(given_message_for_header):
    processed_message = '*# '
    processed_message += ' '.join(given_message_for_header.title())
    processed_message += ' #*'
    length_of_message = len(processed_message)
    line_below_message = f"{'-' * (2 * length_of_message)}"

    print(f"\n{' ' * 10}{line_below_message}")
    print(f"{' ' * 10}|{processed_message:^{len(line_below_message) - 2}}|")
    print(f"{' ' * 10}{line_below_message}")


def ask_the_question():
    error = 1

    while error == 1:
        os.system('clear')
        printing_message_header('reversing a sentence')
        print(f"\n{' * Sentence to reverse:'}", end=" ")

        answer = input()

        if len(answer) == 0 or re.match(r'\s+', answer):
            print(f"\n{' ' * 2}{'ERROR - if you want to reverse something, please put it here.'}")
            os.system('sleep 2')
        else:
            return answer


def check_for_punctuation_and_reverse_one_word(given_word):
    punctuation = '!"#$%&\'()*+,./:;<=>?[\]`{|}~'
    word_without_punctuation = list(given_word.translate(str.maketrans('', '', punctuation)))
    length_of_word = len(given_word)

    for i in range(length_of_word):
        if given_word[i] in punctuation:
            if 0 <= i <= 2:
                word_without_punctuation.insert((len(word_without_punctuation) - i), given_word[i])
            elif (len(given_word) - 3) <= i <= (len(given_word) - 1):
                word_without_punctuation.insert((i - (len(given_word) - 1)), given_word[i])

    return ''.join(word_without_punctuation)


def reverse_the_string(input_string_from_user):
    splitting_string = list(reversed(input_string_from_user.split()))
    length_of_splitting_string = len(splitting_string)
    reversed_list = []

    for i in range(length_of_splitting_string):
        reversed_word = check_for_punctuation_and_reverse_one_word(splitting_string[i])
        reversed_list.append(reversed_word)

    return ' '.join(reversed_list)


def printing_reversed_sentence(given_sentence_reversed):
    print(f"\n{' ** Reversed: '}{given_sentence_reversed}")


def main():
    input_sentence = ask_the_question()
    sentence_that_was_reversed = reverse_the_string(input_sentence)

    printing_reversed_sentence(sentence_that_was_reversed)


if __name__ == '__main__':
    main()
