#!/usr/bin/python

import string
import numpy as np

given_string = 'Ce facem ma boss aici ? Sa imi spui ce putem face. Trebuie sa intelegem ca e lux si opulenta.'


def summarize_letters(processed_string):
    all_letters = string.ascii_lowercase
    length_all_letters = len(all_letters)
    all_punctuation = string.punctuation
    processed_string = processed_string.lower()

    letter_without_spaces = list(filter(lambda k: k != string.whitespace and k != ' ', list(processed_string)))
    letter_without_punctuation = list(filter(lambda j: j not in all_punctuation, letter_without_spaces))
    letter, freq = np.unique(letter_without_punctuation, return_counts=True)

    print(f'\n - > letters from the string:\n  "{processed_string}"', end="\n\n")
    print(f"{'-' * 10}")

    for i in range(len(letter)):
        print(f" {letter[i]}\t{freq[i]}\n{'-' * 10}")

    if len(letter) == length_all_letters:
        print(f"\nAll letters from alphabet have been used.", end="\n\n")
    else:
        print(f"\n - > Not all the letters from the alphabet have been used.", end="\n\n")


def main():
    summarize_letters(given_string)


main()

