#!/usr/bin/python

import os
import sys
import random
import base64
import statistics
import math


def execute_training():
    #x = 10
    #y = 12.2
    #total = x + y
    #print(f"{total:>10}")
    #print(type(total))

    #total = 10.8 + 12.2 + 0.2
    #print(f'{total}')

    #print(5 ** 3)
    #print(4 / 2)
    #print(4 // 2)
    #print(4 % 3)

    #print(f'{9 ** (1 / 3):.3f}')         # radical din 9
    #print(f'{-12 // 5}')
    #print(f'{6 * 3 / (2+1)}')

    #---------------------------------------

    #print('Welcome to Python ', ' King of the Urban Coding Jungle', sep='-', end='!\n')

    #to_print = "Welcome into the Jungle!"
    #print(f'{to_print}')

    #print('Welcome', 'to', 'Python!', sep=' / ')
    #print("Bun\nVenit\nIn\nPython")

    #print("sa fie bine sa nu fie rau "
    #      "ce facem ma boss aici sa mor eu daca pricep")

    #print('Sum is', 10 + 2)

    #-----------------------------------------

    #x = int(5.2)
    #y = float(5)

    #print(y)
    #print(x)

    #-----------------------------------------

    #print('''Nebunie boss sa mor eu ce facem aici
#sa mor eu daca stiu ce vrie de la mine''')

#    print('Bine boss "salut"')

#    variable_to_print = """BOSS de BOSS care
#eeeesti tu BOSS"""
#    print(f'{variable_to_print}')

    #------------------------------------------

    #counter = 1
    #name_message = "Please tell me your name:"

    #print(f'\n\033[1m{counter}. {name_message}\033[0m', end=" ")
    #name = input()

    #counter += 1
    #age_message = "How old are you:"

    #print(f'\033[1;31m{counter}. {age_message}\033[0m', end=" ")
    #age = int(input())

    #print(f'\n ---> Your name is {name} and you are {age} years old.')

    #----------------------------------
    #counter = 0
    #print(f'{counter}. number:', end=" ")
    #first_number = int(float(input()))
    #counter += 1

    #print(f'{counter}. number:', end=" ")
    #second_number = int(float(input()))

    #print(f'{first_number} + {second_number} = {first_number + second_number}')

    #if first_number == second_number:
    #    print(f'{first_number} is equal to {second_number}')
    #elif first_number != second_number:
    #    print(f'{first_number} is not equal to {second_number}')

    #if first_number <= second_number:
    #    print(f'{first_number} is less than or equal to {second_number}')
    #elif first_number >= second_number:
    #    print(f'{first_number} is greater than or equal to {second_number}')

    #if 2 < first_number <= 10:
    #    print(f'{first_number} is between 2 and 10.')

    #---------------------------------------------
    #x = 10
    #print(id(x))

    ##x += 1
    #print(id(x))
    #print(type(x))

    #x = 10.2
    #print(id(x))
    #print(type(x))

    #x = 'lux'
    #print(sys.getsizeof(x))

    #print(type(7.5 * 3))

    #-------------------------------------------

    #print(f'First number:', end=" ")
    #first_number = int(input())

    #print(f'Second number:', end=" ")
    #second_number = int(input())

    #print(f'Third number:', end=" ")
    #third_number = int(input())

    #minimum_number = first_number

    #if second_number < minimum_number:
    #    minimum_number = second_number

    #if third_number < minimum_number:
    #    minimum_number = third_number

    #print(f'Min number is {minimum_number}')

    #print(min(10, 22, 44, 12, 9, 23))
    #print(max(10, 2, 3, 4, 10, 44, 23, 100))

#========================================================================================
    # Chapter 2 tasks - >  homework

    # Task 2.5

    #r = 2
    #pi = 3.14159

    #diameter = 2 * r
    #circumference = 2 * pi * r
    #area = pi * r ** 2

    #print(f' - > Diameter of a circle with radius 2: {diameter}')
    #print(f' - > Circumference of previous mentioned circle: {circumference:.2f}')
    #print(f' - > Area of that circle: {area:.2f}')

#----------------------------------------------------------

    # Task 2.6

    #print(f' - > Give you a number to check if it is even or odd >:', end=" ")
    #given_number = input()

    #try:
    #    given_number = int(given_number)
    #except ValueError:
    #    try:
    #        given_number = float(given_number)
    #    except ValueError:
    #        print(f'ERROR we need an integer or float')
    #        exit(1)

    #if given_number % 2 == 0:
    #    print(f'Given number {given_number} is even.')
    #else:
    #    print(f'Given number {given_number} is odd.')

#------------------------------------------------------------
    # Task 2.7

    #if 1024 % 4 == 0:
    #    print(f'1024 is a multiple of 4')

    #if 2 % 10 == 0:
    #    print(f'2 is a multiple of 10 :))

#------------------------------------------------------------
    # Task 2.8

    #print(f'\n===LEFT ALIGN====')
    #print(f"number\tsquare\tcube")

    #for i in range(0, 6):
    #    print(f'{i}\t\t{i ** 2}\t\t{i ** 3}')

    #print(f'\n===RIGHT ALIGN===')
    #print(f"number\tsquare\tcube")

    #for j in range(0, 6):
    #    print(f'{j:>6}{j ** 2:>8}{j ** 3:>6}')

#------------------------------------------------------------
    #print(ord('1'))

    # Task 2.10

    #count = 1
    #list_with_numbers = []

    #while len(list_with_numbers) < 3:
    #    print(f"{count}. Number:", end=" ")
    #    number = input()
    #    try:
    #        number = int(number)
    #    except ValueError:
    #        try:
    #            number = float(number)
    #        except ValueError:
    #            os.system('clear')
    #            continue
    #    count += 1
    #    list_with_numbers.append(number)

    #print(f"\n Smallest number: {min(list_with_numbers)}\n Largest number: {max(list_with_numbers)}\n"
    #      f" Sum of all numbers: {sum(list_with_numbers)}\n Average: {statistics.mean(list_with_numbers):.2f}\n"
    #      f" Product: {math.prod(list_with_numbers):.2f}")

    # -------------------------------------------------------------------

    # Task 2.11

    print(f'=====Break a number=====')

    phone_number = ""
    list_with_digits = []

    while not isinstance(phone_number, int):
        print(f'Give me your phone number:', end=" ")
        phone_number = input()
        try:
            phone_number = int(phone_number)
        except ValueError:
            os.system('clear')
            continue

    while True:
        after_modulo = phone_number % 10
        phone_number = phone_number // 10
        list_with_digits.append(after_modulo)
        if phone_number == 0:
            break

    for i in list(reversed(list_with_digits)):
        print(f'{i:<3}', end=" ")


def main():
    execute_training()


if __name__ == "__main__":
    main()
