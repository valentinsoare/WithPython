#!/usr/bin/python

from course import Course


def main():
    first_course = Course(name_of_course='Math', min_grade=1, max_grade=10)
    first_course.add_grade_per_course([10, 9, 6])
    first_course.add_grade_per_course({4, 10, 2})

    first_course.add_grade_per_course(4, 10)
    first_course.add_grade_per_course('8 5 10 1')

    after_mod = first_course.edit_grade_per_course(old_grade=22, new_grade=1, date_grade='2023-02-05', index_grade=2)


if __name__ == '__main__':
    main()

