#!/usr/bin/python

import string


def processing_input(given_input):
    punctuation = string.punctuation

    for i in punctuation:
        if i in given_input:
            given_input = given_input.replace(i, '')

    if isinstance(given_input, str) and given_input.isalpha():
        given_input = list(map(lambda j: i.lower(), list(given_input)))

    return given_input


def get_uniq_words(given_string):
    list_of_uniq_words = set(given_string.split())
    return list_of_uniq_words


def main():

    given_sentence = """Price controls are said to exist whenever government mandates a maximum price ("price ceiling") above which a good or service cannot legally be sold or a minimum price ("price floor") below which a good or service cannot legally be sold.
Price ceilings attempt to lower the cost to the consumer of acquiring the price‐​ceilinged product, whereas a price floor attempts to increase the return received by sellers of the product in question. Both schemes achieve outcomes opposite of their objectives.
In markets without price controls, prices are determined by the interaction of the voluntary purchase and use decisions of buyers ("demand") with the voluntary production and sales decisions of sellers ("supply"). If, for whatever reason, buyers demand a product more intensely than had previously been the case—meaning that, at a specific price, they are prepared to buy greater quantities of it today than they were willing to buy yesterday—the result will be that the price will go up."""

    processed_input = processing_input(given_sentence)
    uniq_words = get_uniq_words(processed_input)
    print(f"\n\033[1m - > Unique words in the input text:\033[0m ", end="\n")

    uniq_words = list(uniq_words)
    length_of_uniq_words = len(uniq_words)

    for i in range(length_of_uniq_words):
        if i % 5 == 0:
            print()
        else:
            print(f"{uniq_words[i]}", end=" ")


main()

