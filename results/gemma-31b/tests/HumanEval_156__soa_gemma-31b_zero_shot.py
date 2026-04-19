
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
    (11, 'xi'),
    (19, 'xix'),
    (20, 'xx'),
    (39, 'xxxix'),
    (40, 'xl'),
    (44, 'xliv'),
    (49, 'xlix'),
    (50, 'l'),
    (58, 'lviii'),
    (89, 'lxxxix'),
    (90, 'xc'),
    (94, 'xciv'),
    (99, 'xcix'),
    (100, 'c'),
    (101, 'ci'),
    (140, 'cxl'),
    (152, 'clii'),
    (199, 'cxxcix'),
    (200, 'cc'),
    (300, 'ccc'),
    (399, 'cccxcix'),
    (400, 'cd'),
    (426, 'cdxxvi'),
    (444, 'cdxliv'),
    (499, 'cdxcix'),
    (500, 'd'),
    (555, 'dlv'),
    (600, 'dc'),
    (700, 'dcc'),
    (800, 'dccc'),
    (888, 'dlxxxviii'),
    (900, 'cm'),
    (909, 'cmix'),
    (944, 'cmxliv'),
    (990, 'cmxc'),
    (999, 'cmxcix'),
    (1000, 'm'),
])
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    # Ensure the output is always lowercase
    result = int_to_mini_roman(19)
    assert result == result.lower()
    assert result == 'xix'

def test_int_to_mini_roman_boundaries():
    # Test the absolute boundaries of the restriction 1 <= num <= 1000
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'