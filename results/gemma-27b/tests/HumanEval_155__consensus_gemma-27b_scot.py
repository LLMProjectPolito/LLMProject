
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

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_mixed_digits():
    assert even_odd_count(21436587) == (4, 4)

def test_positive_number():
    assert even_odd_count(123456) == (3, 3)

def test_negative_number():
    assert even_odd_count(-123456) == (3, 3)

def test_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_mixed_digits():
    assert even_odd_count(12) == (1, 1)

def test_negative_with_zero():
    assert even_odd_count(-120) == (2, 1)

def test_positive_with_zero():
    assert even_odd_count(120) == (2, 1)

def test_negative_all_odd():
    assert even_odd_count(-13579) == (0, 5)

def test_negative_all_even():
    assert even_odd_count(-2468) == (4, 0)

def test_number_with_leading_zeroes_string():
    assert even_odd_count(0012) == (1, 1)

def test_number_with_leading_zeroes():
    assert even_odd_count(00012) == (1, 1)

def test_even_odd_count_positive_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_positive_odd():
    assert even_odd_count(1357) == (0, 4)

def test_even_odd_count_mixed():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative_even():
    assert even_odd_count(-246) == (3, 0)

def test_even_odd_count_negative_odd():
    assert even_odd_count(-135) == (0, 3)

def test_even_odd_count_negative_mixed():
    assert even_odd_count(-1234) == (2, 2)

def test_even_odd_count_with_leading_zeroes():
    assert even_odd_count(102) == (2, 1)

def test_even_odd_count_negative_with_leading_zeroes():
    assert even_odd_count(-102) == (2, 1)

def test_even_odd_count_all_zeroes():
    assert even_odd_count(000) == (3, 0)

def test_even_odd_count_negative_all_zeroes():
    assert even_odd_count(-000) == (3, 0)