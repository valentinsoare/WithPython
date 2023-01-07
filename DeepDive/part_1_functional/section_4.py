#!/usr/bin/python


# a = b * (a // b) + (a % b) - formula


def integers_and_ordereddict():
    my_list = ['lux', 'opulenta', 'nebunie', 'home']
    names = ['andrei', 'vali', 'gabriela', 'adriana']

    my_dict = dict(zip(names, my_list))
    print(my_dict)


def main():
    integers_and_ordereddict()


if __name__ == '__main__':
    main()
