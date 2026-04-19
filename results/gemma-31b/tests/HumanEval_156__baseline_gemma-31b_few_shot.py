
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
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
])
def test_int_to_mini_roman_examples(number, expected):
    """Test the examples provided in the docstring."""
    assert int_to_mini_roman(number) == expected

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
])
def test_int_to_mini_roman_single_digits(number, expected):
    """Test all single digit values from 1 to 9."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (10, 'x'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
])
def test_int_to_mini_roman_tens(number, expected):
    """Test key milestones in the tens place."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
])
def test_int_to_mini_roman_hundreds(number, expected):
    """Test key milestones in the hundreds place."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_boundary_max():
    """Test the upper boundary constraint (1000)."""
    assert int_to_mini_roman(1000) == 'm'

@pytest.mark.parametrize("number, expected", [
    (38, 'xxxviii'),
    (88, 'lxxxviii'),
    (388, 'cccviii'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_complex_combinations(number, expected):
    """Test complex numbers with multiple repetitions and subtractive notation."""
    assert int_to_mini_roman(number) == expected