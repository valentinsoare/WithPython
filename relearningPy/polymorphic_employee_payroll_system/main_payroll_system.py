#!/usr/bin/python


from decimal import Decimal
from hourlyEmployee import HourlyEmployee
from salariedEmployee import SalariedEmployee


def init_employee():
    valentin = SalariedEmployee(first_name='Valentin', last_name='Soare',
                                cnp=1871119520010, weekly_salary=Decimal('1_200'), trial_period=3)

    tudorina = HourlyEmployee(first_name='Tudorina', last_name='Soare',
                              cnp=2784636978129, hours_worked=Decimal('40'),
                              wage_per_hour=Decimal('12.44'))

    print(f"\n{' ' * 2} * {valentin}")
    print(f"{' ' * 1} ** {tudorina}")

    print(len(tudorina))


def main():
    init_employee()


if __name__ == '__main__':
    main()
