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
