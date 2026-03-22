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
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(42) == 'xlii'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(501) == 'di'

def test_int_to_mini_roman_complex_cases():
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(278) == 'ccclxxviii'
    assert int_to_mini_roman(799) == 'ccmlxxxix'
    assert int_to_mini_roman(999) == 'cmxcix'

# Focus: Type Scenarios
def test_type_scenario_positive_integer():
    assert isinstance(int_to_mini_roman(19), str)

def test_type_scenario_edge_case_one():
    assert isinstance(int_to_mini_roman(1), str)

def test_type_scenario_edge_case_thousand():
    assert isinstance(int_to_mini_roman(1000), str)