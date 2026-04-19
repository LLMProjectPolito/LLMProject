
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

def test_int_to_mini_roman_near_boundaries():
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(999) == 'cmxcix'

# Focus: Logic Branches
import pytest

def test_int_to_mini_roman_subtractive_branches():
    """Tests the logic branches for subtractive notation (4s and 9s)."""
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_additive_and_boundary_branches():
    """Tests the logic branches for simple additive values and boundary limits."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_mixed_logic_branches():
    """Tests complex numbers that trigger multiple additive and subtractive branches."""
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(388) == 'ccclxxxviii'

# Focus: Type Scenarios
import pytest

def test_int_to_mini_roman_float_type():
    with pytest.raises(TypeError):
        int_to_mini_roman(10.5)

def test_int_to_mini_roman_string_type():
    with pytest.raises(TypeError):
        int_to_mini_roman("10")

def test_int_to_mini_roman_none_type():
    with pytest.raises(TypeError):
        int_to_mini_roman(None)