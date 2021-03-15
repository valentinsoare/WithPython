#!/usr/bin/python3

import random
word = 'neuroscience'
word.partition()

def scramble_letters(given_word):
    word_as_list = given_word.partition()

    final_word = given_word[0] + random.shuffle()


scramble_letters(word)