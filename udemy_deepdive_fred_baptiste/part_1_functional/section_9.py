#!/usr/bin/python
import importlib.util
import sys
import math
import types


def func():
    a = 1001
    print(locals())


def check_modules():
    if isinstance(math, types.ModuleType):
        print('Good')


def to_say_hello():
    return f"Say Hello!!"


def define_a_module():
    love_testing = types.ModuleType('love_testing', 'This is our love for modules')
    love_testing.hello = to_say_hello

    hello = love_testing.hello()

    print(hello)


def how_modules_are_imported():
    python_location = sys.prefix
    print(python_location)

    python_binaries_location = sys.exec_prefix
    print(python_binaries_location)

    look_for_imports = sys.path
    print(look_for_imports)


def main():
    #func()
    #print(globals())
    #print(sys.modules.keys())
    #print(fractions.__file__)

    #check_modules()
    #define_a_module()
    #how_modules_are_imported()



if __name__ == '__main__':
    main()
