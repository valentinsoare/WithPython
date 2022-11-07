#!/usr/bin/python

import os
import string
import random
import statistics
import numpy as np


def sorting_list(given_list_to_process):
    sort_list_ascending = sorted(given_list_to_process)
    sort_list_descending = sorted(given_list_to_process, reverse=True)

    print(f"\n - > * List in ascending order {sort_list_ascending}")
    print(f" - > ** List in descending order: {sort_list_descending}")


def remove_duplicates_and_sort(list_given):
    list_with_uniq_elements = []

    for i in list_given:
        if i not in list_with_uniq_elements:
            list_with_uniq_elements.append(i)

    print(f" - > *** List with uniq values and sorted: {list_with_uniq_elements}")


def summing_th_triples():
    given_list = list(i for i in range(2, 11))
    total_triples_even_integer = sum(map(lambda k: k * 3, filter(lambda j: j % 2 == 0, given_list)))

    print(f" * Triples of even integers: {total_triples_even_integer}")


def finding_name_people():
    given_names = [('Valentin', 'Jones'), ('John', 'Jones'), ('Emily', 'Jones'), ('Andrew', 'Smith'), ('Larwrence', 'McCoy'), ('Alexander', 'Jones')]
    filter_names = list(filter(lambda i: i[1].lower() == 'jones', given_names))

    print(f" * Names from the list with lastname 'Jones':", end=" ")

    for i in filter_names:
        print(f"({i[0]}, {i[1]}) ", end="")


def working_with_lists_duplicates():
    given_list = list(string.ascii_lowercase[0:6])
    list_to_process = list(given_list[random.randrange(0, 6, 1)] for _ in range(20))
    sorting_list(list_to_process)
    remove_duplicates_and_sort(given_list)


def print_in_tabular_format_v1():
    given_list_with_grades = [['Andrew', 4, 10, 9, 7, 23], ['Sonia', 10, 9, 6], ['Valentin', 2, 10, 9, 7], ['Emily', 10, 4, 8, 9, 6]]

    max_length_of_columns = max(list(map(lambda j: len(j), given_list_with_grades)))
    name_of_columns = ['First Name', 'Chemistry', 'English', 'Spanish', 'Math', 'Physics']

    print()
    print()
    for i in name_of_columns:
        print(f"{i:>13}", end="")

    print()
    for i in given_list_with_grades:
        for value in range(max_length_of_columns):
            try:
                match value:
                    case 0 | 1 | 2 | 3 | 4 | 5:
                        print(f"{i[value]:>13}", end="")
            except IndexError:
                print(f"{'None':>13}", end="")
        print()


def print_in_tabular_format_v2():
    given_list_with_grades = [['Andrew', [4, 10, 9, 7, 3]], ['Sonia', [10, 9, 6]], ['Valentin', [2, 10, 9, 7]],
                              ['Emily', [10, 4, 8, 9, 6]]]

    max_length_of_columns = max(list(map(lambda z: len(z[1]), given_list_with_grades)))
    list_with_headers = ['First Name', 'Chemistry', 'English', 'Spanish', 'Math']

    print(f"\n{' ' * 3}{list_with_headers[0]:<15}", end="")

    for header in range(len(list_with_headers)):
        print(f"{list_with_headers[header]:<15}", end="")

    print()

    for i in range(len(given_list_with_grades)):
        print(f"{given_list_with_grades[i][0]:>13}", end="")

        for j in range(max_length_of_columns):
            try:
                match j:
                    case 0 | 3:
                        print(f"{given_list_with_grades[i][1][j]:>15}", end="")
                    case 1:
                        print(f"{given_list_with_grades[i][1][j]:>14}", end="")
                    case 2:
                        print(f"{given_list_with_grades[i][1][j]:>13}", end="")
                    case 4 | 5:
                        print(f"{given_list_with_grades[i][1][j]:>12}", end="")
            except IndexError:
                if j == 3:
                    print(f"{'None':>15}", end="")
                elif j == 4:
                    print(f"{'None':>12}", end="")

        print()


def simulate_queue_with_a_list():
    given_list = []
    count = 0

    while count < 10:
        os.system('clear')
        print(f"\n{' ' * 4} ** {'Enqueuing 10 items:'}", end=" ")
        random_number = random.randrange(1, 10, 1)
        given_list.append(random_number)
        print(f"{given_list}")
        os.system('sleep 1')

        count += 1

    os.system('sleep 2')

    while count >= 0:
        os.system('clear')
        print(f"\n{' ' * 4} ** {'Dequeue all 10 items: '}{given_list}", end=" ")
        if count != 0:
            pop_item = given_list.pop(0)
            print(f"{' ' * 2} Pop item: {pop_item}")
        os.system('sleep 1')
        count -= 1

    print(f"{' ' * 4} ** Entire queue is depleted.")


def duplication_elimination_and_counting_freq():
    generate_50_numbers = np.random.randint(1, 11, size=50)
    integers_values, integers_count = np.unique(generate_50_numbers, return_counts=True)

    print(f"\n - > Generated values: {integers_values}")
    print(f" - > Count values: {integers_count}")


def survey_response_stats():
    twenty_response = np.random.randint(1, 6, size=20)
    values, counts = np.unique(twenty_response, return_counts=True)
    counts = list(counts)

    print(f"\n\n * All values: {values}")
    print(f" * Counter: {counts}")

    calc_mean = statistics.mean(counts)
    calc_median = statistics.median(counts)
    calc_mode = statistics.mode(counts)
    calc_range = [values[0], values[len(values) - 1]]

    calc_min = values[counts.index(min(counts))]
    calc_max = values[counts.index(max(counts))]

    print(f" * Element with minimum appearances: {calc_min}")
    print(f" * Element with maximum appearances: {calc_max}")
    print(f" * Average of appearances: {calc_mean}")
    print(f" * Median: {calc_median}")
    print(f" * Mode: {calc_mode}")
    print(f" * Range: {calc_range}")


def visualizing_survey_response_statistics():
    twenty_response = np.random.randint(1, 6, size=20)
    values, counts = np.unique(twenty_response, return_counts=True)
    counts = list(counts)

    paired_values = list((values[i], counts[i]) for i in range(len(values)))

    print(f"\n\n < - > Answers: {values} ")
    print(f" < - > Counting answers and put them in categories: {counts} ")

    print(f"\n{'Answer':>12}{'Percent':>13}{'Barchart':>15}")

    for i in paired_values:
        value, count = i
        print(f"{value:>12}{((count/len(twenty_response)) * 100):>12}%{' ' * 7}{('#' * count)}")


def coin_tossing():
    responses = np.random.randint(1, 3, size=2_000_000)
    values, count = np.unique(responses, return_counts=True)
    list_with_values_and_count = list((values[i], count[i]) for i in range(len(values)))

    print(f"\n\n{'* Coin value':>13}{'Frequency':>13}{'Percent':>13}{'Barchart':>15}")

    for i in list_with_values_and_count:
        value, count = i
        print(f"{value:>13}{count:>13}{((count/len(responses)) * 100):>12.2f}%{' ' * 7}{'#' * int((count/len(responses)) * 100)}")


def main():
    working_with_lists_duplicates()
    summing_th_triples()
    finding_name_people()
    print_in_tabular_format_v1()
    print_in_tabular_format_v2()
    simulate_queue_with_a_list()
    duplication_elimination_and_counting_freq()
    survey_response_stats()
    visualizing_survey_response_statistics()
    coin_tossing()


if __name__ == '__main__':
    main()
