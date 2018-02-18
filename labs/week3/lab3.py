"""
lab3.py
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

    >>> squared_nums([1, 2, 3])
    [1, 4, 9]
    >>> squared_nums([])
    []
    >>> squared_nums([-1, -2])
    [1, 4]
    """
    squared_nums_list = [ ]
    # Iterate num_list for numbers
    for num in num_list:
        squared_nums_list.append(pow(num, 2))

    return squared_nums_list


def check_title(title_list):
    """
    Removes strings in title_list that aren't title case
    title_list: list of strings
    Returns: list of strings that are titles

    >>> check_title(["Hello World", "Hello_world", "Hello_World"])
    ['Hello World', 'Hello_World']
    >>> check_title(["123466", "137682746"])
    []
    >>> check_title([])
    []
    """
    res_list = []
    for title in title_list:
        if title.istitle( ):
            res_list.append(title)

    return res_list


def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: A dictionary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item currently on hand
    Returns: Updated dictionary where each inventory item is restocked.

    >>> restock_inventory({"1": 1, "2": 2, "3": 3}) == {'1': 11, '2': 12, '3': 13}
    True
    >>> restock_inventory({"-1": -1, "-2": -2,"-3": -3}) == {'-1': 9, '-2': 8,'-3': 7}
    True
    >>> restock_inventory({}) == {}
    True
    """
    new_inventory = { }
    for key, val in inventory.items():
        new_inventory[key] = val + 10

    return new_inventory


def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: Dictionary with:
        key: string that is the name of the inventory item.
        value: integer that equals the number of that item currently on hand.
    Returns: the same inventory_dict with any item that had 0 quantity removed.
    """
    inventory_copy = inventory.copy( )
    for key in inventory_copy.keys( ):
        if not bool(inventory[key]):
            del inventory[key]

    return inventory


def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: A dictionary of grades with:
        key: string of student's name
        value: list of integer grades received in class
    Returns: Dictionary that averages out the grades of each student.
    """
    student_names = grades.keys( )
    avg_dict = dict.fromkeys(student_names)
    for name in student_names:
        grades_list = grades[name]
        avg_dict[name] = sum(grades_list) / len(grades_list)

    return avg_dict


if __name__ == "__main__":
    import doctest
    doctest.testmod( )
