#!/usr/bin/python

grades_in_points = [98, 40, 78, 67, 19, 45]
students = ["George", "Andrei", "Maria", "Irina", "Alina", "Violeta"]

students_grades = []
length_students = len(students)

for i in range(length_students):
    students_grades += [(students[i], grades_in_points[i])]

print(f'\nStudent{"Grade":>11}\tBar')

#grade was split in two in order for those lines to be shorter

for name, grade in students_grades:
    print(f'{f"[{name}]":<13}{f"[{grade}]":<5}\t[{"*" * (grade//2)}]')

print()

