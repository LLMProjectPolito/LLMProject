import pytest

def test_even_odd_count_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_single_digit_even_number():
    assert even_odd_count(4) == (1, 0)

def test_even_odd_count_single_digit_odd_number():
    assert even_odd_count(3) == (0, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_large_number():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_negative_large_number():
    assert even_odd_count(-123456) == (3, 3)

def test_even_odd_count_all_even():
    assert even_odd_count(24680) == (5, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)