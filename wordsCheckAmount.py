#!/usr/bin/python


def from_digits_to_letters(input_amount, after_dot):

    numbers_dict = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: "Five", 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'One Thousand'
    }

    numbers_after_processed = []

    def for_two_digits(input_value):
        after_mod = input_value % 10
        input_value = input_value - after_mod
        numbers_after_processed.extend([input_value, after_mod])
        input_value = 0

        return input_value

    def for_three_digits(input_value):
        after_mod = input_value % 100
        input_value = input_value - after_mod
        input_value = list(str(input_value))
        numbers_after_processed.extend([int(input_value[0]), 100])

        return after_mod

    to_remember = input_amount

    while input_amount != 0:
        if input_amount in numbers_dict.keys():
            numbers_after_processed.append(input_amount)
            input_amount = 0
        elif len(str(input_amount)) == 2:
            input_amount = for_two_digits(input_amount)
        else:
            input_amount = for_three_digits(input_amount)

    print(f"\n\033[1m From digits {to_remember} dollars to letters:\033[0m", end=" ")

    for i in numbers_after_processed:
        print(f" \033[1;31m{numbers_dict.get(i)}\033[0m", end="")

    if after_dot:
        print(f"\033[1;31m and {after_dot}/100 dollars\033[0m", end="\n")
    else:
        print(f"\033[1;31m dollars\033[0m", end="\n")


def processed_input_digit_value(given_input_value):
    after_dot_amount = 0

    try:
        amount = int(given_input_value)
    except ValueError:
        given_input_value = list(given_input_value)
        index_dot = given_input_value.index('.')
        amount = int(''.join(given_input_value[0:index_dot]))
        after_dot_amount = int(''.join(given_input_value[(index_dot+1):]))

    return amount, after_dot_amount


def catch_value():
    ask_for_value = input("\n\033[1m - > Enter dollars amount in digits less than 1000:\033[0m ")
    return ask_for_value


def main():
    amount = catch_value()
    processed_amount, after_dot_amount = processed_input_digit_value(amount)
    from_digits_to_letters(processed_amount, after_dot_amount)


main()
