#!/usr/bin/python

import string
import random
import dynArray
import fixedArray
import stackArray
import queueArray
import numpy as np
import pandas as pd


def main():
    classes = fixedArray.FixedArray(['math', 'physics', 'chemistry', 'object oriented programming', 'english'])
    classes_to_dict = {j.title(): i for i, j in classes.fixed_to_dict(given_keys=[classes[i][0] for i in range(len(classes))]).items()}
    grades = fixedArray.FixedArray([[9, 10, 6.4, 8, 7, 9, 8.6], [10, 8, 6, 9.4, 7, 10], [8, 6, 10, 8, 9, 9, 6],
                                    [10, 9, 7, 8, 9, 10], [8, 6, 10, 10, 9, 7, 8, 9]])

    classes_grades_df = pd.DataFrame({i: grades[i] for i in range(len(grades))}.values(), index=classes_to_dict.keys(),
                                     columns=['Andrew', 'Michele', 'Valentin', 'Jack', 'Richard', 'Kim', 'Kelly', 'David'])
    initial_data_frame = classes_grades_df
    classes_grades_df = classes_grades_df.transpose()

    print(f'\n\033[1m{"**Classes and Grades**":>45}\033[0m\n')
    print(f'{classes_grades_df}')

    print(f'\n\n\033[1m{"**Stats on given table**":>47}\033[0m\n')
    print(f' - Number of students: {len(classes_grades_df.keys()):>2}')
    print(f' - Number of classes: {len(classes_grades_df.values):>3}')

    print(f' - Average per student:', end="")
    print(f'\n   {"-" * 45}', end="")

    count = 0
    for i, j in initial_data_frame.items():
        if count % 3 == 0:
            print()
        print(f'{" ":>3}{i}{": "}{j.values.mean()}', end=" ")
        count += 1

    print(f'\n   {"-" * 45}', end="\n\n")

    ###-------------------------queue running
    print(f'{"=" * 80}', end="\n\n")

    given_queue = queueArray.QueueArray()

    n = 0
    while n < 9:
        number_to_add = random.randint(0, 100)
        given_queue.enqueue(number_to_add)
        n += 1

    print(given_queue)

    value_x = given_queue.dequeue()
    print(value_x)
    print(f'{given_queue}', end="\n\n")

    value_y = given_queue.dequeue()
    print(value_y)
    print(f'{given_queue}', end="\n\n")


if __name__ == '__main__':
    main()
