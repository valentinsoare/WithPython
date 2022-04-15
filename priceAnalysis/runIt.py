#!/usr/bin/python

import operator
import dynArray
import fixedArray
import makePurchases
import registeredStores


def main():
    count_pass = 0
    count_not_pass = 0

    classes = ['Math', 'English', 'Physics', 'History', 'Chemistry', 'Sports']
    grades_dyn = dynArray.DynamicArray([9, 3, 7, 4, 6, 8])
    grades_dyn.dyn_sort(reverse=True)
    to_sort_dict = grades_dyn.dyn_to_dict(classes)

    print(f'\n{"Valentin":>15}\n {"Soare":>11} grades:\n{"-" * 20:>24}')
    for classes, grade in to_sort_dict.items():
        if grade < 5:
            print(f'{"|":>5} \033[31m{classes:<10}\033[0m | \033[31m{grade:<3}\033[0m | \033[1;31mFAILED!!\033[0m')
            count_not_pass += 1
        else:
            print(f'{"|":>5} {classes:<10} | {grade:<3} |')
            count_pass += 1
        print(f'{"-" * 20:>24}')

    print(f'{"|":>5} \033[1m{"Average":<10}\033[0m | \033[1m{sum(to_sort_dict.values())/len(to_sort_dict.values()):<2.1f}\033[0m |')
    print(f'{"-" * 20:>24}')
    print(f'\033[1m{"failed":>11}: {count_not_pass}\033[0m', end=", ")
    print(f'\033[1m{"pass"}: {count_pass}\033[0m', end="\n\n")


if __name__ == '__main__':
    main()
