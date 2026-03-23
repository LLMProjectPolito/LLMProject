import pytest
import math

def test_basic():
    assert cycpattern_check("hello","ell") == True

def test_empty_input():
    assert cycpattern_check("", "") == True

def test_empty_strings():
    assert cycpattern_check("", "") == True