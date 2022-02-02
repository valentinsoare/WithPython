#!/usr/bin/python

import itertools


def catch_word_as_input():
    print(f"\n\033[1m - > Please enter a word:", end="\033[0m ")
    given_word = input()

    return list(given_word)


def generated_possible_perm(given_list_word):
    possible_perm = itertools.permutations(given_list_word, 3)
    return possible_perm


def main():
    word_given = catch_word_as_input()
    output_perm = generated_possible_perm(word_given)
    output_as_strings = []

    for i in output_perm:
        output_as_strings += [''.join(i)]

    print(f"\n\033[1;31m - > Three letter words: ", end="\033[0m\n")
    print(f"\n\t{output_as_strings}")


main()
