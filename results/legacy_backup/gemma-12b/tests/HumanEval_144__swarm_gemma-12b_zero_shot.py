import pytest
import math

def test_simplify_large_numbers_1():
    assert simplify("1000000/1", "1000000/1") == True

def test_simplify_large_numbers_2():
    assert simplify("1000000/1", "1/1000000") == True