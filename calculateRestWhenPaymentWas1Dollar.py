#!/usr/bin/python3

payment = 100  ### you pay 1 dollar 100 cents and input_price will be substract from payment and the rest will be given in a fewest
#number of pennies, nickels, dimes and quarters

input_price = int(input("\n - > Enter a purchase price in cents not greater than 100 (1 dollar): "))

values_for_money = [25, 10, 5, 1]
values_string = ["quarters", "dimes", "nickels", "pennies"]
rest_of_payment = 100 - input_price

x = 0
y = 0
print(f"\n1 penny = 1 cent\n1 nickel = 5 cents\n1 dime = 10 cents\n1 quarter = 25 cents")
print(f"\n ***Your rest is {rest_of_payment} cents and we will give you that rest in: ")

while rest_of_payment != 0:

    calc = rest_of_payment // values_for_money[x]

    if calc != 0:
        print(f" - {calc} {values_string[y]}")

    rest_of_payment = rest_of_payment - calc * values_for_money[x]

    x += 1
    y += 1

