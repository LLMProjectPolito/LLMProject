
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
def test_provided_examples(number, expected):
    """Tests the examples provided in the docstring."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (1000, 'm'),
])
def test_boundary_values(number, expected):
    """Tests the minimum and maximum allowed values."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (4, 'iv'),
    (9, 'ix'),
    (40, 'xl'),
    (90, 'xc'),
    (400, 'cd'),
    (900, 'cm'),
])
def test_subtractive_notation(number, expected):
    """Tests the specific cases where subtractive notation is used."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (3, 'iii'),
    (8, 'viii'),
    (13, 'xiii'),
    (38, 'xxxviii'),
    (88, 'lxxxviii'),
    (388, 'ccclxxxviii'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_complex_combinations(number, expected):
    """Tests various combinations of Roman numeral symbols."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (5, 'v'),
    (10, 'x'),
    (50, 'l'),
    (100, 'c'),
    (500, 'd'),
])
def test_base_symbols(number, expected):
    """Tests the primary Roman numeral symbols."""
    assert int_to_mini_roman(number) == expected

def test_output_format():
    """Ensures the output is always lowercase and contains only valid characters."""
    valid_chars = set("ivxlcdm")
    for i in range(1, 1001):
        result = int_to_mini_roman(i)
        assert isinstance(result, str)
        assert result == result.lower(), f"Value {i} produced uppercase: {result}"
        assert all(char in valid_chars for char in result), f"Value {i} produced invalid chars: {result}"