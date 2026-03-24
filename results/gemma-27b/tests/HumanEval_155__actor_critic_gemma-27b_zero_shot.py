
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
        even_odd_count(12) ==> (1, 1)  # Sign is disregarded
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))  # Handle negative numbers
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd():
    assert even_odd_count(1357) == (0, 4)

def test_single_even():
    assert even_odd_count(2) == (1, 0)

def test_single_odd():
    assert even_odd_count(1) == (0, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_mixed():
    assert even_odd_count(1234567890) == (5, 5)

def test_large_number():
    assert even_odd_count(12345678901234567890) == (10, 10)

def test_large_number_with_zeros():
    assert even_odd_count(1000000000) == (9, 1)

def test_trailing_zeros():
    assert even_odd_count(120) == (2, 1)