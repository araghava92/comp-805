"""
lab3 Python Practice
RAGHAVA ADUSUMILLI
2/13/2018
"""


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
    return list(filter(lambda x: x.istitle(), names)),
        list(list(filter(lambda x: not x.istitle(), names)))
