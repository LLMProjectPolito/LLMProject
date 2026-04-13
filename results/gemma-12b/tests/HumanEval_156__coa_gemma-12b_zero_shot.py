
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
def test_boundary_1():
    assert int_to_mini_roman(1) == 'i'

def test_boundary_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_boundary_500():
    assert int_to_mini_roman(500) == 'd'

# Focus: Logic Branches
def test_int_to_mini_roman_positive_number():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(41) == 'xli'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(45) == 'xlv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(91) == 'xci'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(95) == 'xcv'
    assert int_to_mini_roman(99) == 'xciii'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(101) == 'ci'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(150) == 'cl'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(199) == 'cxcix'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(499) == 'cdxcix'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(949) == 'cmxlix'
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_complex_cases():
    assert int_to_mini_roman(388) == 'cccxxxviii'
    assert int_to_mini_roman(747) == 'dccxlvii'
    assert int_to_mini_roman(864) == 'dccclxiv'
    assert int_to_mini_roman(973) == 'cmxlxxiii'

# Focus: Type Scenarios
def test_type_scenario_valid_integer():
    assert isinstance(int_to_mini_roman(19), str)

def test_type_scenario_valid_integer_large():
    assert isinstance(int_to_mini_roman(999), str)

def test_type_scenario_invalid_input_not_integer():
    try:
        int_to_mini_roman("abc")
    except TypeError:
        assert True
    else:
        assert False