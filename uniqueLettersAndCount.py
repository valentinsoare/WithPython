#!/usr/bin/python

import string
import numpy as np


given_string = 'Sa      fie bine si sa nu fie rau !!!'


def summarize_letters(processed_string):
    all_letters = string.ascii_lowercase
    length_all_letters = len(all_letters)
    all_punctuation = string.punctuation
    processed_string = processed_string.lower()

    letter_without_spaces = list(filter(lambda i: i != string.whitespace and i != ' ', list(processed_string)))
    letter_without_punctuation = [letter_without_spaces[i] for i in range(len(letter_without_spaces)) if letter_without_spaces[i] not in all_punctuation]
    letter, freq = np.unique(letter_without_punctuation, return_counts=True)

    print(f'\n - > letters from the string:\n  "{processed_string}"', end="\n\n")
    print(f"{'-' * 10}")
    for i in range(len(letter)):
        print(f" {letter[i]}\t\t{freq[i]}\n{'-' * 10}")

    if len(letter) == length_all_letters:
        print(f"\nAll letters from alphabet have been used.", end="\n\n")
    else:
        print(f"\n - > Not all the letters from the alphabet have been used.", end="\n\n")


def main():
    summarize_letters(given_string)


main()

