
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_even_odd_count_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(1357) == (0, 4)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_mixed_positive():
    assert even_odd_count(21436587) == (4, 4)

def test_even_odd_count_mixed_negative():
    assert even_odd_count(-21436587) == (4, 4)

def test_even_odd_count_with_leading_zero():
    assert even_odd_count(102) == (2, 1)

def test_even_odd_count_negative_with_leading_zero():
    assert even_odd_count(-102) == (2, 1)