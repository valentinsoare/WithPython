#!/usr/bin/python

import random
import functools
import string


def to_execute():
    given_list = [4, 10, 22, 13, 42, 19, 54]

    print(given_list[2])
    print(given_list[-1])

    print(given_list)

    print(given_list[0] + given_list[2])

    given_list.append(44)

    given_list += [101]
    print(given_list)

    given_list.insert(0, 33)
    print(given_list)

    #given_list += ['Nebunie']
    print(given_list)

    adunare = 0
    for i in range(len(given_list)):
        adunare += given_list[i]

    #print(f"Suma este {adunare}")

    #a = [4, 10, 2]
    #b = [4, 10, 2]
    #c = [4, 10, 2, 1]

    #if a == b:
    #    print(f"AAAAA")

    #if b != c:
    #    print(f"BBBB")



def cube_list(numbers):
    return [i ** 3for i in numbers]


def convert_string(given_string):
    characters = []
    characters += given_string

    return characters


def tuples():
    given_tuple = 'Valentin', 'Andrew'
    another_tuple = 9, 10

    combined = zip(given_tuple, another_tuple)
    after_processing = list(combined)
    #print(after_processing)

    after_processing += [('Emilian', 7)]
    after_processing += [('John', 'Soare', [9, 7, 10])]

    after_processing[3][2][1] = 4

    nr_1 = 44
    nr_2 = 23

    nr_2, nr_1 = nr_1, nr_2

    print(nr_1)

    print(f"{after_processing}")

    for index, element in enumerate(after_processing):
        print(f"{index}. {element}")


def tuples_temp():
    high_low = ('Saturday', [4, 29])
    print(f"\nDay of the week: {high_low[0]}\nLow temperature: {high_low[1][0]:>2}\nHigh temperature: {high_low[1][1]:>2}")


def three_strings():
    list_with_names = ['Valentin', 'Andreea', 'John']

    print()
    for index, name in enumerate(list_with_names):
        print(f"{index + 1}. {name}")


def slicing_lists():
    given_numbers = [4, 10, 22, 78, 19, 45, 6, 29, 32]
    #print(given_numbers[1:5])

    #print(given_numbers[:5])
    #print(given_numbers[6:])
    #xx = given_numbers[:]
    #xx[0] = 100
    #print(xx)
    #print(given_numbers)

    #print(given_numbers[::2])

    #print(given_numbers[::-1])
    #print(reversed(given_numbers))
    #print(given_numbers[-1:-10:-1])

    #given_numbers[0:3] = ['one', 'two'' three', 'four']
    #print(given_numbers)

    #given_numbers[0:3] = []
    #print(given_numbers)

    #print(id(given_numbers))

    #given_numbers[::2] = [100, 100, 100, 100, 100]

    #given_numbers[:] = [102, 33, 44, 42]
    #print(id(given_numbers))

    #numbers = [i for i in range(1, 16)]
    #print(f"{numbers[1:len(numbers):2]}") # even integers

    #numbers[5:10] = [int(i) for i in ('0' * 4)]     # cool thing
    #numbers[5:10] = [0] * 4
    #print(numbers)

    #short_list = numbers[0:5]     # save first five elements fromo index 0
    #print(short_list)

    #numbers[5::] = []             # delete last elements from index 5
    #print(numbers)

    #our_numbers = list(range(21))
    #print(our_numbers)

    #del our_numbers[0]
    #print(our_numbers)

    #del our_numbers[::2]
    #print(our_numbers)

    #del our_numbers[:]
    #print(our_numbers)

    #print(our_numbers)

    #del our_numbers[0:4]
    #print(our_numbers)

    #our_numbers[:len(our_numbers)] = ''
    #print(our_numbers)


def actions_on_lists():
    #numbers = [4, 10, 22, 23, 19, 45, 123, 44, 23, 78, 56, 45, 18, 86, 65, 43, 86]

    #if 23 in numbers:
    #    location = numbers.index(23)
    #    print(location)

    #numbers.sort()
    #print(numbers)

    #sorted_list = sorted(numbers)
    #print(sorted_list)

    #print(numbers.index(23))

    #our_numbers = [67, 12, 46, 43, 13]

    #if 43 in our_numbers:
    #    location_43 = our_numbers.index(43)
    #    print(f"\n43 is at location {location_43} in the list.")

    #if 44 in our_numbers:
    #    location_44 = our_numbers.index(44)
    #    print(f"44 is at the location {location_44} in the list.")
    #else:
    #    print(f"44 is not in the elist")

    #color_names = ['orange', 'black', 'green']

    #color_names.insert(0, 'white')
    #print(color_names)

    #color_names.append('blue')
    #print(color_names)

    #color_names.extend(['violet', 'indigo'])
    #print(color_names)

    #color_names.pop()
    #print(color_names)

    #list_with_countries = ['Romania']

    #given_string = 'ROMANIA'

    #list_with_countries.extend(given_string)
    #print(list_with_countries)

    #color_names.remove('violet')
    #print(color_names)

    #color_names.clear()
    #print(color_names)

    #given_list = list(random.randrange(1, 10) for i in range(1, 21))
    #print(given_list)

    #print(given_list.count(9))

    #color_names = ['orange', 'black', 'green']

    #color_names.reverse()
    #print(color_names)

    #ax = reversed(color_names)

    #cp_list = color_names.copy()        # shallow copy

    #cp_list.insert(0, 'white')

    #print(id(color_names[0]))
    #print(id(cp_list[0]))

    #rainbow = ['green', 'orange', 'violet']

    #index_violet = rainbow.index('violet')
    #rainbow.insert(index_violet, 'red')
    #rainbow.append('yellow')

    #print(rainbow)

    #rainbow.reverse()
    #print(rainbow)

    #rainbow.remove('orange')
    #print(rainbow)

    #-----------------------------

    #given_list = [i**2 for i in range(10)]
    #print(given_list)

    #random_list = [random.randrange(1, 21) for i in range(20)]
    #print(random_list)

    #processed_list = [item for item in random_list if item % 2 != 0]
    #print(processed_list)

    #colors = ['green', 'blue', 'yellow', 'black', 'white']

    #upper_colors = [color.upper() for color in colors]
    #print(upper_colors)

    #---------------------------------------------------

    #cubes = [(i, i**3) for i in range(1, 6)]
    #print(cubes)

    #multiples = [i for i in range(3, 30, 3)]
    #print(multiples)

    #----------------------------------------------------
    #Generator expression

    #random_numbers = [random.randrange(1, 10) for i in range(20)]

    #for value in (i ** 2 for i in random_numbers if i % 2 != 0):
    #    print(f"{value}", end=" ")

    #given_list = [10, 3, 7, 1, 9, 4, 2]

    #cube_even_integers = list(i ** 3 for i in given_list if i % 2 == 0)
    #print(cube_even_integers)

    #-------------------------------------------------------

    #random_numbers = [random.randrange(1, 10) for i in range(20)]

    #def is_odd(given_number):
    #    return given_number % 2 != 0

    #processed_list = list(filter(is_odd, random_numbers))
    #print(processed_list)

    #processed_list_2 = [i for i in random_numbers if is_odd(i)]
    #print(processed_list_2)

    #processed_list_3 = list(filter(lambda i: i % 2 != 0, random_numbers))
    #print(processed_list_3)

    #def is_even(given_number):
    #    return given_number % 2 == 0

    #list_mapped = list(map(lambda i: i ** 2,
    #                       filter(is_even, random_numbers)))
    #print(list_mapped)

    #given_numbers = [1, 2, 3, 4, 5]
    #print(functools.reduce(lambda i, j: i + j, given_numbers))

    #---------------------------------------------------------------------

    #numbers = random.sample(range(1, 16), 15)
    #print(numbers)

    #even_list = list(filter(lambda i: i % 2 == 0, numbers))
    #print(even_list)

    #squared_values = list(map(lambda j: j ** 2, numbers))
    #print(squared_values)

    #advanced_list = list(map(lambda k: k ** 2, even_list))
    #print(advanced_list)

    #----------------------------------------------------

    #fah_temps = [41, 32, 212]

    #new_list_celsius = list(map(lambda i: (i, (i - 32) * (5 / 9)), fah_temps))
    #print(new_list_celsius)

    #----------------------------------------------------

    #colors = ['Red', 'orange', 'Blue', 'green']              e
    #print(min(colors, key=lambda i: i.lower()))

    #sorted_colors = sorted(colors, key=lambda i: i.lower())
    #print(sorted_colors)

    #numbers = random.sample(range(1, 21), 20)
    #print(numbers)

    #rev_square_list = list(map(lambda i: i ** 2, reversed(numbers)))
    #print(rev_square_list)

    #zipped = list(zip(numbers, rev_square_list))
    #print(zipped)

#----------------------------------------------------------------

    #foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']
    #print(f"{min(foods, key=lambda j: j.lower())}")
    #print(f"{max(foods, key=lambda j: j.lower())}")

    #random_1 = random.sample(range(1, 11), 10)
    #random_2 = random.sample(range(1, 11), 10)

    new_list = []

    #print(random_1)
    #print(random_2)

    #new_list = list((index, sum(values)) for index, values in enumerate(zip(random_1, random_2)))
    #print(new_list)

    #------------------------------------------
    #given_list_2d_1 = [random.sample(range(1, 11), 10), random.sample(range(1, 11), 10), random.sample(range(1, 11), 10)]
    #print(given_list_2d_1, end="\n\n")

    #for row in given_list_2d_1:
    #    for column in row:
    #        print(f"{column}", end=" ")
    #    print()

    #t = [[10, 7, 3], [20, 4, 17]]

    #for row in range(len(t)):
    #    print(f"Average t{[row]}: {sum(t[row])/len(t[row]):.2f}")

    #total = 0
    #length = 0
    #for sub_list in range(len(t)):
    #    total += sum(t[sub_list])
    #    length += len(t[sub_list])

    #print(total/length)

    #given_list = [random.sample(range(1, 11), 3), random.sample(range(1, 11), 3)]
    #print(given_list)
    #given_list = []
    #element_value = 0

    #for i in range(2):
    #    intermediary_list = []

    #    for j in range(3):
    #        intermediary_list.append(element_value)
    #        element_value += 1
    #    given_list.append(intermediary_list)

    #print(given_list)

    #max_length_list = max(list(len(i) for i in given_list))

    #for column_header in range(0, max_length_list):
    #    print(f"{column_header:>8}.", end="")

    #print()

    #for index_row, row in enumerate(given_list):
        #print(f"{index_row:>4}.", end=" ")
        #for index_column, column in enumerate(row):
        #    print(f"{index_column:>2}{' ':>6}", end=" ")
        #print()

    #-----------------------------------

    #given_alphabet = string.ascii_lowercase

    #print(given_alphabet[0:(len(given_alphabet) // 2)])
    #print(given_alphabet[:(len(given_alphabet) // 2)])
    #print(given_alphabet[(len(given_alphabet) // 2):len(given_alphabet)])
    #print(given_alphabet[(len(given_alphabet) // 2):])
    #print(given_alphabet[0:len(given_alphabet):2])
    #print(given_alphabet[::-1])
    #print(given_alphabet[-1:-len(given_alphabet):-2])
    #print(given_alphabet[-1:-len(given_alphabet):-3])


#def rotate(first, second, third):
#    third, second = second, third
#    second, first = first, second

#    return first, second, third


#def is_ordered(given_list):
#    sorted_list = sorted(given_list)
#    if sorted_list == given_list:
#        return True
#    else:
#        return False


def main():
    #to_execute()
    #print(cube_list(range(1, 11)))
    #print(convert_string('Birthday'))

    #tuples()
    #tuples_temp()
    #three_strings()
    #slicing_lists()
    #actions_on_lists()

    #---------------------------------------------
    #a = 'Doug'
    #b = 22
    #c = 1984
    #a, b, c = rotate(a, b, c)
    #print(f"{a} and {b} and {c}")

    #a, b, c = rotate(a, b, c)
    #print(f"{a} and {b} and {c}")
    print()
    #--------------------------------------------

    #his_list = [3, 2, 3, 4, 5]
    #print(is_ordered(his_list))

    #---------------------------------------------

if __name__ == '__main__':
    main()
