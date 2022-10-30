#!/usr/bin/python3

"""Calculate how many liters we used for one hundred kilometers. Now the values for liters and kilometers are asked from the user
with validation and all that is needed. At the end the overall liters/kms is calculated"""

import os


def printing_header():
    print(f"\n{'':>20}{'':#>40}")
    print(f"{'#':>21}{'Kilometers Per Liters':>30}{'#':>9}")
    print(f"{'':>20}{'':#>40}")


def catch_input_number_of_questions():

    counter = ""
    while not isinstance(counter, int) or not isinstance(counter, float):
        printing_header()

        print(f'\n - > How many round of values you want to give (q to quit):', end=" ")
        counter = input()

        if counter.lower()[0] == 'q':
            print(f"\n{'Exiting...':>15}")
            os.system('sleep 1')
            exit(0)

        try:
            counter = int(counter)
        except ValueError:
            print(f"\n{' ERROR you need to use an integer or float.':>50}")
            os.system('sleep 1')
            os.system('clear')

            continue

        return counter


def validate_answers(given_answer):
    if given_answer.lower()[0] == 'q':
        print(f"\n{'Exiting...':>15}")
        os.system('sleep 1')
        exit(0)
    elif given_answer.lower()[0] == "e":
        print(f"\n{'Breaking the asking questions scenario...':>55}")
        os.system('sleep 1')
        given_answer = 0

    try:
        given_answer = int(given_answer)
    except ValueError:
        try:
            given_answer = float(given_answer)
        except ValueError:
            print(f"\n{' ERROR you need to use an integer or float.':>55}")
            os.system('sleep 1')
            os.system('clear')
            given_answer = -1

    return given_answer


def ask_questions(round_of_questions):
    i = 0
    question_liters = 0
    list_with_consumption_per_km_onehundred = []
    number_of_liters = ''

    while i < round_of_questions:
        #os.system('clear')
        #printing_header()

        print(f"\n - Round {i + 1} of questions - \n")

        if question_liters == 0:
            print(f' - > How many liters did you used on the road (q to quit or e to end questions):', end=" ")
            answer_liters = input()
            number_of_liters = validate_answers(answer_liters)
            if number_of_liters == -1:
                continue
            elif number_of_liters == 0:
                if len(list_with_consumption_per_km_onehundred) == 0:
                    print(f"\n{' ** No values were given'}")
                    os.system('sleep 1')
                    exit(1)
                else:
                    return list_with_consumption_per_km_onehundred

        print(f' - > Tell me the number of km you driven:', end=" ")
        answer_kms = input()
        number_of_kms = validate_answers(answer_kms)

        if number_of_kms == -1:
            question_liters = 1
        else:
            i += 1
            question_liters = 0
            print(f"{'-' * 46:>47}")
            calc_per_input = number_of_kms / number_of_liters
            list_with_consumption_per_km_onehundred.append(calc_per_input)
            print(f" ** The liters/kms for this was: {calc_per_input:.1f}%", end="\n")
            #os.system('sleep 2')

    return list_with_consumption_per_km_onehundred


def main():
    number_of_rounds = catch_input_number_of_questions()
    list_with_averages_km_liters = ask_questions(number_of_rounds)

    print(f"\n{' *** The overall average liters/kilometers was: '}{sum(list_with_averages_km_liters) / len(list_with_averages_km_liters):.2f}%\n")


if __name__ == "__main__":
    main()
