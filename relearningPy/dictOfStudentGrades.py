#!/usr/bin/python


import statistics


def header(message):
    chars_to_replace = {'u': '|_|', 's': '5', 'a': '@', 'o': '0', 'e': '3'}
    processed_message = ' *** '
    list_with_keys_for_message = chars_to_replace.keys()

    for i in message:
        if i in list_with_keys_for_message:
            processed_message += ' ' + chars_to_replace[i]
        else:
            processed_message += ' ' + i

    processed_message += ' *** '
    length_of_message = len(processed_message)

    print(f"\n{' ' * int(length_of_message * 0.25)}{'-' * int(length_of_message * 1.5)}")
    print(f"{' ' * int(length_of_message * 0.5)}{processed_message}")
    print(f"{' ' * int(length_of_message * 0.25)}{'-' * int(length_of_message * 1.5) }")


def collect_data_to_be_process(what_to_return=0):
    grade_book = {'Susan': [92, 85, 100], 'Eduardo': [83, 95, 79, 65],
                  'Azizi': [91, 89, 82], 'Pantipa': [100, 97, 78],
                  'Valentin': [98, 100, 89], 'Diana': [100, 98, 89, 98, 69, 97]}

    if what_to_return == 0:
        list_of_tuples_from_dict = grade_book.items()
        return list_of_tuples_from_dict
    else:
        return grade_book


def print_grade_book(collection_with_grades):
    all_grades_total = 0
    all_grades_count = 0
    max_number_of_grades = max(map(lambda j: len(j), collection_with_grades.values()))

    print(f"\n{' ' * 16}{'Name of student':<28}{'Grades':<{max_number_of_grades * 4}}{'Average per student'}")
    for name, grades in collection_with_grades.items():
        print(f"{' ' * 16}{name:>15}{' ' * 12}", end=" ")
        for i in range(len(grades)):
            if i != (len(grades) - 1):
                print(f"{grades[i]},", end=" ")
            else:
                print(f"{grades[i]:<{(max_number_of_grades * 4) - (len(grades) * 4) + 3}}", end=" ")
        print(f"{statistics.mean(grades):.2f}")

        all_grades_count += len(grades)
        all_grades_total += sum(grades)

    print(f"\n{' ' * 16} * Entire class average is {all_grades_total/all_grades_count:.2f}")


def main():
    header('Student Grades Averages')

    dict_of_grades = collect_data_to_be_process(1)
    print_grade_book(dict_of_grades)


if __name__ == "__main__":
    main()
