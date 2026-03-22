import pytest
import math


# Focus: Boundary Values
def test_int_to_mini_roman_boundary_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_boundary_9():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_boundary_10():
    assert int_to_mini_roman(10) == 'x'

# Focus: Type Scenarios
def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

# Focus: Logic Branches
def test_int_to_mini_roman_1():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_2():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(426) == 'cdxxvi'