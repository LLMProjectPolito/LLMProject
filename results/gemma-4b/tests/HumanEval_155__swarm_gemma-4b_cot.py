
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
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_negative_number_with_even_and_odd():
    assert even_odd_count(-12) == (1, 1)

def test_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_positive_number_with_even_and_odd():
    assert even_odd_count(123) == (1, 2)

def test_positive_zero():
    assert even_odd_count(0) == (1, 0)

def test_large_negative_number():
    assert even_odd_count(-123456789) == (4, 5)

def test_large_positive_number():
    assert even_odd_count(123456789) == (5, 4)