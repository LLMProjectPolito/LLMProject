
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_positive_number():
    assert even_odd_count(123456) == (3, 3)

def test_zero():
    assert even_odd_count(0) == (1, 0)  # Zero is considered even

def test_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_mixed_even_and_odd_digits():
    assert even_odd_count(12345) == (2, 3)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_leading_zeroes():
    assert even_odd_count(102) == (2, 1)

def test_trailing_zeroes():
    assert even_odd_count(120) == (2, 1)

def test_multiple_zeroes():
    assert even_odd_count(10020) == (3, 1)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_negative_number_with_zeroes():
    assert even_odd_count(-1020) == (2, 2)

def test_invalid_input_string():
    with pytest.raises(TypeError):
        even_odd_count("abc")

def test_invalid_input_list():
    with pytest.raises(TypeError):
        even_odd_count([])

def test_large_negative_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_max_integer():
    assert even_odd_count(2147483647) == (4, 5)

def test_min_integer():
    assert even_odd_count(-2147483648) == (1, 5)

def test_input_type():
    with pytest.raises(TypeError):
        even_odd_count(1.5)