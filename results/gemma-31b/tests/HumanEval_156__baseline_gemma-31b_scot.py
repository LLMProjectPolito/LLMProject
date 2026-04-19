
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
def test_docstring_examples(number, expected):
    """Verify the examples provided in the function docstring."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (1000, 'm'),
])
def test_boundaries(number, expected):
    """Verify the minimum and maximum constraints."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (4, 'iv'),
    (9, 'ix'),
    (40, 'xl'),
    (90, 'xc'),
    (400, 'cd'),
    (900, 'cm'),
])
def test_subtractive_cases(number, expected):
    """Verify cases where subtractive notation is required."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (3, 'iii'),
    (8, 'viii'),
    (30, 'xxx'),
    (80, 'lxxx'),
    (300, 'ccc'),
    (800, 'dccc'),
])
def test_additive_cases(number, expected):
    """Verify cases where additive repetition is required."""
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
def test_single_digits(number, expected):
    """Verify all single digit conversions."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (10, 'x'),
    (50, 'l'),
    (100, 'c'),
    (500, 'd'),
])
def test_round_numbers(number, expected):
    """Verify standard Roman numeral base values."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (388, 'ccclxxxviii'),
    (444, 'cdxliv'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
    (763, 'dlxiii'),
])
def test_complex_combinations(number, expected):
    """Verify complex numbers that combine multiple Roman numeral rules."""
    assert int_to_mini_roman(number) == expected