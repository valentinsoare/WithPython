#!/usr/bin/python

import numpy as np
import pandas as pd
from collections import Counter


def calculate_avg():
    grades_from_exams = np.array(np.random.randint(60, 101, 12).reshape((3, 4)))
    print(f"\n* Grades from the exams:")

    def calc_average(given_array, type_of_axis):
        for k in given_array.mean(axis=type_of_axis):
            print(f"{k:.2f}", end=" ")

    for i in range(len(grades_from_exams)):
        print(f"{' ' * 1}", end="")
        for j in range(len(grades_from_exams[i])):
            print(f"{grades_from_exams[i][j]:>3}", end=" ")
        print()

    print(f"\n - > Average per each exam:", end=" ")
    calc_average(grades_from_exams, type_of_axis=0)

    print(f"\n - > Average per student:", end=" ")
    calc_average(grades_from_exams, type_of_axis=1)


def filling_arrays():
    two_by_three = np.ones((2, 3))
    print(f"\n{two_by_three}")

    three_by_three = np.zeros((3, 3))
    two_by_five = np.full((2, 5), 7)
    print(f"\n{three_by_three}\n\n{two_by_five}")

    empty_np_array = np.empty(7, dtype=str)
    print(empty_np_array)


def broadcasting():
    two_by_two = np.arange(4).reshape((2, 2))
    cube_elements = two_by_two ** 3
    adding_seven = two_by_two + 7
    multiply_by_two = two_by_two * 2


def multiplication():
    three_by_three = np.arange(2, 19, 2).reshape((3, 3))
    three_by_three_reverse = np.arange(9, 0, -1).reshape((3, 3))

    multiplication_opr = three_by_three * three_by_three_reverse
    print(multiplication_opr)


def list_of_lists():
    given_list = [[2, 3, 5, 7, 11], [13, 17, 19, 23, 29]]
    array_two_by_five = np.array(given_list)

    print(array_two_by_five)


def method_astype():
    future_two_by_three = np.array(np.linspace(1.1, 6.6, num=6).reshape(2, 3))
    two_by_three_converted_to_integers = future_two_by_three.astype(dtype=int, copy=True)

    print(f"*Before conversion:\n {future_two_by_three}\n")
    print(f"**After conversion:\n {two_by_three_converted_to_integers}")


def flattening_arrays():
    six_elements_power_of_two = np.array(list(2 ** i for i in np.arange(6)))
    two_by_three = np.array(six_elements_power_of_two.reshape(2, 3))

    print(f"\n*After creation:\n{two_by_three}")

    flatten_array = two_by_three.flatten()
    print(f"\n**With flatten: {flatten_array}")

    ravel_array = two_by_three.ravel()
    print(f"**With ravel: {ravel_array}")

    print(id(two_by_three))
    print(id(flatten_array))
    print(id(ravel_array))

    flatten_array[0] = 100
    ravel_array[0] = 100

    print(two_by_three)


def numpy_array_output():
    given_numpy_array = np.array(list(i for i in np.random.randint(80, 150, 16)))
    numpy_array = np.array(given_numpy_array.reshape(4, 4))

    longest_element = len(str(numpy_array.max()))

    print(f"\n * printing numpy style, right allign:\n")

    print(f"{' ' * 5}", end="")
    for row in numpy_array:
        for element in row:
            print(f"{element:>{longest_element}}", end=" ")
        print(f"\n{' ' * 5}", end="")


def pandas_dataframe_output_like():
    grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90],
                   'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}

    list_with_fields = ['Math', 'English', 'Chemistry']
    pandas_grades = pd.DataFrame(grades_dict.values(), index=grades_dict.keys(), columns=list_with_fields)
    print(pandas_grades)

    longest_key_dict = max(list(len(i) for i in grades_dict.keys()))

    print(f"{' ' * (longest_key_dict + 2)}", end="")

    for i in range(len(list_with_fields)):
        print(f"{list_with_fields[i]:>{len(list_with_fields[i]) + 2}}", end="")

    print()
    for name, grades in grades_dict.items():
        print(f"{name:<{longest_key_dict + 2}}", end="")
        for value in range(len(grades)):
            print(f"{grades[value]:>{len(list_with_fields[value]) + 2}}", end="")
        print()


def indexing_and_slicing():
    giving_array = np.array(np.random.randint(1, 16, 15).reshape(3, 5))
    print(f"{giving_array}")

    print(f"\n{giving_array[1]}")
    print(f"\n{giving_array[:, 4]}")

    print(f"{giving_array[0:2]}")

    print(f"\n{giving_array[:, 1:4]}")

    print(f"\n{giving_array[1, 4]}")

    print(f"{giving_array[0:2, [0, 2, 4]]}")


def broadcasting_capabilities():
    given_array = np.random.randint(1, 9, 20)
    new_arr = given_array * 2
    old_arr = np.array([2, 3])
    next_version = np.full(20, 10)
    print(f"{given_array * next_version}")

def stacking():
    array_1 = np.array([[0, 1], [2, 3]])
    array_2 = np.array([[4, 5], [6, 7]])

    array_3 = np.vstack([array_1, array_2])
    print(array_3)

    array_4 = np.hstack([array_1, array_2])
    print(array_4)

    array_5 = np.vstack([array_4, array_4])
    print(array_5)

    array_6 = np.hstack([array_3, array_3])
    print(array_6)


def to_concatenate():
    first_array = np.array(np.random.randint(1, 9, 20).reshape(4, 5))
    second_array = np.array(np.random.randint(21, 29, 10).reshape(2, 5))

    concatenated_array = np.concatenate([first_array, second_array], axis=0)

    print(f"{first_array}\nNEBUNIE\n{second_array}\n\n\n\n{concatenated_array}")


def count_negative():
    given_integers = np.array(np.random.randint(-99, 99, 25).reshape(5, 5))
    values, counting_digits = np.unique(given_integers, return_counts=True)

    print(f"\n * Given Array with Positive and Negative Integers:\n{given_integers}")
    count_negative = 0
    dict_with_appearances = {}

    for i in range(len(values)):
        if values[i] < 0:
            dict_with_appearances[values[i]] = counting_digits[i]
            count_negative += 1

    print(f"\n * How many negative numbers: {count_negative}")
    print(f"\n * Frequency of negative numbers:\n{dict_with_appearances}")


def median_numpy_array(given_numpy_array):
    median_value = 0
    array_to_work_with = np.array(given_numpy_array)
    print(f"\n ** Given numpy array\n to calculate median.\n{given_numpy_array}")

    if len(np.shape(given_numpy_array)) == 2:
        array_to_work_with = array_to_work_with.ravel()
        print(f"\n * Raveled array:\n{array_to_work_with}\n")

    if len(array_to_work_with) == 0:
        print(f" * No elements in the array.")
        exit(1)
    elif len(array_to_work_with) == 1:
        median_value = array_to_work_with[0]
    elif len(array_to_work_with) % 2 != 0:
        median_value = array_to_work_with[(len(array_to_work_with) // 2)]
    else:
        median_value = array_to_work_with[int(len(array_to_work_with) / 2)]

    return median_value


def mode_numpy_array(given_array):
    array_to_work_with = np.array(given_array)

    print(f" * * Given array:\n{array_to_work_with}")

    if len(array_to_work_with) == 0:
        print(f" ERROR * array is empty")
        exit(0)

    values, counting = np.unique(array_to_work_with, return_counts=True)
    most_frequent = max(counting)

    return values[list(counting).index(most_frequent)]


def main():
    #calculate_avg()
    #filling_arrays()
    #broadcasting()
    #multiplication()
    #list_of_lists()
    #flattening_arrays()
    #method_astype()
    #numpy_array_output()
    #pandas_dataframe_output_like()
    #indexing_and_slicing()
    #broadcasting_capabilities()
    #stacking()
    #to_concatenate()
    #count_negative()
    #calc_median = median_numpy_array(np.array(np.random.randint(1, 10, 9)))
    #print(f"Median: {calc_median}")
    mode_calc = mode_numpy_array(np.random.randint(1, 10, 12).reshape(3, 4))
    eprint(f"\nMode calc: {mode_calc}")



if __name__ == '__main__':
    main()
