
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_even_odd_count_positive_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_positive_odd():
    assert even_odd_count(1357) == (0, 4)

def test_even_odd_count_mixed():
    assert even_odd_count(1234) == (2, 2)

def test_even_odd_count_single_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_negative_even():
    assert even_odd_count(-24) == (2, 0)

def test_even_odd_count_negative_odd():
    assert even_odd_count(-13) == (0, 2)

def test_even_odd_count_negative_mixed():
    assert even_odd_count(-123) == (1, 2)

def test_even_odd_count_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_large_negative_number():
    assert even_odd_count(-9876543210) == (5, 5)

def test_even_odd_count_repeated_digits():
    assert even_odd_count(2222) == (4, 0)

def test_even_odd_count_repeated_odd_digits():
    assert even_odd_count(1111) == (0, 4)

def test_even_odd_count_edge_case():
    assert even_odd_count(10) == (1, 1)

def test_even_odd_count_another_edge_case():
    assert even_odd_count(-10) == (1, 1)