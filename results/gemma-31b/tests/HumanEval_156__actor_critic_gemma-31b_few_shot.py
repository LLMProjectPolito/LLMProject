
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

def test_roman_examples():
    """Tests the examples provided in the docstring."""
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

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
def test_roman_single_digits(number, expected):
    """Tests all single digit cases including the subtraction rule for 4 and 9."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (10, 'x'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    (1000, 'm'),
])
def test_roman_milestones(number, expected):
    """Tests the key Roman numeral symbols and their subtraction pairs."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (38, 'xxxviii'),
    (88, 'lxxxviii'),
    (399, 'cccxcix'),
    (888, 'dlxxxviii'),
    (999, 'cmxcix'),
])
def test_roman_complex_combinations(number, expected):
    """Tests complex numbers that require multiple symbols and subtraction rules."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("invalid_input", [
    0, 
    -1, 
    -100, 
    1001, 
    5000
])
def test_roman_invalid_range(invalid_input):
    """Tests that inputs outside the range 1 <= num <= 1000 raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(invalid_input)

@pytest.mark.parametrize("wrong_type", [
    "10", 
    10.5, 
    None, 
    [], 
    {}
])
def test_roman_type_safety(wrong_type):
    """Tests that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(wrong_type)