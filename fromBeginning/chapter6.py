#!/usr/bin/python

import collections
import operator
import os
import string

import numpy as np
import pandas as pd
from collections import Counter


def various_exercises():
    #country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Romania': 'ro',
    #                 'United Kingdom': 'uk', 'Germany': 'de', 'France': 'fr'}
    #sorted_dict_country_codes = dict(sorted(country_codes.items(), key=lambda i: i[0]))

    #roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}

    #var = 'III'
    #print(roman_numerals['II'])

    #if var in roman_numerals:
    #    print(f"AAAAAaaaa")

    #roman_numerals['L'] = 50
    #print(f"\n{roman_numerals}")

    #del roman_numerals['III']
    #print(roman_numerals)


    #count = 0
    #length_of_sorted_dict = len(sorted_dict_country_codes)

    #-----------------------------------

    #while count < length_of_sorted_dict:
    #    print(f"^* {sorted_dict_country_codes}")
    #    element_to_pop = sorted_dict_country_codes.pop()
    #    print(f" * Element to pop: {element_to_pop}, count: {count + 1}")

    #    os.system('sleep 1')
    #    count += 1

    #----------------[

    #search_for_key = sorted_dict_country_codes.get('United Kingdom')
    #print(search_for_key)

    #------------------

    #if 'germany' in sorted_dict_country_codes:
    #    print(f"{sorted_dict_country_codes['germany']}")

    #-------------------

    #keys_dict = sorted_dict_country_codes.keys()
    #values_dict = sorted_dict_country_codes.values()

    #reverse_key_value = collections.UserDict(map(lambda i: (i[1], i[0]), sorted_dict_country_codes.items()))

    #reverse_values_view = reverse_key_value.keys()
    #print(reverse_values_view)

    #reverse_key_value['pl'] = 'Poland'
    #print(reverse_key_value)

    #--------------------------------------------------------------
    #country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Romania': 'ro',
    #                 'United Kingdom': 'uk', 'Germany': 'de', 'France': 'fr'}
    #sorted_dict_country_codes = dict(sorted(map(lambda i: (i[0].lower(), i[1]), country_codes.items())))
    #reverse_key_value = dict(map(lambda i: (i[1], i[0]), sorted_dict_country_codes.items()))
    #print(sorted_dict_country_codes)

    #for i in sorted(country_codes.keys()):
    #    print(f"{i}")

    #----------------------------------------------------------------

    #roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}

    #list_of_keys = list(roman_numerals.keys())
    #list_of_values = list(roman_numerals.values())
    #list_of_items = list(roman_numerals.items())

    #print(f"List of keys: {list_of_keys}")
    #print(f"List of values: {list_of_values}")
    #print(f"List of items: {list_of_items}")

    #----------------------------------------------------------------

    #country_capitals_1 = {'Romania': 'Bucharest', 'France': 'Paris', "England": 'London'}
    #country_capitals_2 = {'Germany': 'Berlin', 'Hungary': 'Budapest'}
    #country_capitals_3 = {'France': 'Paris', "England": 'London', 'Romania': 'Bucharest'}

    #if country_capitals_1 == country_capitals_3:
    #    print(f"1 is the same with 3")

    #if country_capitals_2 != country_capitals_3:
    #    print(f"2 and 3 are different")

    #------------------------------------------------------------------

    #given_list = np.random.randint(1, 6, 50)
    #to_count = Counter(given_list)
    #sorted_dict = sorted(to_count.items(), key=lambda i: i[1], reverse=True)

    #print(f"{'Value':<15}{'Count'}")

    #for value, count in sorted_dict:
    #    print(f"{value:<15}{count}")

    #--------------------------------------[

    #country_codes = {}

    #country_codes.update({'South Africa': 'za'})
    #country_codes.update({'Romania': 'ro', 'United Kingdom': 'uk'})
    #country_codes.update({'Romania': 'RO'})
    #country_codes.update(Romania='ro')
    #country_codes.update([('Germany', 'de'), ('France', 'fr')])

    #print(country_codes)

    #------------------------------

    #months = {'January': 1, 'February': 2, 'March': 3}
    #emonth_changed = {number: name for name, number in months.items()}
    #month_changed = dict(map(lambda j: (j[1], j[0]), filter(lambda k: k, tuple(months.items()))))

    #grades = {'Sue': [78, 87, 94], 'Bob': [84, 95, 91]}
    #grades_average = dict(map(lambda k: (k[0], float(f"{sum(k[1])/len(k[1]):.2f}")), filter(lambda i: i, grades.items())))

    #print(grades_average)

    #-----------------------------

    #dict_cubes = {i: i**3 for i in range(1, 6)}
    #print(dict_cubes)

    #-----------------------------
    #colors = {'red', 'blue', 'yellow', 'green', 'red', 'blue'}

    #given_text = 'to be or not to be that is the question'
    #our_set = set(given_text.split())

    #print(sorted(our_set))

    #-----------------------------

    #if {3, 5, 1} < {1, 3, 5, 10}:
    #    print(f"True")

    #if {1, 3, 5}.issubset({1, 3, 5, 10, 40}):
    #    print(f"True")

    #if {4, 10, 2, 20}.issuperset({4, 20}):
    #    print(f"True")

    #if {20, 3, 10}.isdisjoint({4, 23}):
    #    print(f"True")

    #----------------------------

    #given_string = 'abc def ghi  jkl mno'
    #given_string_1 = 'hi mom'

    #given_string = set(map(lambda j: j.strip(), set(given_string)))
    #given_string_1 = set(map(lambda k: k.strip(), set(given_string_1)))

    #if given_string.issuperset(given_string_1):
    #    print(f"True")

    #-----------------------------

    #ax = {4, 10, 2}.union({100, 9, 2})
    #print(ax)

    #ay = {4, 10, 2}.intersection([200, 4, 19])
    #print(ay)

    #az = {19, 10, 2}.difference([201, 14, 2, 10])
    #print(az)

    #at = {19, 10, 2, 14}.symmetric_difference([201, 14, 2, 10])
    #print(at)

    #-----------------------------

    #set_1 = {10, 20, 30}
    #set_2 = {5, 10, 15, 20}

    #result_difference = set_1.difference(set_2)
    #print(result_difference)

    #result_symetric_difference = set_1.symmetric_difference(set_2)
    #print(result_symetric_difference)

    #result_union = set_1.union(set_2)
    #print(result_union)

    #result_intersection = set_1.intersection(set_2)
    #print(result_intersection)

    #-------------------------------
    #x = {3, 12, 20}

    #x.intersection_update([10, 20, 4])
    #y = x.intersection([10, 20, 4])
    #x.update(range(1, 11))

    #x.add(101)

    #x.remove(20)
    #x.discard(101)

    #x.clear()

    #print(x)

    #--------------------------------

    #given_numbers = np.random.randint(1, 11, 20)
    #given_numbers_set = sorted({i for i in given_numbers if i % 2 == 0})

    #print(given_numbers_set)

    #----------------------------------------



def main():
    various_exercises()


if __name__ == '__main__':
    main()

