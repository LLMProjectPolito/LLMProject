
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

# The function int_to_mini_roman is assumed to be imported or defined in the environment.

@pytest.mark.parametrize("number, expected", [
    (1, "i"),
    (1000, "m"),
])
def test_boundary_values(number, expected):
    """Test the minimum and maximum allowed boundaries."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (19, "xix"),
    (152, "clii"),
    (426, "cdxxvi"),
])
def test_provided_examples(number, expected):
    """Test the examples provided in the problem description."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (4, "iv"),
    (9, "ix"),
    (40, "xl"),
    (90, "xc"),
    (400, "cd"),
    (900, "cm"),
])
def test_subtractive_notation(number, expected):
    """Test the subtractive rules which are common failure points in Roman numeral logic."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (3, "iii"),
    (30, "xxx"),
    (300, "ccc"),
    (333, "cccxxxiii"),
])
def test_repetition_limits(number, expected):
    """Test that the function handles the maximum allowed consecutive characters correctly."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (8, "viii"),
    (44, "xliv"),
    (88, "lxxxviii"),
    (388, "ccclxxxviii"),
    (888, "dccclxxxviii"),
    (999, "cmxcix"),
])
def test_complex_combinations(number, expected):
    """Test complex numbers that require multiple different Roman numeral rules."""
    assert int_to_mini_roman(number) == expected

def test_lowercase_requirement():
    """
    A broad check to ensure that for a variety of numbers, 
    the output is always lowercase.
    """
    test_numbers = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 44, 99, 444, 999]
    for n in test_numbers:
        result = int_to_mini_roman(n)
        assert result == result.lower(), f"Expected lowercase for {n}, but got {result}"
        assert result.isupper() is False, f"Result for {n} should not be uppercase"

@pytest.mark.parametrize("number, expected", [
    (2, "ii"),
    (5, "v"),
    (10, "x"),
    (50, "l"),
    (100, "c"),
    (500, "d"),
])
def test_single_symbol_values(number, expected):
    """Test basic single-character Roman numeral mappings."""
    assert int_to_mini_roman(number) == expected