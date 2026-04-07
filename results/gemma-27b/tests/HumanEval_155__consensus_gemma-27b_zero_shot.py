
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_positive_number():
    assert even_odd_count(123456) == (3, 3)

def test_negative_number():
    assert even_odd_count(-123456) == (3, 3)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_mixed_digits():
    assert even_odd_count(12) == (1, 1)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_negative_single_even():
    assert even_odd_count(-2) == (1, 0)

def test_negative_single_odd():
    assert even_odd_count(-1) == (0, 1)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_number_with_leading_zeros_as_string():
    assert even_odd_count(100) == (2, 1)

def test_number_with_trailing_zeros():
    assert even_odd_count(120) == (2, 1)

def test_number_with_multiple_zeros():
    assert even_odd_count(102030) == (3, 3)

def test_number_with_leading_zeros():
    assert even_odd_count(0011) == (0, 2)

def test_number_with_mixed_leading_zeros():
    assert even_odd_count(0123) == (1, 2)

def test_negative_number_with_leading_zero():
    assert even_odd_count(-102) == (2, 1)

def test_number_with_multiple_zeros_2():
    assert even_odd_count(1002) == (2, 1)

def test_negative_number_with_multiple_zeros():
    assert even_odd_count(-1002) == (2, 1)