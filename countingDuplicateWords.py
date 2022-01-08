#!/usr/bin/python

import operator
import string
from collections import Counter


def string_prep(sentence):
    to_remove_punctuation = list(string.punctuation)

    for i in to_remove_punctuation:
        if i in sentence:
            sentence = sentence.replace(i, '')

    return sentence


def words_counter(sentence_given):
    given_list_of_words = list(map(lambda i: i.lower(), list(sentence_given.split())))
    counting = Counter(given_list_of_words)

    return counting


def parse_the_counter_dict(given_dict):
    given_dict = dict(sorted(given_dict.items(), key=operator.itemgetter(1)))
    number_of_duplicate_words = 0
    dict_with_duplicate_words = {}

    for word, count in given_dict.items():
        if count > 1:
            number_of_duplicate_words += 1
            dict_with_duplicate_words.update({word: count})

    return dict_with_duplicate_words, number_of_duplicate_words


def printing(dict_with_dup, number_of_dup):
    print(f"\n\033[1m - > Words that appeared more than once:\033[0m ", end="\n\n")

    for i, j in dict_with_dup.items():
        print(f"{i:<20} {j}")

    print(f"\n\033[1;31m - > We have {number_of_dup} words with two or more occurrences.\033[0m", end="\n")


def main():

    given_sentence = """Price controls are said to exist whenever government mandates a maximum price ("price ceiling") above which a good or service cannot legally be sold or a minimum price ("price floor") below which a good or service cannot legally be sold.
Price ceilings attempt to lower the cost to the consumer of acquiring the price‐​ceilinged product, whereas a price floor attempts to increase the return received by sellers of the product in question. Both schemes achieve outcomes opposite of their objectives.
In markets without price controls, prices are determined by the interaction of the voluntary purchase and use decisions of buyers ("demand") with the voluntary production and sales decisions of sellers ("supply"). If, for whatever reason, buyers demand a product more intensely than had previously been the case—meaning that, at a specific price, they are prepared to buy greater quantities of it today than they were willing to buy yesterday—the result will be that the price will go up."""

    sentence_without_punctuation = string_prep(given_sentence)
    counter_dict = words_counter(sentence_without_punctuation)
    dict_with_duplicates, number_of_duplicates = parse_the_counter_dict(counter_dict)
    printing(dict_with_duplicates, number_of_duplicates)


main()
