"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    return "This function returns a string value."

def give_me_an_integer():
    return 1

def give_me_a_boolean():
    return True

def give_me_a_float():
    return 1.0

def give_me_a_list():
    return ["this", "is", "a", "list"]

def give_me_a_dictionary():
    return {"first": "entry"}

def give_me_a_tuple():
    return (1, )

def sum_numbers_one_to_ten():
    return sum(range(1, 11))

def check_is_even(number):
    return number % 2 == 0

def check_is_less_than(number1, number2):
    return number1 < number2

# Additional method - 1
def check_is_odd(number):
    return number % 2 != 0

# Additional method - 2
def check_is_greater_than(number1, number2):
    return number1 > number2
