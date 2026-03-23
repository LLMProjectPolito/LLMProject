import pytest
import math


# Focus: Boundary Values
import pytest

def test_int_to_mini_roman_lower_boundary():
    assert int_to_mini_roman(1) == "i"

def test_int_to_mini_roman_upper_boundary():
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_boundary_near_upper():
    assert int_to_mini_roman(999) == "cmxciii"

# Focus: Logic Branches
def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_subtractive_cases():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_mixed_cases():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(789) == 'dccxcix'
    assert int_to_mini_roman(999) == 'cmxciX'

# Focus: Type Scenarios
def test_int_to_mini_roman_valid_input():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(999) == "cmxciii"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(399) == "cccxcix"
    assert int_to_mini_roman(500) == "d"

def test_int_to_mini_roman_type_scenarios():
    assert isinstance(int_to_mini_roman(10), str)
    assert isinstance(int_to_mini_roman(500), str)
    assert isinstance(int_to_mini_roman(999), str)
    assert len(int_to_mini_roman(100)) > 0