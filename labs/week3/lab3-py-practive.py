"""
lab3 Python Practice
RAGHAVA ADUSUMILLI
2/13/2018
"""
from functools import reduce


def switch_case(str_list):
    """
    Maps strings in the str_list to a new string of same characters, but
    the first letter contains the opposite case
    str_list: list of strings
    Returns: list of original strings with opposite casing for first letter
    """
    return list(map(lambda x: x[0].swapcase() + x[1:], str_list))


def make_title(words):
    """
    Maps words in a list to words in the same list, but as titled strings.
    words: list of words
    Returns: new list of titled words
    """
    return list(map(lambda x: x.title(), words))


def three_times_nums(num_list):
    """
    Maps numbers in the num_list to numbers that are 3 times the original value
    num_list: list of numbers
    Returns: list of numbers that are of three times the values in num_list
    """
    return list(map(lambda x: x*3, num_list))


def square_nums(num_list):
    """
    Maps numbers in the num_list to numbers of same value, but squares the
    number given
    num_list: list of numbers
    Returns: list from num_list which are squared
    """
    return list(map(lambda x: pow(x, 2), num_list))


def double_nums(num_list):
    """
    Maps numbers in the num_list to their doubles
    num_list: list of numbers
    Returns: list of doubled numbers
    """
    return list(map(lambda x: x*2, num_list))


def only_even(mixed_list):
    """
    Filters out odd integers and strings that contain an odd number of
    characters.
    mixed_list: list of integers and/or strings
    Returns: list of only integers and strings that are even or have an even
    number of characters.
    """
    return list(filter(lambda x: not bool(x % 2) if isinstance(x, int)
        else (not bool(len(x) % 2) if isinstance(x, str) else False), mixed_list))


def test_title(names):
    """
    Filters out capitalized and non-cap words into their respective lists.
    names: list of names
    Returns: both lists for review
    """
    return (list(filter(lambda x: x.istitle(), names)),
        list(filter(lambda x: not x.istitle(), names)))


def keep_lowercase(strs):
    """
    Filters out strings that have uppercase values
    strs: list of strings
    Returns: list of strings that do not contain
    uppercase values
    """
    return list(filter(lambda x: not any(map(lambda y: y.isupper(), x)), strs))


def lessthan_5(num_list):
    """
    Filters out numbers less than five
    num_list: list of numbers
    Returns: list of numbers in the original list that are less than five
    """
    return list(filter(lambda x: x > 4, num_list))


def remove_special_characters(string_list):
    """
    Filters out strings that have non-alphanumeric elements
    char_list: list of strings
    Returns: list of strings that have only letters or numbers in them
    """
    return list(filter(lambda x: x.isalpha() or x.isdigit(), string_list))


def greatest_difference(num_list):
    """
    Finds the maximum and minimum numbers in a_list and computes the difference.
    num_list: list of numbers
    Returns: the difference between the maximum and minimum numbers in num_list
    """
    num_list.sort()
    return num_list[-1:][0] - num_list[0]


def create_word(letters):
    """
    Takes a list of characters and creates a word (list with alpha chars only)
    from them.
    letters: list of letters
    Returns: list that has alpha characters only
    """
    return reduce(lambda x, y: x + y, letters)


def multiplication_total_of(num_list):
    """
    Multiplies all the numbers in num_list together and gives the total
    num_list: list of numbers
    Returns: the multiplied total of the numbers in the num_list
    """
    return reduce(lambda x, y: x * y, num_list)


def subtraction_of(number_list):
    """
    Subtracts the numbers in number_list
    number_list: list of numbers
    Returns: the difference of the numbers in the number_list
    """
    return reduce(lambda x, y: x - y, number_list)
