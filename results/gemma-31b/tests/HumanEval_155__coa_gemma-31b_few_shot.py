
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
import math


# Focus: Boundary Values
def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digits():
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_negative_boundaries():
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-2) == (1, 0)

# Focus: Negative Values
def test_even_odd_count_negative_mixed():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-123) == (1, 2)

def test_even_odd_count_negative_all_even():
    assert even_odd_count(-2468) == (4, 0)

def test_even_odd_count_negative_all_odd():
    assert even_odd_count(-1357) == (0, 4)

# Focus: Type Scenarios
def test_even_odd_count_positive():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-2468) == (4, 0)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)