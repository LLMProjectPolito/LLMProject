import pytest
import math

def test_cycpattern_check_positive():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abcd", "") == True

def test_cycpattern_check_long_b():
    assert cycpattern_check("hello", "helloworld") == False