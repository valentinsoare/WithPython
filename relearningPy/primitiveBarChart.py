#!/usr/bin/python

def create_and_print_header(given_message):
    len_of_message = len(given_message)

    print(f"\n{' ' * (12 + (len_of_message // 2))}{given_message}")
    print(f"{' ' * 12}{'-' * (2 * len_of_message)}")


def draw_bar_chart(list_with_values):
    print(f"\n{'Index'}{'Country':>16}{'Value':>12}{'Bar':>8}")

    for index, value in enumerate(list_with_values):
        print(f"{index:>5} {value[0]:>15} {value[1]:>11}{' ' * 4}", end=" ")
        print(f"{('*' * value[1])}")


def main():
    given_list_with_values = [('China', 30), ('Romania', 12), ('United States', 44), ('Rusia', 40), ('UK', 39)]

    create_and_print_header('Drawing Bar Chart')
    draw_bar_chart(given_list_with_values)


if __name__ == '__main__':
    main()
