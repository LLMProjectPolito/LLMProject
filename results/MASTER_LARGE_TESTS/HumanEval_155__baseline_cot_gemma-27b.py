import pytest

def test_positive_number():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-246) == (3, 0)
    assert even_odd_count(-135) == (0, 3)
    assert even_odd_count(-1234567890) == (5, 5)

def test_zero():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)

def test_single_digit():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(3) == (0, 1)

def test_all_even():
    assert even_odd_count(2222) == (4, 0)

def test_all_odd():
    assert even_odd_count(1111) == (0, 4)

def test_large_number():
    assert even_odd_count(12345678901234567890) == (10, 10)

def test_leading_zeros():
    assert even_odd_count(102) == (2, 1)
    assert even_odd_count(-002) == (1, 1)

def test_boundary_conditions():
    assert even_odd_count(2147483647) == (5, 5)  # Max 32-bit integer
    assert even_odd_count(-2147483648) == (5, 5) # Min 32-bit integer