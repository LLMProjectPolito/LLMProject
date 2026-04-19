
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
    roman_map = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')
    ]
    result = []
    for value, symbol in roman_map:
        while number >= value:
            result.append(symbol)
            number -= value
    return "".join(result)

import pytest

@pytest.mark.parametrize("number, expected", [
    # Basic single digits
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
    (20, 'xx'),
    (30, 'xxx'),
    (40, 'xl'),
    (50, 'l'),
    (60, 'lx'),
    (70, 'lxx'),
    (80, 'lxxx'),
    (90, 'xc'),
    
    # Hundreds
    (100, 'c'),
    (200, 'cc'),
    (300, 'ccc'),
    (400, 'cd'),
    (500, 'd'),
    (600, 'dc'),
    (700, 'dcc'),
    (800, 'dccc'),
    (900, 'cm'),
    
    # Boundary / Max
    (1000, 'm'),
    
    # Examples provided in docstring
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    
    # Complex combinations
    (39, 'xxxix'),
    (44, 'xliv'),
    (99, 'xcix'),
    (399, 'cccxcix'),
    (444, 'cdxliv'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected