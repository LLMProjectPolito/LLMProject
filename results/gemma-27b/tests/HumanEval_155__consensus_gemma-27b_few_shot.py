
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_all_even():
    assert even_odd_count(246) == (3, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(135) == (0, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_single_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_mixed_length():
    assert even_odd_count(21) == (1, 1)
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(214) == (2, 1)
    assert even_odd_count(1234) == (2, 2)

def test_positive_number():
    assert even_odd_count(123456) == (3, 3)

def test_negative_number():
    assert even_odd_count(-123456) == (3, 3)

def test_number_with_leading_zeros_as_string():
    assert even_odd_count(100) == (2, 1)

def test_number_with_trailing_zeros():
    assert even_odd_count(120) == (2, 1)

def test_number_with_multiple_zeros():
    assert even_odd_count(102030) == (3, 3)

def test_number_with_leading_zeroes_string():
    assert even_odd_count(0012) == (1, 1)

def test_number_with_leading_zeroes_int():
    assert even_odd_count(1200) == (2, 2)

def test_negative_number_with_leading_zeroes_string():
    assert even_odd_count(-0012) == (1, 1)

def test_negative_number_with_leading_zeroes_int():
    assert even_odd_count(-1200) == (2, 2)