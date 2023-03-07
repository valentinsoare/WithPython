#!/usr/bin/python

from time import sleep
from typing import Union
from components.gradebook import GradeBook
from components.progressbar import ProgressBar
from components.variousCheckings import _print_banner, _ask_how_many_students, _ask_for_students_details, \
     _check_if_str, _for_name_checking, _check_if_integer, _intro_to_app


class Controller:
    def __init__(self, students_class_name, number_of_students, class_master) -> None:
        self.students_class_name: str = _check_if_str(students_class_name)
        self.number_of_students: int = _check_if_integer(number_of_students, return_tuple=False)
        self.class_master: str = _for_name_checking(class_master)

        self.new_grade_book = GradeBook(students_class_name=self.students_class_name,
                                        number_of_students=self.number_of_students,
                                        class_master=self.class_master)

    def implement_option_1(self) -> Union[None, int]:
        """Register student"""
        students_to_be_added: Union[dict, int] = -1

        while students_to_be_added == -1:
            number_of_students_to_add: Union[str, int] = _ask_how_many_students(name_of_class=self.students_class_name)
            if number_of_students_to_add == -1:
                return 0
            else:
                students_to_be_added: Union[dict, int] = _ask_for_students_details(number_of_students_to_add,
                                                                                   name_of_class=self.students_class_name)


    @staticmethod
    def implement_option_2():
        """Add course"""
        print('Doing 2')

    @staticmethod
    def implement_option_3():
        """Add grade"""
        print('Doing 3')

    @staticmethod
    def implement_option_4():
        """Edit grade"""
        print('Doing 4')

    @staticmethod
    def implement_option_5():
        """Calculate average per student"""
        print('Doing 5')

    @staticmethod
    def implement_option_6():
        """Calculate average per class"""
        print(f'Doing 6')

    @staticmethod
    def implement_option_7():
        """Display grades"""
        print('Doing 7')

    @staticmethod
    def implement_option_8():
        """Get courses"""
        print(f'Doing 8')

    @staticmethod
    def implement_option_9():
        """Exit"""
        print(f"\n{' ' * 8} \033[1;32mExiting....\033[0m\n", flush=True)
        sleep(2)
                                                              
    def execute_selection(self, user_input: int) -> None:
        controller_name = f"implement_option_{user_input}"

        try:
            controller = getattr(self, controller_name)
        except AttributeError:
            print(f"\n{' ' * 3} ERR1005 - Given option {user_input} does not exists in the menu!\n", flush=True)
            sleep(2)
        else:
            controller()

    def run_menu(self) -> None:
        user_input: int = 0

        while user_input != 9:
            self.generate_menu()
            user_input = int(input())
            self.execute_selection(user_input)

    def generate_menu(self) -> None:
        do_methods: list = [i for i in dir(self) if i.startswith('implement_option_')]
        menu_string: str = "\n".join([f"{' ' * 10}{indx + 1}. {getattr(self, method).__doc__}" for indx, method in enumerate(do_methods)])
        line_sep = _print_banner(grade_book_class=self.students_class_name)

        print(f"{menu_string}", flush=True)
        print(f"{' ' * 8}\033[1;32m{'-' * line_sep}\033[0m", flush=True)
        print(f"{' ' * 10}\033[1m * Select:\033[0m", end=" ", flush=True)

    def __repr__(self) -> str:
        return f"class_name: {self.students_class_name}," \
               f"number_of_students: {self.number_of_students}," \
               f"class_master: {self.class_master},"

    def __str__(self) -> str:
        return f'{self.__repr__()}'


def _load_progress_bar(given_message: str, vars_to_load: dict) -> Controller:
    print('\033[?25l')
    progress = ProgressBar(description=given_message, end='DONE!', timeout=0.1)
    progress.start()

    grade_book = Controller(*vars_to_load.values())
    for _ in range(20):
        sleep(0.25)

    progress.stop()

    print('\033[?25h', end="")
    return grade_book


def main():
    vars_to_load_initial_grade_book: dict = _intro_to_app()
    grade_book = _load_progress_bar(given_message=f"* Creating {list(vars_to_load_initial_grade_book.values())[0]} grade book",
                                    vars_to_load=vars_to_load_initial_grade_book)
    grade_book.run_menu()


if __name__ == '__main__':
    main()
