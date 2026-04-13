
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
import math

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_zero_input():
    assert even_odd_count(0) == (1, 0)

def test_positive_even():
    assert even_odd_count(2468) == (4, 0)

def test_positive_odd():
    assert even_odd_count(13579) == (0, 5)

def test_negative_even():
    assert even_odd_count(-2468) == (4, 0)

def test_negative_odd():
    assert even_odd_count(-13579) == (0, 5)

def test_mixed_positive():
    assert even_odd_count(12345) == (2, 3)