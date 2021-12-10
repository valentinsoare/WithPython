#!/usr/bin/python

e_constant = 1
x = 0
final = 1

for i in range(1, 11):
    while i - x != 0:
        calc = i - x
        final = calc * final
        x += 1
    e_constant = e_constant + (1 / final)
    x = 0
    final = 1

    print(f"Iteration: {i} - > {e_constant}")
