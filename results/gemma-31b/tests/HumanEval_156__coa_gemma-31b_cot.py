
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
def test_int_to_mini_roman_lower_boundary():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_upper_boundary():
    assert int_to_mini_roman(1000) == 'm'

# Focus: Logic Branches
import pytest

def test_subtractive_logic_branches():
    """Tests the logic branches for subtractive Roman numeral combinations (4s and 9s)."""
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_additive_logic_branches():
    """Tests the logic branches for standard additive Roman numeral combinations."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'

def test_boundary_and_mixed_branches():
    """Tests the upper boundary and complex combinations of additive/subtractive logic."""
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(999) == 'cmxcix'

# Focus: Type Scenarios
import pytest

def test_int_to_mini_roman_return_type():
    """Verify that the function returns a string."""
    assert isinstance(int_to_mini_roman(1), str)

def test_int_to_mini_roman_invalid_type_float():
    """Verify that providing a float raises a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(10.5)

def test_int_to_mini_roman_invalid_type_string():
    """Verify that providing a string raises a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman("10")