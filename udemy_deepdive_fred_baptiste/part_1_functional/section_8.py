#!/usr/bin/python

from re import split
import dataclasses
from typing import Union
from collections import namedtuple
from functools import singledispatch
from random import randint, random


def add_city(name_of_city):
    if name_of_city:
        cities.append(name_of_city)

    return cities


def sort_cities_by_population(descending):
    return list(sorted(cities, key=lambda i: i[2], reverse=descending))


def working_with_simple_tuples():
    global cities
    cities = list()

    def working_with_cities():
        return cities

    working_with_cities.add_city = add_city
    working_with_cities.display = cities
    working_with_cities.sort_cities_by_population = sort_cities_by_population

    return working_with_cities

#-----------------------------------------------


def playing_with_tuples():
    given_tuple = 'Lux', 'opulenta', 'in', 'Bucuresti', 'saracie', 'haos', 'jeg'

    condition, _, link, city, *__ = given_tuple
    print(f"{condition} {link} {city}")


def use_named_tuples():
    city_population = namedtuple(typename='city_population', field_names=['city_name', 'country', 'population'])
    bucuresti = city_population(city_name='Bucuresti', country='RO', population=1_500_000)
    london = city_population(city_name='London', country='UK', population=8_780_000)
    beijing = city_population(city_name='Beijing', country='China', population=21_000_000)

    cities = [bucuresti, london, beijing]
    pop = (i.population for i in cities)
    print(sum(sorted(pop, reverse=False)))

    for i, j in zip(range(len(cities)), cities):
        print(j.city_name)

    for k, l in enumerate(cities):
        print(l.country)


def using_nt():
    person = namedtuple(typename='person', field_names=['first_name', 'last_name', 'age', 'sex', 'address'])
    valentin_soare = person(first_name='Valentin', last_name='Soare', age=35, sex='male', address='Lucretiu Patrascanu, Nr. 9')

    # modifyeing a named tuple
    valentin_soare = valentin_soare._replace(address='WTF :D')
    print(valentin_soare)

    valentin_soare = person._make((*valentin_soare[:4], 'Zeilor Nr. 21'))       # using _make method!
    print(valentin_soare)


    valentin_soare = person(*valentin_soare[:4], 'Libertatii 21') # using tuples and slicing


    *rest_of_elements, address = valentin_soare                   # using extended unpacking :D
    address = 'Bld. C.F.R. Bl. 35/335'
    valentin_soare = person(*rest_of_elements, address)

    print(valentin_soare)

    #tudorina_soare = person(first_name='Tudorina', last_name='Soare', age=56)
    #stelian_soare = person(first_name='Stelian', last_name='Soare', age=54)

    #if isinstance(stelian_soare, tuple):
    #    print(f"Yes it is!")

    #if valentin_soare != stelian_soare:
    #    print(f"They are different!")

    a = (2, 3)
    b = (1, 1)

    product = sum(i[0] * i[1] for i in list(zip(a, b)))
    print(product)

#    @dataclasses.dataclass(order=True)
#    class CoolSquare:
#        x: float
#        y: float

#        def __str__(self):
#            return f'x: {self.x}, y: {self.y}'

#    first = CoolSquare(20, 40)
#    print(first)

#def grades_book(*, name_of_the_grade_book: str, students_names: list, grade_per_students: dict):


    person = namedtuple(typename='person', field_names=['first_name', 'last_name', 'age', 'sex', 'address'])
    valentin_soare = person(first_name='Valentin', last_name='Soare', age=35, sex='male', address='Lucretiu Patrascanu, Nr. 9')


    # exxtending a nameed tuple

    person_ext = namedtuple('person_ext', person._fields + ('country',))
    #valentin_soare = person_ext(first_name='Valentin', last_name='Soare', age=35, sex='male',
    #                        address='Lucretiu Patrascanu, Nr. 9', country='Romania')


    #valentin_soare = person(*valentin_soare, 'Romania')


    valentin_soare = person_ext._make([*valentin_soare, 'Romania'])
    print(valentin_soare)



def named_tuple_in_the_making(values: list, field_names: list):
    print()



def dataclass_in_the_making(values: list, field_names: list):
    return f'Nebunie'


def tuple_in_the_making(values: list, field_names: list):
    print()


def creating_data_struct(values: list, field_names: list, type_of_struct: str = 'namedtuple'):
    struct = {'namedtuple': named_tuple_in_the_making,
              'dataclass': dataclass_in_the_making,
              object: tuple_in_the_making}

    return struct.get(type_of_struct, struct[object])(values, field_names)


def mod_ext_named_tuples():
    city = namedtuple('city', ['name', 'country', 'population', 'mayor', 'university'])

    #bucuresti = city(name='bucuresti', country='Romania', population='1_500_000',
    #                 mayor='Nicusor', university='Universitatea Bucuresti')

    #bucuresti = bucuresti._replace(population='1_850_000')
    #print(bucuresti)

    #extended_city = namedtuple('extended_city', [*city._fields, 'capital'])
    #bucuresti = extended_city(*bucuresti, 'Bucuresti')

    #extended_city.__doc__ = 'sa fie bine sa nu fie rau'
    #print(extended_city.__doc__)


    city = namedtuple(typename='city', field_names=['name', 'country', 'population', 'mayor', 'university']) # for default values
    city_default = city(name=None, country=None, population=0, mayor=None, university=None)    # this is a prototype

    giurgiu = city_default._replace(name='Giurgiu', country='RO', population=65_500, mayor='Anghelescu')
    print(giurgiu)


    city = namedtuple(typename='city', field_names=['name', 'country', 'population', 'mayor', 'university'])
    city.__new__.__defaults__ = (None, None, 0, None, None)

    giurgiu = city(name='Giurgiu', country='Giurgiu', population=65_000, mayor='Anghelescu')
    print(giurgiu)


def creating_cars(brand=None, model=None, year=2021, fuel=None, kilometers=0, top_speed=None):
    fields = ['brand', 'model', 'year', 'fuel', 'kilometers', 'top_speed']
    car = namedtuple(typename='car', field_names=fields)

    return car(*[brand, model, year, fuel, kilometers, top_speed])


def create_color():
    color = namedtuple(typename='color', field_names=['red', 'blue', 'green', 'alpha'])
    return color(randint(0, 255), randint(0, 255), randint(0, 255), round(random(), 2))


def from_dict_to_named_tuple():
    cars_dict = dict(brand='bmw', model='3 series', year=2022, fuel='gasoline')

    car = namedtuple('car', cars_dict.keys())
    #bmw = car(*cars_dict.values()) #or
    bmw = car(**cars_dict)                 # this is the best aproach when unpacing a dict will have key - value pair.

    boss_da_boss = 'brand'
    print(getattr(bmw, boss_da_boss))
    print(getattr(bmw, 'top_speed', 'Nu exista!'))


def read_a_mongo_db_to_namedtuple():
    data_list = [
        {'k1': 'bmw 3 series'},
        {'k1': 'mazda 6'},
        {'k1': 'civic 5D', 'k2': 'honda typeR', 'k3': 'mercedes G klass'},
        {'k1': 'audi a8 long'}
    ]

    keys: set = set(j for i in data_list for j in i.keys())
    struct = namedtuple(typename='car', field_names=sorted(keys))

    struct.__new__.__defaults__ = (None, ) * len(struct._fields)

    list_with_named_tuples_from_dict = dict(enumerate(struct(**i) for i in data_list))

    for i, j in list_with_named_tuples_from_dict.items():
        print(j.k1)


def tuplify_dict_of_dicts(dict_to_convert: dict) -> dict:
    processing_keys: list = [j for i in dict_to_convert.values() for j in i.keys()]
    keys_for_nt: list = [j for i, j in enumerate(processing_keys) if j not in processing_keys[:i]]

    struct_nt: namedtuple = namedtuple(typename='generic_nt', field_names=keys_for_nt, rename=True)
    struct_nt.__new__.__defaults__ = (None,) * len(struct_nt._fields)

    return dict(enumerate(struct_nt(**i) for i in dict_to_convert.values()))


def main():

    az = creating_data_struct(['first_name', 'last_name', 'age', 'sex', 'address'],
                              ['Valentin', 'Soare', 35, 'male', 'Lucretiu Patrascanu, Nr. 9'], 'dataclass')
    print(az)

    #cities = working_with_simple_tuples()
    #cities.add_city(('Craiova', 'RO', 700_000))
    #cities.add_city(('Iasi', 'RO', 200_000))
    #cities.add_city(('Chicago', 'US', 4_000_000))
    #cities.add_city(('New York', 'US', 8_000_000))

    #print(cities.display)
    #print(cities.sort_cities_by_population(descending=False))
    #---------------------------------------------------------
    #playing_with_tuples()
    #------------------------------
    #use_named_tuples()
    #------------------------------
    #using_nt()
    #------------------------------
    #mod_ext_named_tuples()
    #---------------------------

    #honda = creating_cars(brand='Honda',
    #                      model='Civic 5D',
    #                      year=2021,
    #                      fuel='gasoline',
    #                      kilometers=51_500,
    #                      top_speed=230)
    #print(honda._asdict())

    #-------------------------------

    #coloring = create_color()
    #coloring.red

    #-------------------------------
    #from_dict_to_named_tuple()
    #-------------------------------
    #read_a_mongo_db_to_namedtuple()
    #-------------------------------
    given_dict = {0: {'first_name': 'Valentin', 'last_name': 'Soare', 'age': 35, 'sex': 'male', 'occupation': 'engineer'},
                  1: {'first_name': 'Tudorina', 'last_name': 'Soare', 'occupation': 'teacher'},
                  2: {'first_name': 'Stelian', 'last_name': 'Soare', 'age': 54, 'occupation': 'police man'}}

    for i, j in tuplify_dict_of_dicts(given_dict).items():
        print(f"{j.first_name} and {j.occupation}")

    print(split(r',\s*', 'Lucretiu Patrascanu,Nr.9,Bl. Y2,Ap. 21,Bucuresti,Romania,030504'))



if __name__ == '__main__':
    main()
