
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

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_number_with_leading_zeroes():
    assert even_odd_count(102) == (2, 1)

def test_number_with_multiple_zeroes():
    assert even_odd_count(10020) == (3, 1)

def test_negative_number_with_zeroes():
    assert even_odd_count(-1020) == (2, 2)

def test_negative_mixed_digits():
    assert even_odd_count(-1234) == (2, 2)

def test_number_with_leading_zero():
    assert even_odd_count(102) == (2, 1)

def test_negative_number_with_leading_zero():
    assert even_odd_count(-102) == (2, 1)

def test_number_with_multiple_zeros():
    assert even_odd_count(1002) == (2, 1)

def test_negative_number_with_multiple_zeros():
    assert even_odd_count(-1002) == (2, 1)

def test_max_int():
    assert even_odd_count(2147483647) == (4, 5)

def test_min_int():
    assert even_odd_count(-2147483648) == (1, 7)

def test_number_with_repeated_digits():
    assert even_odd_count(2222) == (4, 0)

def test_number_with_repeated_odd_digits():
    assert even_odd_count(1111) == (0, 4)

def test_number_with_mixed_repeated_digits():
    assert even_odd_count(1212) == (2, 2)

def test_negative_number_with_mixed_repeated_digits():
    assert even_odd_count(-1212) == (2, 2)