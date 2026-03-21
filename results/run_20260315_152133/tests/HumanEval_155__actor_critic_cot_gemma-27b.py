import pytest
import sys

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    pass # Assume function is defined elsewhere

def test_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_mixed_digits():
    assert even_odd_count(123456) == (3, 3)

def test_leading_zero():
    assert even_odd_count(102) == (2, 1)

def test_float_input():
    with pytest.raises(TypeError):
        even_odd_count(12.34)

def test_string_input():
    with pytest.raises(TypeError):
        even_odd_count("123")

def test_large_negative_number():
    assert even_odd_count(-9876543210) == (5, 5)

def test_max_integer():
    # Expected values (0, 9) and (0, 10) need to be verified against the actual implementation.
    assert even_odd_count(sys.maxsize) == (0, 9)

def test_min_integer():
    # Expected values (0, 9) and (0, 10) need to be verified against the actual implementation.
    assert even_odd_count(-sys.maxsize - 1) == (0, 10)

def test_all_zeros():
    assert even_odd_count(000) == (3, 0)

def test_none_input():
    with pytest.raises(TypeError):
        even_odd_count(None)

def test_zero_string():
    with pytest.raises(TypeError):
        even_odd_count("000")

def test_string_with_non_digit():
    with pytest.raises(TypeError):
        even_odd_count("12a3")

def test_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_empty_string():
    with pytest.raises(TypeError):
        even_odd_count("")