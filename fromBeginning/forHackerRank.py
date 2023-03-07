#!/usr/bin/python


import datetime
from itertools import product


def find_the_runner_up(qty_numbers, elements):
    records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    second_largest_grade = sorted(set(i[1] for i in records))[1]
    print(*sorted([i[0] for i in records if i[1] == second_largest_grade]), sep='\n')


def finding_the_percentage():
    given_grades: dict = {'alpha': [20, 30, 40], 'beta': [30, 50, 70]}
    query_name = 'alpha'

    extracted_from_dict = given_grades.get(query_name, 0)
    print(f"{sum(extracted_from_dict) / len(extracted_from_dict):.2f}")


def average_distincts(array):
    unq = set(array)
    return round(sum(unq) / len(unq), 3)


def working_with_sets():
    M = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    b = set(map(int, input().split()))

    print(*sorted(a.symmetric_difference(b)), sep='\n')


def disjoint_sets():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    initial_happiness: int = 0

    for i in arr:
        if i in A:
            initial_happiness += 1
        elif i in B:
            initial_happiness -= 1

    print(initial_happiness)


def set_add_stamps():
    i: int = 0
    number_of_stamps = int(input())
    countries: set = set()

    while i < number_of_stamps:
        countries.add(str(input()))
        i += 1

    print(len(countries))


def list_methods():
    class List(list):
        def print(self):
            print(self)

    if __name__ == '__main__':
        working_list = List()

        for _ in range(int(input())):
            i = input().split()
            getattr(working_list, i[0])(*map(int, i[1:]))


def to_chck(input_value: str, *args):
    az = datetime.date.today()
    print(az)


def cartesian_product():
    print(*product(*[list(map(int, input().split())) for i in range(2)]), sep=' ')


def intro():
    ax = {0: {}}

    if not ax[0]:
        print('AAAA')


def working_on_strings_cases(given_string):
    return ''.join(i.upper() if i.islower() else i.lower() for i in given_string)


def main():
    #find_the_runner_up(5, [2, 3, 6, 6, 5])
    #finding_the_percentage()
    #average_distincts([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])
    #working_with_sets()
    #disjoint_sets()
    #list_methods()
    #to_chck('vali', 4, 10, 2)
    #cartesian_product()
    #intro()
    ax = working_on_strings_cases('NebuNieMare Boss')
    print(ax)

if __name__ == '__main__':
    main()
