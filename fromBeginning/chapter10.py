#!/usr/bin/python


import math
import dataclasses
from typing import Union, ClassVar
from decimal import Decimal
from account import Account
from collections import namedtuple


class Point:
    def __init__(self,x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError('x coordinate should be an integer!')
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError('y coordinate should be an integer!')
        self._y = value

    def move(self, x, y):
        if not (isinstance(x, int) or isinstance(y, int)):
            raise ValueError('X and Y coordinates should be integer values!')

        self._x = x
        self._y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class Circle:
    def __init__(self, radius, x, y):
        self._radius = radius
        self._point = Point(x, y)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int):
            raise ValueError('Radius value should be an integer!')
        self._radius = value

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        point = namedtuple('point', ['x', 'y'])

        if not isinstance(point, tuple):
            raise ValueError('When creating point as a parameter in circle we need a tuple with two integers as coordinates!')

        to_use = point(x=value[0], y=value[1])
        self._point = Point(*to_use)

    def move(self, x, y):
        return self.point.move(x, y)

    def __str__(self):
        return f'{str(self.point)}, radius: {self.radius}'

    def __format__(self, value):
        return f'{str(self):{value}}'


class MainAccount:
    def __init__(self, name: str, balance: Decimal):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance


def play_with_accounts():
    main_account = Account(Decimal('1871119520010'), 'Valentin Soare', Decimal('87584'), 'VIP', 'Bucharest')

    main_account.deposit(Decimal('231'))
    print(f"Account nuber: {main_account.account_number}", flush=True)
    print(f"Balance: {main_account.balance:,}$", flush=True)
    main_account.balance = Decimal('150000.00')


def working_with_named_tuples():
    Card = namedtuple('Card', ['face', 'suit'])
    first = Card(face='aiurea', suit='goot_to_go')

    given_values = ['Queen', 'Hearts']
    card = Card._make(given_values)
    print(card)


class Square:
    def __init__(self, side):
        self.side = side
        self._perimeter = self.perimeter
        self._area = self.area
        self._diagonal = self.diagonal

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if not isinstance(value, Union[int, float]) or value <= 0:
            raise ValueError('Side value must be an integer greater than zero!')

        self._side = value

    @property
    def perimeter(self):
        return 4 * self.side

    @property
    def area(self):
        return self.side * self.side

    @property
    def diagonal(self):
        return math.sqrt((2 * self.side**2))


class Invoice:
    def __init__(self, part_number, part_description, quantity, price):
        self.part_number: str = part_number
        self.part_description: str = part_description
        self.quantity: int = quantity
        self.price: Decimal = price
        self._all_properties = None
        self._nr_of_properties = None

    @property
    def part_number(self):
        return self._part_number

    @part_number.setter
    def part_number(self, number):
        if not isinstance(number, str) or number.isalpha():
            raise ValueError('Part number should be a string containing digits and alpha numerical characters.')

        self._part_number = number

    @property
    def part_description(self):
        return self._part_description

    @part_description.setter
    def part_description(self, description):
        if not isinstance(description, str) or description.isnumeric():
            raise ValueError('Description should be a string and containing alpha characters!')

        self._part_description = description

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity_value):
        if not isinstance(quantity_value, int) or quantity_value < 0:
            raise ValueError('Quantity should be an integer and greater or equal to zero!')

        self._quantity = quantity_value

    @property
    def price(self):
        return self._price.quantize(Decimal('0.00'))

    @price.setter
    def price(self, price):
        if not isinstance(price, Decimal) or price <= Decimal('0.00'):
            raise ValueError('Price should be a decimal value and greater than zero')

        self._price = price.quantize(Decimal('0.00'))

    def calculate_invoice(self):
        return self.quantity * self.price

    def export_properties_as_tuple(self):
        invoice = namedtuple('invoice', ['part_number', 'part_description', 'quantity', 'price'])
        return invoice(self.part_number, self.part_description, self.quantity, self.price)

    def populate_properties_list(self):
        self._all_properties = [self.part_number, self.part_description, self.quantity, self.price]
        self._nr_of_properties = len(self._all_properties)

    @property
    def all_properties(self):
        return self._all_properties

    @property
    def nr_of_properties(self):
        return self._nr_of_properties

    def __str__(self):
        return f'part_number: {self.part_number}, part_description: {self.part_description},' \
               f' quantity: {self.quantity}, price: {self.price}'


def create_new_type():
    given_properties = ['account', 'name', 'balance']

    usable_account = dataclasses.make_dataclass(cls_name='UsableAccount', fields=given_properties)
    first_account = usable_account(account='RORNCB18711119520010', name='Valentin Soare', balance=Decimal('10_000'))

    @dataclasses.dataclass(order=True)
    class CoolSquare:
        x: float
        y: float

        def __str__(self):
            return f'x: {self.x}, y: {self.y}'

    first = CoolSquare(20, 40)
    print(first)

def if_setter():
    valentin = MainAccount(name='Valentin Soare', balance=Decimal('150'))
    valentin.balance = 20
    print(valentin.balance)


def creating_immutable_type():
    given_list_of_properties = ['country', 'city', 'street', 'postalcode']

    my_home = dataclasses.make_dataclass(cls_name='my_home', fields=given_list_of_properties, frozen=True)
    garsoniera_lucretiu = my_home(country='Romania', city='Bucuresti', street='Lucretiu Patrascanu', postalcode='030504')

    for field in dataclasses.fields(garsoniera_lucretiu):
        print(f"{field.name}: {str(getattr(garsoniera_lucretiu, field.name))}")

def creating_another_frozen_class():
    @dataclasses.dataclass(order=True, frozen=True)
    class Apartment:
        country: str
        city: str
        street: str
        postalcode: int

    def __str__(self):
        return f"country: {self.country}\ncity: {self.city}\nstreet: {self.street}\npostalcode: {self.postalcode}"

    my_home = Apartment(country='Romania', city='Bucuresti', street='Lucretiu Patrascanu', postalcode=0o30504)

    #my_home.street = 'nebunie mare'


def main() -> None:
    #play_with_accounts()
    #working_with_named_tuples()
    #if_setter()

    #---------------------------------------

    #first_circle = Circle(32, 14, 12)
    #print(first_circle)

    #first_circle.move(10, 14)
    #print(f"{first_circle:>50}")

    #----------------------------------------

    #first_sqr = Square(20.2)
    #print(first_sqr.diagonal)

    #----------------------------------------

    #first_invoice = Invoice(part_number='1234A', part_description='To Go To School', quantity=40, price=Decimal('35'))
    #print(first_invoice)

    #first_invoice.populate_properties_list()
    #print(first_invoice.all_properties)

    #ax = first_invoice.export_properties_as_tuple()
    #print(ax)

    #print(first_invoice.calculate_invoice())

    #--------------------------------------

    #create_new_type()

    #-------------------------------------

    #creating_immutable_type()

    creating_another_frozen_class()


if __name__ == '__main__':
    main()
