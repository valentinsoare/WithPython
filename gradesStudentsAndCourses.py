#!/usr/bin/python3

given_list = [['87', '90', '78', '94'], ['78', '98', '92', '67']]
students = ['Chris', 'Eva']
names_classes = ['Math', 'Chemistry', 'Physics', 'English']

def printing(given_list, name_classes):

    """Printing catalog pandas style but without pandas"""

    maxi_names = max(len(str(students[i])) for i in range(len(students)))

    print(f'|\033[1;4m{"Student":>{maxi_names * 2}}\033[0m|', end='')

    for k in range(len(names_classes)):
        print(f"\033[1;4m{names_classes[k].rjust(maxi_names * 2)}\033[0m|", end='')

    print()

    for i in range(len(given_list)):
        print(f'|\033[1;4m{students[i].rjust(maxi_names * 2)}\033[0m|', end='')
        for j in range(len(given_list[i])):
            print(f'\033[1;4m{given_list[i][j].rjust(maxi_names * 2)}\033[0m|', end='')
        print()


printing(given_list, names_classes)