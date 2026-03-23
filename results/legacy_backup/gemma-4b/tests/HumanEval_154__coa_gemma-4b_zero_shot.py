import pytest
import math


# Focus: Boundary Values
import pytest

def test_cycpattern_check_boundary_low():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_boundary_high():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_boundary_edge():
    assert cycpattern_check("abab","baa") == True

# Focus: Type Scenarios
def test_type_scenario_1():
    assert cycpattern_check("abcd","abd") == False

def test_type_scenario_2():
    assert cycpattern_check("hello","ell") == True

def test_type_scenario_3():
    assert cycpattern_check("whassup","psus") == False

# Focus: Logic Branches
import pytest

def test_cycpattern_check_substring_present():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char_match():
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True