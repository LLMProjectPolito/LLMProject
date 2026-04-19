
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

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(-1) == (0, 1)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

# Focus: Type Scenarios
import pytest

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(246) == (3, 0)
    assert even_odd_count(135) == (0, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-1357) == (0, 4)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

# Focus: Sign Handling
def test_even_odd_count_negative_mixed():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_negative_even():
    assert even_odd_count(-246) == (3, 0)

def test_even_odd_count_negative_odd():
    assert even_odd_count(-135) == (0, 3)