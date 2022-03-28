#!/usr/bin/python

import re
import math
from itertools import combinations,\
    permutations


def remainder_one():
    print(f' -Integers:', end=" ")
    for i in range(100, 999):
        to_count = 0
        for j in range(2, 8):
            if i % j == 1:
                to_count += 1
                if to_count == 6:
                    print(f'{i}', end=" ")


def finding_integer():
    final = ''
    to_begin = int(math.sqrt(27182))

    while not re.search(r'^27182', final):
        to_begin += 1
        final = str(to_begin ** 2)

    print(f'\n -Found number: {to_begin} - Reached pattern: {final}')


def integer_linear_combinations(coin_value_x, coin_value_y, value_to_give):
    var = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if (coin_value_x * x - coin_value_y * y or coin_value_x * x + coin_value_y * y) == value_to_give:
                print(f' -X = {x} and Y = {y}')
                var = 1

        if var == 1:
            break


def get_cmc(a, b):
    cmc = 0
    to_continue = 0

    if a > b:
        z = a
    else:
        z = b

    while to_continue == 0:
        if z % a == 0 and z % b == 0:
            cmc = z
            to_continue = 1
        z += 1

    print(f' -Least Common Multiple for {a} and {b} is {cmc}')


def n_queens_brute_force(number_n):

    def check_for_solution(perm):
        for i in combinations(range(len(perm)), 2):
            i1, i2 = i
            if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
                return False

        return True

    def brute_for_search(number_n_var):
        for perm in permutations(list(range(number_n_var))):
            if check_for_solution(perm):
                perm = list(perm)
                return perm

    first_good_moves = brute_for_search(number_n)

    print(f' -First available moves for {number_n} queens on {number_n} x {number_n} chessboard: ')

    for i in enumerate(first_good_moves):
        column, row = i
        print(f'\t row: {row}, column {column}')


def generate_permutations(perm, n):
    if len(perm) == n:
        print(perm)
        return

    for k in range(n):
        if k not in perm:
            perm.append(k)
            generate_permutations(perm, n)
            perm.pop()


def to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False

    return True


def generating(perm, n):
    if len(perm) == n:
        print(perm)
        exit(0)

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if to_solution(perm):
                generating(perm, n)

            perm.pop()


def merging_lists(list_one, list_two):
    to_add = 0
    final_list = []
    i = 0

    while (len(list_one) and len(list_two)) != 0:
        if list_one[i] < list_two[i]:
            to_add = list_one.pop(i)
        elif list_two[i] < list_one[i]:
            to_add = list_two.pop(i)

        final_list.append(to_add)

    print(final_list)


def fibonacci(given_number):
    if given_number <= 2:
        return 1

    return fibonacci(given_number - 1) + fibonacci(given_number - 2)


def palindrome_recursive(given_word):
    if len(given_word) == 1:
        return True

    if given_word[0] != given_word[-1]:
        return False

    given_word = given_word[1:(len(given_word) - 1)]
    return palindrome_recursive(given_word)


def coins_problem(coins_qty):
    if coins_qty < 8:
        print(f'Quantity of coins should be greater or equal to 8.')

    if coins_qty == 8:
        return [3, 5]
    elif coins_qty == 9:
        return [3, 3, 3]
    elif coins_qty == 10:
        return [5, 5]

    coins = coins_problem(coins_qty - 3)
    coins.append(3)

    return coins


def coins_another_value(amount):
    def to_get(given_value):
        dict_to_get = {24: [5, 5, 7, 7], 25: [5, 5, 5, 5, 5],
                       26: [7, 7, 7, 5], 27: [5, 5, 5, 5, 7], 28: [7, 7, 7, 7]}

        return dict_to_get.get(given_value)

    if amount <= 23:
        print(f'Quantity of coins should be greater or equal to 23.')
        return 1
    elif 24 <= amount <= 28:
        return to_get(amount)

    coins_to_return = coins_another_value(amount - 5)
    coins_to_return.append(5)

    return coins_to_return


def main():
    #remainder_one()
    #finding_integer()
    #integer_linear_combinations(14, 5, 6)
    #get_cmc(4, 18)
    #n_queens_brute_force(13)
    #generate_permutations(perm=[], n=4)
    #generating(perm=[], n=8)
    #----------------------------
    #first = [1, 3, 5, 7, 9]
    #second = [2, 4, 6, 8, 10]
    #merging_lists(first, second)
    #-----------------------------
    #value = 6
    #number = fibonacci(value)
    #print(f'{value} fibonacci number is {number}')
    ##----------------------------
    #given_word = 'racecar'
    #value = palindrome_recursive(given_word)
    #if value:
    #    print(f'"{given_word}" is a palindrome')
    #----------------------------
    #number_of_coins = 23
    #value = coins_problem(number_of_coins)
    #print(f' -> {number_of_coins}$ change in banknotes with values of 3 and 5 dollars: {value} <-')
    #----------------------------
    x = coins_another_value(55)
    if x != 1:
        print(x)
    #----------------------------
    #y = fibonacci(6)
    #print(y)
    #----------------------------


if __name__ == '__main__':
    main()
