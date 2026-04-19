
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
import math


# Focus: Boundary Values
def test_int_to_mini_roman_min_boundary():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_max_boundary():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_near_max_boundary():
    assert int_to_mini_roman(999) == 'cmxcix'

# Focus: Type Scenarios
import pytest

def test_int_to_mini_roman_return_type():
    """Verify that the function returns a string for a valid integer input."""
    assert isinstance(int_to_mini_roman(10), str)

def test_int_to_mini_roman_float_input():
    """Verify that providing a float instead of an integer raises a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(10.5)

def test_int_to_mini_roman_string_input():
    """Verify that providing a string instead of an integer raises a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman("10")

# Focus: Logic Branches
import pytest

@pytest.mark.parametrize("number, expected", [
    (4, 'iv'), (9, 'ix'), (40, 'xl'), (90, 'xc'), (400, 'cd'), (900, 'cm')
])
def test_subtractive_logic_branches(number, expected):
    """Tests the logic branches specifically handling subtractive Roman numeral notation."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (1, 'i'), (5, 'v'), (10, 'x'), (50, 'l'), (100, 'c'), (500, 'd'), (1000, 'm')
])
def test_additive_logic_branches(number, expected):
    """Tests the logic branches handling standard additive Roman numeral notation."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (444, 'cdxliv'), (999, 'cmxcix'), (888, 'dlxxxviii')
])
def test_complex_mixed_logic_branches(number, expected):
    """Tests logic branches where multiple additive and subtractive rules are combined."""
    assert int_to_mini_roman(number) == expected