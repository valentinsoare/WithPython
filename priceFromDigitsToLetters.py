#!/usr/bin/python3

import math

input_value = input("**Enter total price value smaller than 1000 in digits -> ")
final_answer = []
after_point = []

numbers_dict = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: "Five", 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
    18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
    80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand'
}

if not input_value.isdecimal():
    input_value = float(input_value)
    diff = input_value - math.floor(input_value)
    diff = round(diff * 100)
    after_point += str(f'and {diff}/100')
    input_value = math.floor(input_value)
else:
    input_value = int(input_value)

input_value_str = str(input_value)
input_length = len(input_value_str)

for i in reversed(list(numbers_dict.keys())):
    if input_value - i >= 0:
        if input_length == 3:
            final_answer.append(numbers_dict[int(input_value_str[0])])
            final_answer.append(numbers_dict[int(i)])
            input_value = input_value - int(input_value_str[0]) * i
        elif input_length == 2:
            if input_value < 20:
                final_answer.append(numbers_dict[input_value])
            else:
                final_answer.append(numbers_dict[int(i)])
            input_value = input_value - i
        elif input_length == 1 and input_value < 10:
            final_answer.append(numbers_dict[input_value])

        input_value_str = input_value
        input_length -= 1

if len(after_point) > 0:
    final_answer.append(''.join(after_point))

final_string = ' '.join(final_answer)

print(f'{final_string} dollars')

