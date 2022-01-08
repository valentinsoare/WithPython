#!/usr/bin/python

import operator


def calc_average_per_student(grade_book):
    averages_students = {}
    number_of_grades_per_grade_book = 0
    sum_for_average_class = 0

    for student, grades in grade_book.items():
        averages_students[student] = sum(grades) / len(grades)
        sum_for_average_class += sum(grades)
        number_of_grades_per_grade_book += len(grades)

    average_class = sum_for_average_class / number_of_grades_per_grade_book

    return averages_students, average_class


def printing_averages(averages_for_students, average_class):

    print(f"\n - > Averages per student in sorted order", end="\n")
    students_averages = dict(sorted(averages_for_students.items(), key=operator.itemgetter(1), reverse=True))

    for i, j in students_averages.items():
        print(f"\t| {i:<10} | {j:.1f}")

    print(f"\n - > Average on entire class: {average_class:.2f}", end="\n\n")


def printing_grades_book(grades_book_given):

    print(f"\n - > Grades per student in sorted order:", end="\n")
    for i, j in grades_book_given.items():
        print(f"\t| {i:<10} |", end="\t")
        for k in sorted(j):
            print(f"{k}", end=" ")
        print()


def main():
    given_grade_book = {'Gabriela': [9.2, 8.5, 9.3, 10],
                        'Valentin': [7.2, 9.4, 8, 8.2],
                        'Andreea': [6, 7.2, 8.3, 9.4],
                        'Andrei': [9.8, 8.4, 6.9, 7.5]
                        }

    printing_grades_book(given_grade_book)
    students_averages, average_per_entire_class = calc_average_per_student(given_grade_book)
    printing_averages(students_averages, average_per_entire_class)


main()
