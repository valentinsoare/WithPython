#!/usr/bin/python

import random
import operator
import statistics
import numpy as np


def generated_list(number_of_answers=20, scale_for_answers=5):
    list_to_return = [random.randrange(1, (scale_for_answers + 1)) for i in range(number_of_answers)]
    print(f"\n*List of grades: {list_to_return}", end="\n")
    return list_to_return


def freq_of_elements(answers_list):
    elements, freq = np.unique(answers_list, return_counts=True)
    print(f"\n- > Grades and frequencies: ", end="\n\n")

    for element, count in zip(elements, freq):
        print(f"Grade: {element:<2} frequency: {count}")

    return elements, freq


def printing_statistics(given_list, freq_of, elements_given):
    combine_them = list(zip(elements_given, freq_of))
    values_max = max(list(map(operator.itemgetter(1), combine_them)))
    values_min = min(list(map(operator.itemgetter(1), combine_them)))

    print(f"\n*Max grade: {max(given_list)}")
    print(f"*Min grade: {min(given_list)}")

    def max_min(given_zipped_list, value, type_given):
        for i in given_zipped_list:
            k, m = i
            if value == m:
                print(f"*{type_given} of grades by appearances: {i} ")
                return k, m

    max_value = max_min(combine_them, values_max, 'Max')
    min_value = max_min(combine_them, values_min, 'Min')

    print(f"*Ranges of grades/appearances: {min_value} - {max_value}", end="\n")
    print(f"*Ranges of grades: {min(given_list)} - {max(given_list)}")
    print(f"*Grades mean: {statistics.mean(given_list)}")
    print(f"*Median: {statistics.median(given_list)}")
    print(f"*Mode: {statistics.mode(given_list)}")
    print(f"*Variance: {statistics.variance(given_list):.2f}")
    print(f"*Standard deviation: {statistics.stdev(given_list):.2f}", end="\n\n")


def main():
    list_of_answers = generated_list(20, 10)
    elements, frequency_of_elements = freq_of_elements(list_of_answers)
    printing_statistics(list_of_answers, frequency_of_elements, elements)


main()
