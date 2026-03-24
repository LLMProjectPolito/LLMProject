
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
import math

def test_even_odd_count_positive():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_wrong_type():
    """Test with a string input."""
    try:
        even_odd_count("abc")
    except TypeError:
        assert True
    else:
        assert False