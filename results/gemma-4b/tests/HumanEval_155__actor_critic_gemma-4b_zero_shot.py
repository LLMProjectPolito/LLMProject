
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
    num = abs(num)
    if num == 0:
        return (1, 0)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return (even_count, odd_count)

def test_positive_even():
    assert even_odd_count(12) == (1, 1)

def test_positive_odd():
    assert even_odd_count(123) == (1, 2)

def test_negative_even():
    assert even_odd_count(-12) == (1, 1)

def test_negative_odd():
    assert even_odd_count(-123) == (1, 2)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_large_number_even():
    assert even_odd_count(1234567890) == (5, 5)

def test_large_number_odd():
    assert even_odd_count(12345678901) == (5, 5)

def test_negative_large_number_even():
    assert even_odd_count(-1234567890) == (5, 5)

def test_negative_large_number_odd():
    assert even_odd_count(-12345678901) == (5, 5)

def test_mixed_digits():
    assert even_odd_count(2143567890) == (5, 5)

def test_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd():
    assert even_odd_count(13579) == (0, 5)