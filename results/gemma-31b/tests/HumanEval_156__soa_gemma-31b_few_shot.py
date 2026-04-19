
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

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),
    (10, 'x'),
    (19, 'xix'),
    (20, 'xx'),
    (30, 'xxx'),
    (40, 'xl'),
    (50, 'l'),
    (60, 'lx'),
    (70, 'lxx'),
    (80, 'lxxx'),
    (90, 'xc'),
    (100, 'c'),
    (152, 'clii'),
    (200, 'cc'),
    (300, 'ccc'),
    (400, 'cd'),
    (426, 'cdxxvi'),
    (500, 'd'),
    (600, 'dc'),
    (700, 'dcc'),
    (800, 'dccc'),
    (900, 'cm'),
    (999, 'cmxcix'),
    (1000, 'm'),
    (37, 'xxxvii'),
    (88, 'lxxxviii'),
    (399, 'cccxcix'),
    (888, 'dlxxxviii'),
])
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    # Ensure the output is always lowercase
    result = int_to_mini_roman(19)
    assert result == result.lower()
    assert result == 'xix'