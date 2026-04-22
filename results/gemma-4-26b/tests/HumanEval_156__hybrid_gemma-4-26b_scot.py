
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

@pytest.mark.parametrize("input_val, expected", [
    (1, "i"),
    (1000, "m"),
])
def test_boundaries(input_val, expected):
    """Test the minimum and maximum allowed values."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (5, "v"),
    (10, "x"),
    (50, "l"),
    (100, "c"),
    (500, "d"),
])
def test_base_symbols(input_val, expected):
    """Test the primary additive symbols."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (4, "iv"),
    (9, "ix"),
    (40, "xl"),
    (90, "xc"),
    (400, "cd"),
    (900, "cm"),
])
def test_subtractive_logic(input_val, expected):
    """Test the specific subtractive logic (e.g., IV, XC, CM)."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (2, "ii"),
    (3, "iii"),
    (8, "viii"),
    (30, "xxx"),
    (80, "lxxx"),
    (300, "ccc"),
    (800, "dccc"),
])
def test_additive_logic(input_val, expected):
    """Test the repetition/additive logic (e.g., III, LXXX)."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    # Docstring & Provided Examples
    (19, "xix"),
    (152, "clii"),
    (426, "cdxxvi"),
    # Complex combinations from both suites
    (38, "xxxviii"),
    (44, "xliv"),
    (88, "lxxxviii"),
    (99, "xcix"),
    (388, "ccclxxxviii"),
    (444, "cdxliv"),
    (654, "dcliv"),
    (777, "dccxxvii"),
    (888, "dccclxxxviii"),
    (944, "cmxliv"),
    (999, "cmxcix"),
])
def test_complex_combinations(input_val, expected):
    """Test complex numbers combining multiple rules and symbols."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val", [1, 10, 100, 500, 1000])
def test_lowercase_invariant(input_val):
    """
    Ensures that the output is always lowercase, 
    maintaining the 'mini' Roman numeral requirement.
    """
    result = int_to_mini_roman(input_val)
    assert result == result.lower(), f"Output for {input_val} was not lowercase: {result}"