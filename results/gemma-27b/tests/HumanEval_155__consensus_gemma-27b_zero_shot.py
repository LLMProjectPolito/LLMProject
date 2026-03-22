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

def test_number_with_leading_zeroes_string():
    assert even_odd_count(0012) == (1, 1)

def test_number_with_leading_zeroes_int():
    assert even_odd_count(1200) == (2, 2)

def test_number_with_leading_zeros_as_string():
    assert even_odd_count(0022) == (2, 0)

def test_number_with_leading_zeros_and_odd():
    assert even_odd_count(0011) == (0, 2)

def test_number_with_leading_zeros_mixed():
    assert even_odd_count(0012) == (1, 1)

def test_negative_number_with_leading_zeroes_string():
    assert even_odd_count(-0012) == (1, 1)

def test_negative_number_with_leading_zeroes_int():
    assert even_odd_count(-1200) == (2, 2)