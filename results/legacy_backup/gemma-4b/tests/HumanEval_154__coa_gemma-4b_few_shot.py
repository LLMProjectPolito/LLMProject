import pytest
import math


# Focus: Boundary Values
def test_cycpattern_check_basic_true():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("whassup","psus") == False

# Focus: Type Scenarios
def test_cycpattern_check_basic_true():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("whassup","psus") == False

# Focus: Logic Branches
def test_cycpattern_check_basic_true():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("whassup","psus") == False