#!/usr/bin/python

import math
import random
import statistics
import datetime
from decimal import Decimal as Dec


#def square(given_number):
#    return given_number ** 2


#def calc_square_root(given_number):
#    return f"{str(decimal.Decimal(given_number ** 0.5))}"


#def determine_maximum_of_three(first_value, second_value, third_value):
#    max_value = first_value

#    if second_value > max_value:
#        max_value = second_value

#    if third_value > max_value:
#        max_value = third_value

#    return max_value

#def compare_colors():
#    given_list_with_colors = ['orange', 'yellow', 'red', 'blue', 'green']
#    maximum_color = given_list_with_colors[0]

#    for i in range(1, len(given_list_with_colors) -1):
#        if given_list_with_colors[i] > maximum_color:
#            maximum_color = given_list_with_colors[i]

#    return maximum_color

#def generate_numbers():
#    count = 9
#    for i in range(10):
#        if count == 0:
#            print(random.randrange(1, 11, 1))
#        else:
#            print(random.randrange(1, 11, 1), end=", ")

#        count -= 1

#def play_with_tuples():
#    student = ('Sue', [89, 94, 85])
#    print(student)

#    name, grades = student
#    print(f"\nName: {name}\nGrades: {' '.join([str(i) for i in grades])}")

#def calc_average_grades(*args):
#    print(f"Average: {sum(args) / len(args)}")

#def calculate_product(*args):
#    print(f"Product of {args}: {math.prod(args)}")

#def square_decimal(given_value=1):
#    return Dec(math.pow(given_value, 2))

#def objecting():
#    width = 15.5
#    print(f"Before: {id(width)}")

#    width += 1
#    print(f"After modification: {id(width)}")

#def calculate_stats(given_list):
#    calc_pop_mean = statistics.mean(given_list)
#    variance = statistics.mean([((i - calc_pop_mean) ** 2) for i in given_list])

#    print(f"Variance: {variance}")
#    print(f"Standard Deviation: {math.sqrt(variance)}")
#    statistics.

#def dateAndTime():
#    day_of_today = datetime.datetime.now()
#    day_of_epoch = datetime.date.today().strftime('%s')

#    print(f"Date of today in human format: {day_of_today}")
#    print(f"Date in epoch: {day_of_epoch}")

#def rounding_numbers(given_number):
#    print(f"{round(given_number)}, {round(given_number, 2)}, {round(given_number, 3)}, {round(given_number, 4)}")

def temperature_conversion():
    message_header = f"{' ' * 12}{'Celsius'}{' ' * 10}{'Fahrenheit'}"
    length_of_message = len(message_header)

    print(f"\n{message_header}\n{' ' * 12}{'-' * (length_of_message - 12)}")

    for given_value_celsius in range(0, 101):
        value_in_fahrenheit = (9 / 5) * given_value_celsius + 32
        print(f"{given_value_celsius:>19}{value_in_fahrenheit:20.1f}")


def main():
    #number_returned = square(2)
    #print(number_returned)

    #print(calc_square_root(144))

    #print(determine_maximum_of_three(40, 20, 31))

    #print(compare_colors())

    #generate_numbers()
    #play_with_tuples()

    #grades = [4, 10, 7]
    #calc_average_grades(*grades)

    #numbers = [10, 20, 30]
    #calculate_product(*numbers)

    #calculate_product(*range(1, 6, 2))

    #print(square_decimal(4))

    #objecting()

    #list_with_stats = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]
    #calculate_stats(list_with_stats)

    #dateAndTime()

    #rounding_numbers(13.56449)

    temperature_conversion()

if __name__ == '__main__':
    main()
