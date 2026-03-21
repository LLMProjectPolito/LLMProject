import pytest

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-246) == (3, 0)
    assert even_odd_count(-135) == (0, 3)
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)

def test_even_odd_count_single_digit():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(3) == (0, 1)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(-9876543210) == (5, 5)

def test_even_odd_count_leading_zeros():
    assert even_odd_count(102) == (2, 1)
    assert even_odd_count(-204) == (2, 1)

def test_even_odd_count_boundary_conditions():
    assert even_odd_count(2147483647) == (5, 5)  # Max 32-bit integer
    assert even_odd_count(-2147483648) == (5, 5) # Min 32-bit integer