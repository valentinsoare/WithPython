# gradebook.py

from re import split
from time import sleep
from typing import Union
from datetime import date
from random import randint
from .course import Course
from .student import Student
from collections import namedtuple
from .variousCheckings import _check_if_str, _check_if_numeric, \
    _for_name_checking, _working_on_grades_from_add


def generate_student_id(name: str, students: dict) -> str:
    message_to_use = 'POL1007'

    if type(name) != str:
        return message_to_use
    else:
        name_split = split(r',\s*', name)
        if len(name_split) != 2:
            print(f"\n{' ' * 3} \033[31mPOL1007 - Student name should contain first and last name separated by a "
                  f"comma or a comma and a space!\033[0m\n")
            sleep(2)
            return message_to_use
        else:
            while True:
                _id = name_split[0][0].upper() + name_split[1][0].upper() + str(randint(10000, 99999))
                if _id not in students:
                    return _id


class GradeBook:
    def __init__(self, students_class_name, number_of_students, class_master):
        self._students_class_name = students_class_name
        self._number_of_students = number_of_students
        self._class_master = class_master
        self._grades: dict = {}
        self._students: dict = {}
        self._courses: dict = {}

    @property
    def students_class_name(self) -> str:
        return self._students_class_name

    @students_class_name.setter
    def students_class_name(self, students_class_name) -> None:
        self._students_class_name = _check_if_str(students_class_name)

    @property
    def number_of_students(self) -> int:
        return self._number_of_students

    @number_of_students.setter
    def number_of_students(self, number_of_students) -> None:
        self._number_of_students = _check_if_numeric(number_of_students)

    @property
    def class_master(self) -> namedtuple:
        return self._class_master

    @class_master.setter
    def class_master(self, class_master) -> None:
        self._class_master = _for_name_checking(class_master)

    @property
    def grades(self) -> dict:
        return self._grades

    @property
    def students(self) -> dict:
        return self._students

    @property
    def courses(self) -> dict:
        return self._courses

    def _check_exists(self, _student, class_to_use) -> None:
        if _student.name not in self._grades:
            self._grades.update({_student.name: {class_to_use.name_of_course: {}}})
        else:
            self._grades[_student.name].update({class_to_use.name_of_course: {}})

    def register_student(self, name: str, age: Union[int, float],
                         address: str, employed: bool, classes: Union[str, list], teacher_name: Union[str, list]) -> Union[str, dict]:

        id_for_student = generate_student_id(name=name, students=self._students)

        _student = Student(name=name, age=age, address=address, id=id_for_student, employed=employed)
        self._students.update({_student.id: (_student.name, _student)})

        if (type(classes) and type(teacher_name)) == str:
            class_to_use = Course(name_of_course=classes.capitalize(), min_grade=1, max_grade=10, teacher_name=teacher_name)
            self._courses.update({class_to_use.name_of_course: class_to_use})
            self._check_exists(_student, class_to_use)
        elif (type(classes) and type(teacher_name)) == list:
            for i, j in zip(classes, teacher_name):
                class_to_use = Course(name_of_course=i.capitalize(), min_grade=1, max_grade=10, teacher_name=j)

                if class_to_use.name_of_course not in self.courses:
                    self._courses.update({class_to_use.name_of_course: class_to_use})

                self._check_exists(_student, class_to_use)
        else:
            print(f"\n{' ' * 3} \033[31mPOL1001 - When register a student we need at least a class and a teacher name or a \
                    list of classes and teacher for each class!\033[0m\n")
            sleep(2)
            return 'POL1001'

        return self.students

    def add_course_for_student(self, name_of_student: str, name_of_course: Union[str , list], teacher_name: Union[str, list]) -> Union[str, dict]:
        name: str = _for_name_checking(name_of_student)

        if name not in self._grades:
            print(f"\n{' ' * 3} \033[31mERR1001 - Student {name} doesn\'t exists in the gradebook. "
                  f"As a first step you need to register the student!\033[0m\n")
            sleep(2)
            return 'ERR1001'
        elif (type(name_of_course) and type(teacher_name)) == str:
            teacher_name = [teacher_name]
            name_of_course = [name_of_course]

        if (type(name_of_course) and type(teacher_name)) == list:
            courses_already_exists: list = []
            for i, j in zip(name_of_course, teacher_name):
                if i.capitalize() in self.grades[name]:
                    courses_already_exists.append(i.capitalize())
                else:
                    given_course = Course(name_of_course=i.capitalize(), min_grade=1, max_grade=10, teacher_name=j)
                    self._grades[name].update({given_course.name_of_course: {}})
                    self._courses.update({given_course.name_of_course: given_course})

            if courses_already_exists:
                print(f"\n{' ' * 3} \033[31mPOL1002 - The following courses {', '.join(courses_already_exists)} "
                      f"already exists for student {name}!\033[0m\n")
                sleep(2)
                return 'POL1002'
        else:
            print(f"""\n{' ' * 3} \033[31mPOL1001 - When adding a course for a student we need 
            at least a class and a teacher name or a list of classes and teacher for each class!\033[0m\n""")
            sleep(2)
            return 'POL1001'

        return self.courses

    def add_grade(self, name_of_student: str, *args) -> Union[dict, str]:
        name_for_student: str = _for_name_checking(name_of_student)

        if len(args) >= 2:
            course, grades_to_add, grade_with_exceptions_type = _working_on_grades_from_add(*args)
        else:
            print(f"\n{' ' * 3} \033[31mPOL1003 - In order to add a grade we need the name of the"
                  f" course and grade after it when method is called!\033[0m\n")
            sleep(2)
            return 'POL1003'

        if name_for_student not in self.grades:
            print(f"{' ' * 3} \033[31mERR1002 - Name of student - {name_for_student} - doesn\'t exists in grades!\033[0m\n")
            sleep(2)
            return 'ERR1002'
        elif course not in self.grades[name_for_student]:
            print(f"{' ' * 3} \033[31mERR1003 - Course {course} does not exists in grades for {name_for_student}!\033[0m")
            sleep(2)
            return 'ERR1003'

        for i, j in enumerate(grades_to_add):
            if str(date.today()) not in self.grades[name_for_student][course]:
                self._grades[name_for_student][course].update({str(date.today()): [j]})
            else:
                self._grades[name_for_student][course][str(date.today())].append(j)

        return self.grades[name_for_student][course]

    def get_grades(self, name_of_the_student: str, course=None, get_with_date=False) -> Union[list, None]:
        name_of_the_student: str = _for_name_checking(name_of_the_student)

        if not course:
            try:
                if get_with_date:
                    grades_to_print = self.grades[name_of_the_student]
                else:
                    grades_to_print = []
                    for i in self.grades[name_of_the_student].values():
                        if i:
                            grades_to_print.extend(*i.values())
            except KeyError:
                grades_to_print = None
        else:
            course: str = _check_if_str(course)
            try:
                if get_with_date:
                    grades_to_print = self.grades[name_of_the_student][course]
                else:
                    grades_to_print = []
                    for i in self.grades[name_of_the_student][course].values():
                        if i:
                            grades_to_print.extend(i)
            except KeyError:
                grades_to_print = None

        return grades_to_print

    def calc_average_per_student(self, name_of_the_student: str, course=None) -> Union[float, str]:
        result: list = []
        name: str = _for_name_checking(name_of_the_student)

        if name not in self.grades:
            print(f"\n{' ' * 3} \033[31mERR1001 - Student {name} doesn\'t exists in the gradebook. "
                  f"As a first step you need to register the student!\033[0m\n")
            sleep(2)
            return 'ERR1001'
        elif course and course not in self.grades[name_of_the_student]:
            print(f"\n{' ' * 3} \033[31mERR1003 - Course {course} does not exist in the "
                  f"grade book for student {name}!\033[0m\n")
            sleep(2)
            return 'ERR1003'
        else:
            if course:
                course: str = _check_if_str(course)
                result = self.get_grades(name, course)
            else:
                for i, j in self.grades[name].items():
                    if j:
                        result.append(self.calc_average_per_student(name, i))

        return sum(result)/len(result)

    def calc_average_class(self, course=None, average_entire_course=False) -> Union[dict, float]:
        averages_per_course: dict = {}

        for i, j in self.grades.items():
            averages_per_course.update({i: self.calc_average_per_student(i, course)})

        if not average_entire_course:
            return averages_per_course
        else:
            return sum(averages_per_course.values())/len(averages_per_course.values())

    def edit_grade(self, student_name: str, course: str, old_grade: Union[int, float, str],
                   new_grade: Union[int, float, str], date_for_grade: str) -> Union[list, str]:
        name: str = _for_name_checking(student_name)
        course: str = _check_if_str(course)

        if name and name not in self.grades:
            print(f"\n{' ' * 3} \033[31mERR1001 - Student {name} doesn\'t exists in the gradebook. "
                  f"As a first step you need to register the student!\033[0m\n")
            sleep(2)
            return 'ERR1001'
        elif course and course not in self.grades[name]:
            print(f"\n{' ' * 3} \033[31mERR1003 - Course {course} does not exist in the "
                  f"grade book for student {name}!\033[0m\n")
            sleep(2)
            return 'ERR1003'
        else:
            if old_grade and date_for_grade:
                try:
                    locate_input: list = self.grades[name][course][date_for_grade]
                    result = list(map(lambda i: float(str(i).replace(str(old_grade), str(new_grade))), locate_input))
                    self.grades[name][course][date_for_grade] = result
                except KeyError:
                    print(f"\n{' ' * 3} \033[31mERR1004 - Date for grade does not exists!\033[0m\n")
                    sleep(2)
                    result = 'ERR1004'
            else:
                print(f"\n{' ' * 3} \033[31mPOL1004 - old grade and date for grade parameters are not given!\033[0m\n")
                sleep(2)
                result = 'POL1004'

        return result

    def __repr__(self) -> str:
        return f'class_name: {self.students_class_name}, ' \
               f'number_of_students: {self.number_of_students}, ' \
               f'class_master: {self.class_master}'

    def __str__(self) -> str:
        return f'{self.__repr__()}'
