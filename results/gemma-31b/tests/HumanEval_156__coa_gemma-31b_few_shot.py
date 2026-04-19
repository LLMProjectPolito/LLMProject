
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
import pytest

def test_int_to_mini_roman_lower_boundary():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'

def test_int_to_mini_roman_upper_boundary():
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(999) == 'cmxcix'

# Focus: Logic Branches
import pytest

def test_subtractive_logic_branches():
    """Tests the logic branches for subtractive Roman numeral notation (4s and 9s)."""
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(999) == 'cmxcix'

def test_additive_logic_branches():
    """Tests the logic branches for standard additive Roman numeral notation."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(888) == 'dccclxxxviii'

def test_boundary_logic_branches():
    """Tests the logic branches for the minimum and maximum constraints."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

# Focus: Type Scenarios
import pytest

def test_int_to_mini_roman_output_type():
    """Verify that the function returns a string for a valid integer input."""
    assert isinstance(int_to_mini_roman(10), str)

def test_int_to_mini_roman_float_input():
    """Verify that passing a float instead of an integer raises a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(10.5)

def test_int_to_mini_roman_string_input():
    """Verify that passing a string instead of an integer raises a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman("10")