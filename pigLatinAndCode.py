#!/usr/bin/python3

import re
import itertools


def printing_lines(number_of_lines):
    i = 0
    while i < number_of_lines:
        print(f'-', end=' ')
        i += 1
    print()


def check_if_punctuation(given_word):
    checking = re.search(r'(([a-z]{1,})(\W))', given_word)
    if checking:
        punctuation_checking = 1
        return punctuation_checking, checking.group(1), checking.group(2), checking.group(3)
    else:
        punctuation_checking = 0
        return punctuation_checking, given_word


def check_word_with_capitalized_letter(given_word):
    if given_word[0].isupper():
        return True
    else:
        return False


def regarding_word_length(word, punctuation):
    word_length = len(word)

    if word_length >= 3:
        final_word_second = word[1] + word[2:word_length] + word[0] + 'ay' + punctuation
    elif word_length == 2:
        final_word_second = word[1] + word[0] + 'ay' + punctuation
    elif word_length == 1:
        final_word_second = word[0] + 'ay' + punctuation


    return final_word_second

def prepare_for_commas(given_word):
    tuple_of_running_function = (check_if_punctuation(given_word.lower()))

    if len(tuple_of_running_function) == 4:
        comma_condition, entire_word, word, punctuation = tuple_of_running_function
    else:
        comma_condition, word = tuple_of_running_function

    if comma_condition == 1:
        final_word = regarding_word_length(word, punctuation)
    else:
        final_word = regarding_word_length(word, '')

    return final_word


def generate_pig_latin_word(given_word):

    if check_word_with_capitalized_letter(given_word):
        given_word = prepare_for_commas(given_word).lower()
        final_pig_word = given_word[0].capitalize() + given_word[1:(len(given_word))]
    else:
        given_word = given_word.lower()
        final_pig_word = prepare_for_commas(given_word)

    return final_pig_word


def create_phrase(input_word):
    phrase = ''

    check = re.search(r'\w', input_word)
    if check:
        check_if_digit = re.search(r'\d', input_word)
        if check_if_digit:
            phrase += input_word + ' '
        else:
            phrase += generate_pig_latin_word(input_word) + ' '
    else:
        phrase += input_word

    return phrase


def running_main(list_of_words):
    phrase = ''

    for i in range(len(list_of_words)):
        phrase += create_phrase(list_of_words[i])

    print(f'\n\033[1m-> Coded Phrase:\033[0m \033[1;34m{phrase}\033[0m\n')


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

    return to_print


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


def main():
    given_text = input('\n\033[1m*Please enter your phrase: \033[0m')
    splitting_text = given_text.split()
    printing_lines(40)
    print(f'\033[1m*Enter which word (position from 0 to the end of the phrase) you want to code\n rest of the phrase will be in pig latin:\033[0m ')

    qty = input(f'\t- How many words you want to convert from letters to numbers (q to quit) ? -> ')

    if qty[0].lower() == 'q':
        print(f'\n\033[1;31mExiting...\033[0m')
        exit()
    else:
        qty = int(qty)

    i = 0
    j = 1
    list_words_to_convert = []

    print()
    while i < qty:
        value = input(f'\t\033[1;3{j + 1}m{i + 1}. Word number (q to interrupt and execute):\033[0m ')

        if value[0].lower() == 'q':
            break
        else:
            value = int(value)

        list_words_to_convert.append(splitting_text[value])
        i += 1
        j += 1

    phrase = ''

    for i in range(len(splitting_text)):
        if splitting_text[i] in list_words_to_convert:
            phrase += from_word_to_numbers(splitting_text[i]) + ' '
        else:
            phrase += create_phrase(splitting_text[i])

    print(f'\n\033[1;31m*Conversion for the given phrase:\033[0m\033[1;34m {phrase}\033[0m')


main()