
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
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    (99, 'xcix'),
    (100, 'c'),
    (152, 'clii'),
    (400, 'cd'),
    (426, 'cdxxvi'),
    (500, 'd'),
    (888, 'dlxxxviii'),
    (900, 'cm'),
    (999, 'cmxcix'),
    (1000, 'm'),
])
def test_int_to_mini_roman_valid_cases(number, expected):
    """Test standard Roman numeral conversions within the range 1-1000."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    """Ensure the output is always lowercase."""
    result = int_to_mini_roman(426)
    assert result == result.lower()

@pytest.mark.parametrize("number", [
    1,
    1000,
])
def test_int_to_mini_roman_boundaries(number):
    """Test the boundary values of the restriction 1 <= num <= 1000."""
    result = int_to_mini_roman(number)
    assert isinstance(result, str)
    assert len(result) > 0