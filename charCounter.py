#!/usr/bin/python

import string
from collections import Counter


def parse_sentence_processing(given_sentence):
    punctuation = string.punctuation

    for i in punctuation:
        if i in given_sentence:
            given_sentence = given_sentence.replace(i, '')

    sentence_as_list_letters = list(map(lambda j: j.lower(), list(given_sentence)))

    return sentence_as_list_letters


def count_letters(given_list):
    counting = Counter(given_list)
    counting_parsed = {i: j for i, j in counting.items() if i.isalpha()}

    return counting_parsed


def display_letters(dict_count):
    sorted_alpha_order = dict(sorted(dict_count.items()))
    all_letters = set(string.ascii_lowercase)
    sorted_alpha = set(sorted_alpha_order.keys())

    for i, j in sorted_alpha_order.items():
        print(f"{i}\t{j}")

    print(f"\n - > Letters not in the original string:", end=" ")

    for i in all_letters.difference(sorted_alpha):
        print(f"{i}", end=" ")

    print()


def main():

    given_sentence ="""Sen. Ted Cruz (R-Texas) begged Tucker Carlson for forgiveness on Thursday. His sin: intimating that some of the people who 
    stormed the U.S. Capitol on Jan. 6, 2021 were terrorists. The one-time presidential candidate debased himself in front of millions of conservative viewers, attempting 
    to atone for daring to criticize the MAGA rioters, but a prickly Carlson refused to accept his apology."""

    list_of_letters = parse_sentence_processing(given_sentence)
    counter_dict = count_letters(list_of_letters)
    display_letters(counter_dict)


main()
