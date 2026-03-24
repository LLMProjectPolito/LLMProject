
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
from your_module import int_to_mini_roman  # Replace your_module

# Test Suite for int_to_mini_roman

def test_valid_input_range():
    """Tests that the function handles numbers within the specified range (1-1000) correctly."""
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(1000) == "m"

def test_basic_roman_conversions():
    """Tests basic Roman numeral conversions."""
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"

def test_complex_roman_conversions():
    """Tests more complex Roman numeral conversions."""
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(789) == "dccmlxxxix"
    assert int_to_mini_roman(944) == "cmlxxxiiii"
    assert int_to_mini_roman(399) == "cccxcix"

def test_edge_cases():
    """Tests edge cases and boundary conditions."""
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(8) == "viii"
    assert int_to_mini_roman(1000) == "m"

def test_numbers_with_repeated_symbols():
    """Tests numbers that require repeated Roman symbols."""
    assert int_to_mini_roman(22) == "xxii"
    assert int_to_mini_roman(88) == "lxxxviii"
    assert int_to_mini_roman(444) == "cdxliv"

def test_numbers_with_subtractive_notation():
    """Tests numbers that use subtractive notation (IV, IX, XL, XC, CD, CM)."""
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(14) == "xiv"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(44) == "xliv"
    assert int_to_mini_roman(49) == "xlix"

def test_large_numbers_within_range():
    """Tests numbers close to the upper limit of the range."""
    assert int_to_mini_roman(999) == "cmxcix"
    assert int_to_mini_roman(1000) == "m"

def test_invalid_input_less_than_one():
    """Tests input less than 1.  Should raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_invalid_input_greater_than_one_thousand():
    """Tests input greater than 1000. Should raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)