
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

import pytest

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    >>> int_to_mini_roman(1) == 'i'
    >>> int_to_mini_roman(1000) == 'm'
    >>> int_to_mini_roman(3) == 'iii'
    >>> int_to_mini_roman(20) == 'xx'
    >>> int_to_mini_roman(300) == 'ccc'
    """
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}

    if not 1 <= number <= 1000:
        raise ValueError("Input must be between 1 and 1000")

    # Use a dictionary comprehension for a more concise roman_map
    roman_map_dict = {k: v for k, v in roman_map.items()}

    result = ""
    values = sorted(roman_map_dict.keys(), reverse=True)

    for value in values:
        while number >= value:
            result += roman_map_dict[value]
            number -= value

    return result