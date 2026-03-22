import pytest
import math

def test_cycpattern_check_basic():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("any", "") == False

def test_cycpattern_check_wrong_type():
    assert cycpattern_check(123, "abc") is None