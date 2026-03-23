import pytest

def test_even_odd_count_negative_number_with_zeros():
    # Digits: 1,0,0,2,0,0,3 -> evens: 0,0,2,0,0 (5), odds: 1,3 (2)
    assert even_odd_count(-1002003) == (5, 2)

def test_even_odd_count_zero():
    # Edge case: the number 0 should be counted as one even digit and no odd digits.
    assert even_odd_count(0) == (1, 0)