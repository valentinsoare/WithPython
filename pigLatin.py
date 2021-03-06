#!/usr/bin/python3

import re


def check_if_punctuation(given_word):
    checking = re.search(r'(([a-z]{1,})(\W))', given_word)
    if checking:
        punctuation_checking = 1
        return punctuation_checking, checking.group(1), checking.group(2), checking.group(3)
    else:
        punctuation_checking = 0
        return punctuation_checking, given_word, given_word, ''


def check_word_with_capitalized_letter(given_word):
    if given_word[0].isupper():
        return True
    else:
        return False


def prepare_for_commas(given_word):
    comma_condition, entire_word, word, punctuation = check_if_punctuation(given_word.lower())
    word_length = len(word)
    if comma_condition == 1:
        final_word = word[1] + word[2:word_length] + word[0] + 'ay' + punctuation
    else:
        final_word = word[1] + word[2:word_length] + word[0] + 'ay'

    return final_word


def generate_pig_latin_word(given_word):

    if check_word_with_capitalized_letter(given_word):
        given_word = prepare_for_commas(given_word).lower()
        final_piglatin_word = given_word[0].capitalize() + given_word[1:(len(given_word))]
    else:
        given_word = given_word.lower()
        final_piglatin_word = prepare_for_commas(given_word)

    return final_piglatin_word


def running_main(list_of_words):
    phrase = ''
    for i in list_of_words:
        phrase += generate_pig_latin_word(i) + ' '

    print(f'\n\033[1m-> Coded Phrase:\033[0m \033[1;34m{phrase}\033[0m')


given_text = input('\n\033[1m*Please enter your phrase: \033[0m')
list_of_words = given_text.split()
running_main(list_of_words)
