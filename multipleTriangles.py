#!/usr/bin/python

def first_triangle(input_var):
    for j in range(0, input_var):
        print(f"*", end="")
    for k in range(0, 12 - input_var):
        print(f" ", end="")

    print(f"   ", end="")


def second_triangle(input_var):
    for x in range(12, input_var, - 1):
        print(f"*", end="")
    for z in range(0, input_var):
        print(f" ", end="")

    print(f"   ", end="")


def third_triangle(input_var):
    for b in range(0, input_var):
        print(f" ", end="")
    for k in range(0, 12 - input_var):
        print("*", end="")

    print(f"   ", end="")


def forth_triangle(input_var):
    for a in range(12 - input_var, 1, -1):
        print(f" ", end="")
    for c in range(0, input_var):
        print(f"*", end="")

    print()


def main():
    for i in range(1, 12):
        first_triangle(i)
        second_triangle(i)
        third_triangle(i)
        forth_triangle(i)

main()