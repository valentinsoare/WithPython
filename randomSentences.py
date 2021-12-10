#!/usr/bin/python3

from collections import Counter
import operator
import random
import re

given_text = """The best cinematic performances don’t share some standard of craft or technique; what they have in common
is a feeling of invention and discovery, of emotional depth and power, and a sense of self-consciousness regarding the idea and the art of performance itself. 
They also reflect broader transformations in the art of cinema during their times. Such actors as Joan Crawford, Barbara Stanwyck, and Jimmy Stewart were already stars 
in the high studio era of the nineteen-thirties, but their work became more freely expressive, more galvanic, in the postwar years, when the studios lost their tight grip on 
production—and when a new generation of directors made their mark in that freer environment. The French New Wave, developing new techniques with a new generation of actors (and crew), 
lifted layers of varnish from the art of acting to fill the screen with performances of jolting immediacy, spontaneity, and vulnerability.

The film performances of the beginning of the twenty-first century are a product of the drastic transformations that have taken place in 
moviemaking in recent decades, as a new generation of directors, both in Hollywood and outside of it, has managed to invent modes of moviemaking capable of adapting to unprecedented crises 
in the industry. The competition from television (“prestige” or otherwise), the top-heavy expansion of blockbuster franchises, and the rise of streaming platforms have led to a decline in 
studio movie production. As a result, independent producers have grown significantly in prominence and power, and their financing has had a liberating effect on directors, and, by extension, 
on actors: working largely with modest budgets (yet occasionally with larger ones than studios would provide), filmmakers have been able to take greater risks and make more unusual films—and 
to develop new methods of performance with actors whose artistry closely fits their own.

Equally relevant is the ready availability of inexpensive yet (relatively) high-definition video, which has helped to democratize filmmaking, putting the power of image-making into the
hands both of young directors starting out and of experienced ones changing course. The ultra-low-budget filmmakers lumped together as mumblecore rebuilt acting from the ground up, 
working with locals and friends, borrowing the manner and tone of personal documentaries, home videos, and YouTubers—and developing new styles on the basis of the people whose personalities
they revealed and spotlighted, such as Greta Gerwig, Helena Howard, and Adam Driver, all of whom displayed astonishing new emotional range and realms. (The rapidity of changes in American 
film production, and of independents’ response to them, is part of why my list features predominantly actors in American movies."""


def processed_text(text):
    pattern = r'[^\w]'
    rtn_text = re.sub(pattern, ' ', text)
    return rtn_text


def analysing_given_text(given_text):
    counting_words_appearances = Counter(given_text.split())
    list_was_analyzed = sorted(counting_words_appearances.items(), key=operator.itemgetter(1))

    print(f'\n\033[1m*Words used three times or more in the given text:\033[0m')

    counting_prints = 0
    counting_commas = 0

    print(f'\033[1;31m[\033[0m', end=' ')

    for i in range(len(list_was_analyzed)):
        if list_was_analyzed[i][1] >= 3:

            counting_prints += 1

            if counting_commas == 11:
                print(f'{list_was_analyzed[i][0]}: {list_was_analyzed[i][1]}', end='')
            elif list_was_analyzed[i] == list_was_analyzed[len(list_was_analyzed) - 1]:
                print(f'{list_was_analyzed[i][0]}: {list_was_analyzed[i][1]}', end='')
            else:
                print(f'{list_was_analyzed[i][0]}: {list_was_analyzed[i][1]}', end=', ')

            counting_commas += 1

            if counting_prints % 12 == 0:
                counting_prints = 0
                counting_commas = 0
                print()
                print(" ", end=' ')

    print(f'\033[1;31m ]\033[0m')


def form_phrases_with_random_words(given_text):
    text_for_processing = processed_text(given_text)
    processed_words = [i.lower() for i in set(text_for_processing.split())]
    text_length = len(processed_words) - 1

    i = 0
    phrase = ''

    while i < 5:
        rnd = random.randint(0, text_length)

        if i == 0:
            phrase += processed_words[rnd].capitalize()
        elif i == 4:
            phrase += ' ' + processed_words[rnd] + '. '
            break
        else:
            phrase += ' ' + processed_words[rnd]

        i += 1

    print(f'\n\033[1m*Phrase with five words created by using random generator:\033[0m')
    print(f'\033[1;31m[ \033[0m{phrase}\033[1;31m]\033[0m')


analysing_given_text(given_text)
form_phrases_with_random_words(given_text)
