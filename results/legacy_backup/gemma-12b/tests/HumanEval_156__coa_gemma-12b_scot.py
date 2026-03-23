import pytest
import math


# Focus: Boundary Values
def test_boundary_minimum():
    assert int_to_mini_roman(1) == "i"

def test_boundary_maximum():
    assert int_to_mini_roman(1000) == "m"

def test_boundary_just_above_lower_bound():
    assert int_to_mini_roman(2) == "ii"

# Focus: Logic Branches
def test_int_to_mini_roman_branch_1_less_than_10():
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(1) == "i"

def test_int_to_mini_roman_branch_2_between_10_and_50():
    assert int_to_mini_roman(11) == "xi"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(35) == "xxxv"
    assert int_to_mini_roman(49) == "xlix"

def test_int_to_mini_roman_branch_3_between_50_and_100():
    assert int_to_mini_roman(51) == "li"
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(79) == "lxxix"
    assert int_to_mini_roman(90) == "xc"

# Focus: Type Scenarios
def test_int_to_mini_roman_valid_range():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(14) == "xiv"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(999) == "cmxciii"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(6) == "vi"
    assert int_to_mini_roman(7) == "vii"
    assert int_to_mini_roman(8) == "viii"
    assert int_to_mini_roman(9) == "ix"

def test_int_to_mini_roman_complex_cases():
    assert int_to_mini_roman(147) == "cxlvii"
    assert int_to_mini_roman(388) == "cccxxxviii"
    assert int_to_mini_roman(499) == "cdxcix"
    assert int_to_mini_roman(744) == "dccxliv"
    assert int_to_mini_roman(949) == "cmxlix"
    assert int_to_mini_roman(999) == "cmxciii"