
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
    (2, "ii"),
    (3, "iii"),
    (4, "iv"),
    (5, "v"),
    (9, "ix"),
    (10, "x"),
    (40, "xl"),
    (50, "l"),
    (90, "xc"),
    (100, "c"),
    (400, "cd"),
    (500, "d"),
    (900, "cm"),
    (1000, "m"),
])
def test_roman_base_units_and_subtractions(input_val, expected):
    """Test all fundamental Roman numeral building blocks and subtractive pairs."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (19, "xix"),
    (152, "clii"),
    (426, "cdxxvi"),
])
def test_docstring_examples(input_val, expected):
    """Verify the specific examples provided in the problem description."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (3, "iii"),
    (30, "xxx"),
    (300, "ccc"),
    (8, "viii"),
    (38, "xxxviii"),
    (88, "lxxxviii"),
    (388, "ccclxxxviii"),
    (888, "dccclxxxviii"),
])
def test_repetition_and_addition(input_val, expected):
    """Test cases involving multiple repetitions of the same numeral."""
    assert int_to_mini_roman(input_val) == expected

def test_case_sensitivity():
    """Ensure the output is strictly lowercase as per requirements."""
    # Even if the logic produces 'XIX', the requirement is 'xix'
    result = int_to_mini_roman(19)
    assert result == result.lower()
    assert result != result.upper()

@pytest.mark.parametrize("input_val, expected", [
    (99, "xcix"),
    (444, "cdxliv"),
    (999, "cmxcix"),
    (555, "dlv"),
    (666, "dvi"),
    (789, "dccclxxxix"),
])
def test_complex_combinations(input_val, expected):
    """Test complex numbers that mix subtraction and addition across multiple magnitudes."""
    assert int_to_mini_roman(input_val) == expected

def test_boundary_limits():
    """Explicitly test the absolute boundaries of the allowed range."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'