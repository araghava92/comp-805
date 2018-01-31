"""
lab2.py
RAGHAVA ADUSUMILLI
01/30/2017
"""
import re

#1  Function Interface:
def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    squared_nums_list = []
    # Iterate num_list for numbers
    for num in num_list:
        squared_nums_list.append(pow(num, 2))

    return squared_nums_list


def  check_title(title_list):
    """
    Removes strings in title_list that aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    """
    res_list = []
    for title in title_list:
        if title.istitle():
            res_list.append(title)

    return res_list
