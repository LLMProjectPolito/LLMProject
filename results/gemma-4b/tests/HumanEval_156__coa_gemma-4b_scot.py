
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

def test_int_to_mini_roman_boundary_low():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_boundary_high():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_boundary_mid():
    assert int_to_mini_roman(500) == 'd'

# Focus: Type Scenarios
import pytest

def test_type_scenario_single_digit():
    assert int_to_mini_roman(1) == 'i'

def test_type_scenario_two_digit_small():
    assert int_to_mini_roman(10) == 'x'

def test_type_scenario_two_digit_large():
    assert int_to_mini_roman(19) == 'xix'

# Focus: Logic Branches
import pytest

def test_int_to_mini_roman_1():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_2():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(426) == 'cdxxvi'