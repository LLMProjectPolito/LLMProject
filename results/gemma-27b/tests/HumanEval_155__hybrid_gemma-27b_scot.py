
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

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

def test_positive_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_positive_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_positive_mixed_digits():
    assert even_odd_count(123456) == (3, 3)

def test_negative_even_digits():
    assert even_odd_count(-2468) == (4, 0)

def test_negative_odd_digits():
    assert even_odd_count(-13579) == (0, 5)

def test_negative_mixed_digits():
    assert even_odd_count(-123456) == (3, 3)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-9876543210) == (5, 5)