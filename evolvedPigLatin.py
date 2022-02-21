#!/usr/bin/python

import string


def catch_input_and_split():
    print(f"\n\033[1m - > Please enter you sentence/phrase: ", end="\033[0m")
    given_sentence = input()

    splitting_words = given_sentence.split()

    return splitting_words


def check_for_punctuation(given_word):
    punctuation_in_a_word = string.punctuation
    given_word_in_a_list = list(given_word)
    punctuation_location = {}

    for i in range(len(given_word_in_a_list)):
        if given_word_in_a_list[i] in punctuation_in_a_word:
            punctuation_location[i] = given_word_in_a_list[i]

    if len(punctuation_location) != 0:
        return True, punctuation_location

    return False, punctuation_location


def check_for_vowel(given_word):
    given_vowels = 'aeiou'

    if given_word[0] in given_vowels:
        return True

    return False


def processing_word(word_from_sentence):
    punctuation_to_add = ''
    val = 0

    if word_from_sentence.istitle():
        val = 1
        word_from_sentence = word_from_sentence.lower()

    value_if, value_locations = check_for_punctuation(word_from_sentence)

    for i, j in value_locations.items():
        if i == (len(word_from_sentence) - 1):
            punctuation_to_add = j
            word_from_sentence = word_from_sentence[:-1]

    final_word = word_from_sentence + punctuation_to_add

    if check_for_vowel(word_from_sentence):
        final_word = word_from_sentence + 'ay' + punctuation_to_add
    else:
        if word_from_sentence[0] in string.ascii_letters:
            final_word = word_from_sentence[1:] + word_from_sentence[0] + "ay" + punctuation_to_add

    if val == 1:
        final_word = final_word.title()

    return final_word


def main():
    split_phrase = catch_input_and_split()
    final_phrase = ''

    for i in split_phrase:
        processed_word = processing_word(i)
        final_phrase += ' ' + processed_word

    print(f"\n\033[1m \033[1;31m-> RESULT:\033[0m", end=" ")
    print(f"\033[1m{final_phrase}\033[0m", end="\n\n")


main()
