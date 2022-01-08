#!/usr/bin/python

import operator
import collections

given_string = ('A market economy is an economy where private and public ownership of businesses is the norm. Laborers and workers work for these companies. Land, buildings, materials, resources, and money are owned by businesses and consumers.'
                'These entities can conduct business with each other as they see necessary, and consumers can buy and sell at their discretion. Businesses sell their products and services at the highest price consumers will pay. Prices are also determined by competition. If one business sells something for $2.00, a business selling the same item might charge $1.95 to attract more shoppers.'
                'This competition lets people and other businesses look for the lowest prices they can find. Workers promote their skills and services at the highest possible wages they can attract—employers seek to get the most skilled employees at the lowest possible wages.')


def counting_words(given_string_text):
    counting_dict = {}

    for i in given_string_text.split():
        if i in counting_dict:
            counting_dict[i] += 1
        else:
            counting_dict[i] = 1

    return counting_dict


def determine_number_of_uniq_words(given_dict_with_count):

    print(f'\n\033[1m{"WORD":<18}{"COUNT"}\033[0m')
    for i, j in sorted(given_dict_with_count.items(), key=operator.itemgetter(1)):
        print(f"{i:<17} {j}", end="\n")


def determine_counting_another_method(given_string):
    return collections.Counter(given_string.split())


def main():
    #dict_with_count = counting_words(given_string)
    #or

    dict_with_count = collections.Counter(given_string.split())
    determine_number_of_uniq_words(dict_with_count)


main()
