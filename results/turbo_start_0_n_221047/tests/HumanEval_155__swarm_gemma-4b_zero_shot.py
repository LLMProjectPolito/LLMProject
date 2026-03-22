import pytest
import math

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

def test_zero_as_input():
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

def test_mixed_negative():
    assert even_odd_count(-12345) == (2, 3)