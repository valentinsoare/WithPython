#!/usr/bin/python

import itertools

# easy approach with libraries and prebuilt functions


def generate_anagram(given_string):
    generated_anagrams = list(''.join(i) for i in itertools.permutations(given_string))
    return generated_anagrams


def main():
    anagrams_generated_from_word = list(generate_anagram('nebunie'))
    print(anagrams_generated_from_word)


if __name__ == '__main__':
    main()
