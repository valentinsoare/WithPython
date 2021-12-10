#!/usr/bin/python

binary_number = input("\n\033[1m**Add your number in binary format:\033[0m ")

steps = 0
given_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
final_number = []

for i in binary_number:
    if i not in "10":
        print(f"\033[1;31m - > ERROR the number is not in binary format.\033[0m", end="\n")
        exit(1)

given_number = int(binary_number)

while given_number // 10 != 0:
    extract = given_number % 10
    given_number = given_number // 10

    if extract == 1:
        final_number.append(given_list[steps])

    steps += 1

final_number.append(given_list[steps])

print(f" \033[1m- > Binary \033[1;31m{binary_number}\033[0m is \033[1;32m{sum(final_number)}\033[0m in decimal.\033[0m")