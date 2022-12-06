#!/usr/bin/python

import os
import random


def printing_header(given_message):
    message_to_use = given_message.split()
    message_to_use = ' '.join(i.capitalize() for i in message_to_use)

    line_to_draw = f"{'-' * (2 * len(message_to_use))}"

    print(f"\n{' ' * 20}{message_to_use:^{len(line_to_draw)}}")
    print(f"{' ' * 20}{line_to_draw}")


def create_sentence():
    article = ['a', 'an', 'the']
    noun = ['time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world', 'people', 'earth', 'water', 'car']
    verb = ['accept', 'bring', 'fly', 'hop', 'run', 'work', 'swim', 'generate', 'concatenate']
    preposition = ['in', 'on', 'at', 'of', 'to', 'by', 'with']

    arhitecture_of_sentence = [article, noun, verb, preposition, article, noun]

    sentence = ''

    for i in range(len(arhitecture_of_sentence)):
        location = random.randrange(0, len(arhitecture_of_sentence[i]))
        if i == 0:
            sentence += arhitecture_of_sentence[i][location].capitalize()
        elif i == len(arhitecture_of_sentence) - 1:
            sentence += ' ' + arhitecture_of_sentence[i][location] + '.'
        else:
            sentence += ' ' + arhitecture_of_sentence[i][location]

    return sentence


def printing_sentence(nr_of_sentences_wanted):
    i = 0

    while i < nr_of_sentences_wanted:
        sentence_to_use = create_sentence()
        print(f"{' ' * 32}{(i + 1):>{len(str(nr_of_sentences_wanted))}}. {sentence_to_use}")
        i += 1


def main():
    printing_header('random sentences generator')
    printing_sentence(10)


if __name__ == '__main__':
    main()
