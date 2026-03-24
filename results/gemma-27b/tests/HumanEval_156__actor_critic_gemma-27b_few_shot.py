
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    result = ""

    for value, symbol in sorted(roman_map.items(), reverse=True):
        while number >= value:
            result += symbol
            number -= value

    return result.lower()

import pytest

@pytest.mark.parametrize("number, expected", [
    # Single digits
    (1, 'i'),
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),

    # Tens
    (10, 'x'),
    (11, 'xi'),
    (14, 'xiv'),
    (15, 'xv'),
    (19, 'xix'),
    (20, 'xx'),
    (30, 'xxx'),
    (39, 'xxxix'),
    (40, 'xl'),
    (49, 'xlix'),
    (50, 'l'),
    (90, 'xc'),

    # Hundreds
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    (1000, 'm'),

    # Complex numbers
    (152, 'clii'),
    (426, 'cdxxvi'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
    (399, 'cccix'),
    (899, 'dcccxcix'),
    (99, 'xcix'),
    (998, 'cmxcviii'),
    (388, 'cccLxxxviii'), # Added test case for all symbols
])
def test_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected

def test_mini_roman_lower_bound():
    assert int_to_mini_roman(1) == 'i'