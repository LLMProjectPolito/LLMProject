import pytest
from your_module import even_odd_count  # Replace your_module

def test_positive_integer():
    assert even_odd_count(123456) == (3, 3)

def test_negative_integer():
    assert even_odd_count(-12) == (1, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_mixed_digits():
    assert even_odd_count(12345) == (2, 3)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-9876543210) == (5, 5)

def test_number_with_repeating_digits():
    assert even_odd_count(2222) == (4, 0)
    assert even_odd_count(1111) == (0, 4)
    assert even_odd_count(1212) == (2, 2)

def test_number_with_leading_zeros_treated_as_digits():
    assert even_odd_count(10203) == (2, 2)

def test_edge_case_single_digit_even():
    assert even_odd_count(8) == (1, 0)

def test_edge_case_single_digit_odd():
    assert even_odd_count(7) == (0, 1)