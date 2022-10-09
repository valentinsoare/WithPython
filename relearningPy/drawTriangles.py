#!/usr/bin/python

def one_below_the_other(size_of_triangle):
    for i in range(size_of_triangle):
        for j in range(i+1):
            print(f"*", end="")
        print()

    print()

    for k in range(size_of_triangle):
        for z in range(size_of_triangle - k):
            print(f"*", end="")
        print()

    print()

    for t in range(size_of_triangle):
        print(f"{' ' * t}", end="")
        for x in range(size_of_triangle - t):
            print(f"*", end="")

        print()

    print()

    for r in range(size_of_triangle):
        print(f"{' ' * (size_of_triangle - (r + 1))}", end="")
        for w in range(r+1):
            print(f"*", end="")
        print()


def main():
    one_below_the_other(12)


if __name__ == "__main__":
    main()
