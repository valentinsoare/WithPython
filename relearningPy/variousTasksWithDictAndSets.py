#!/usr/bin/python

import os
import numpy as np


def dict_manipulation():
    tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
    tlds.update({'France': 'fr'})

    tlds['Germany'] = 'de'
    print(tlds)

    for i, j in tlds.items():
        print(f"{i:>15} {j:>5}")

    reversed_keys_values = dict(map(lambda k: (k[1], k[0]), filter(lambda j: j, tlds.items())))
    reversed_keys_values = {j: i for i, j in tlds.items()}
    to_uppercase_letters_country_names = {l: k.upper() for k, l in tlds.items()}

    print(to_uppercase_letters_country_names)


def set_manipulation():
    s_1 = {'yellow', 'green', 'blue'}
    s_2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

    if s_1 > s_2:
        print(f"True")
    else:
        print(f"False")

    ax = s_1.intersection(s_2)
    ay = s_1.union(s_2)
    az = s_1.difference(s_2)
    aw = s_1.symmetric_difference(s_2)

    print(aw)


def main():
    #dict_manipulation()
    set_manipulation()


if __name__ == '__main__':
    main()
