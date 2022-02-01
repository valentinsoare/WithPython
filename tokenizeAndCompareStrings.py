#!/usr/bin/python


def catch_input_and_split():
    print(f"\033[1m\n - > Please enter your sentence/phrase to find words there starting with letter b.\033[0m", end="\n")
    print(f"\033[1m\t\tSentence:", end=" ")
    given_sentence = input()

    return given_sentence.split()


def check_for_b(given_word):
    type_letter = 0

    if given_word.istitle():
        type_letter = 1
        given_word = given_word.lower()

    if given_word[0] == 'b':
        if type_letter == 1:
            return given_word.title()
        else:
            return given_word

    return 1


def check_for_ed(word_given):
    x = ''.join(reversed(list(word_given[-1:-3:-1])))
    if x == 'ed':
        return word_given

    return 1


def main():
    list_of_words = catch_input_and_split()
    with_b = []
    with_ed = []

    for i in list_of_words:
        x = check_for_b(i)
        if x != 1:
            with_b += [x]

        y = check_for_ed(i)
        if y != 1:
            with_ed += [y]

    if len(with_b) != 0:
        print(f"\n\033[1m - > WORDS from given sentence that begin with letter b:\033[0m \033[1;31m{with_b}\033[0m")

    if len(with_ed) != 0:
        print(f"\n\033[1m - > WORDS that ends with ed:\033[0m \033[1;31m{with_ed}\033[0m")


main()
