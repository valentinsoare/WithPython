#!/usr/bin/python

import itertools

string = "IUBIRE"


def produce_anagrams(given_string):
    length_of_string = len(given_string)
    list_from_string = list(given_string)
    return list(itertools.permutations(list_from_string, length_of_string))


def main():
    generated_anagrams = produce_anagrams(string)
    print(f'\n - > Anagrams for {string}: ', end="\n\n")

    count = 0
    for i in generated_anagrams:
        for j in i:
            print(f"{j}", end=" ")

        if count == 2:
            count = 0
            print()
        else:
            print(f", ", end="")
            count += 1


main()

