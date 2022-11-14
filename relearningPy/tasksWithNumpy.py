#!/usr/bin/python

import numpy as np


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


def main():
    #calculate_avg()
    #filling_arrays()
    



if __name__ == '__main__':
    main()
