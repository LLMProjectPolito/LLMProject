
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
    # Examples from docstring
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    
    # Boundary cases
    (1, 'i'),
    (1000, 'm'),
    
    # Single digits
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
    (38, 'xxxviii'),
    (39, 'xxxix'),
    (40, 'xl'),
    (44, 'xliv'),
    (49, 'xlix'),
    (50, 'l'),
    (60, 'lx'),
    (70, 'lxx'),
    (80, 'lxxx'),
    (88, 'lxxxviii'),
    (90, 'xc'),
    (94, 'xciv'),
    (99, 'xcix'),
    
    # Hundreds
    (100, 'c'),
    (111, 'cxxi'),
    (200, 'cc'),
    (300, 'ccc'),
    (399, 'cccxcix'),
    (400, 'cd'),
    (444, 'cdxliv'),
    (500, 'd'),
    (600, 'dc'),
    (666, 'dclxvi'),
    (700, 'dcc'),
    (789, 'dcclxxxix'),
    (800, 'dccc'),
    (888, 'dccclxxxviii'),
    (900, 'cm'),
    (944, 'cmxliv'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_valid(number, expected):
    """Test valid inputs within the range 1 <= num <= 1000."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    """Ensure the output is strictly lowercase."""
    result = int_to_mini_roman(426)
    assert result == result.lower()
    assert result == 'cdxxvi'