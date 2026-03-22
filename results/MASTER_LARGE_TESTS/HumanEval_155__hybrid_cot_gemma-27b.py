import pytest

def test_positive_number():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(12345) == (2, 3)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-246) == (3, 0)
    assert even_odd_count(-135) == (0, 3)
    assert even_odd_count(-1234567890) == (5, 5)
    assert even_odd_count(-12345) == (2, 3)
    assert even_odd_count(-102) == (2, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)

def test_single_digit():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(1) == (0, 1)

def test_large_number():
    assert even_odd_count(1234567890123456) == (8, 8)
    assert even_odd_count(2468024680) == (10, 0)
    assert even_odd_count(1234567890) == (5, 5)

def test_leading_zeros():
    assert even_odd_count(102) == (2, 1)
    assert even_odd_count(012) == (2, 1)  # Python interprets 012 as 12 (octal literal)

def test_mixed_digits():
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(24680) == (5, 0)
    assert even_odd_count(1234) == (2, 2)

def test_non_integer_input():
    with pytest.raises(TypeError):
        even_odd_count(12.34)
    with pytest.raises(TypeError):
        even_odd_count("123")

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)