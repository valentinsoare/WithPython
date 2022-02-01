#!/usr/bin/python
import string


def catch_input_sentence():
    print(f"\n\033[1m - > Enter sentence to reverse it: ", end="\033[0m")
    given_sentence = input()

    splitting_sentence = given_sentence.split()

    return splitting_sentence


def main():
    splited_sentence = catch_input_sentence()
    length_sentence = (len(splited_sentence) - 1)
    reversed_sentence = ''

    for i in range(length_sentence, -1, -1):
        word = ''
        for j in splited_sentence[i]:
            if j not in string.punctuation:
                word += j

        if i == length_sentence:
            reversed_sentence += ' ' + word.title()
        else:
            reversed_sentence += ' ' + word.lower()

    last_word_punct = splited_sentence[len(splited_sentence) - 1]
    reversed_sentence += last_word_punct[len(last_word_punct) - 1]

    print(f"\n\033[1m - > Sentence in reversed:\033[0m {reversed_sentence}", end="\n\n")


main()
