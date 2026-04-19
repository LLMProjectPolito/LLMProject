
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

# The function int_to_mini_roman is assumed to be available in the environment.

@pytest.mark.parametrize("number, expected", [
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
])
def test_provided_examples(number, expected):
    """Validate the examples provided in the problem description and docstrings."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (1000, 'm'),
])
def test_boundaries(number, expected):
    """Verify the lower and upper boundaries of the restricted range [1, 1000]."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (5, 'v'),
    (10, 'x'),
    (50, 'l'),
    (100, 'c'),
    (500, 'd'),
    (1000, 'm'),
])
def test_single_symbols(number, expected):
    """Verify numbers that map to a single Roman numeral character."""
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
    """Verify the subtractive notation rules for 4s and 9s across all scales."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (2, 'ii'),
    (3, 'iii'),
    (30, 'xxx'),
    (300, 'ccc'),
    (8, 'viii'),
    (80, 'lxxx'),
    (800, 'dccc'),
])
def test_repetitive_additive(number, expected):
    """Verify cases where symbols are repeated (additive notation)."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (38, 'xxxviii'),
    (76, 'lxxvi'),
    (99, 'xcix'),
    (444, 'cdxliv'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_complex_combinations(number, expected):
    """Verify complex combinations of additive and subtractive numerals."""
    assert int_to_mini_roman(number) == expected

def test_output_format_and_type():
    """Ensure the function returns a lowercase string for various inputs."""
    test_values = [1, 4, 9, 49, 99, 444, 888, 999, 1000]
    for val in test_values:
        result = int_to_mini_roman(val)
        
        # Type check
        assert isinstance(result, str), f"Output for {val} should be a string, got {type(result)}"
        
        # Case check
        assert result == result.lower(), f"Output for {val} is not lowercase: {result}"
        assert not any(char.isupper() for char in result), f"Output for {val} contains uppercase characters: {result}"