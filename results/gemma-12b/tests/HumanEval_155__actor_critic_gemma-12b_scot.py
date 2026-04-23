
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
from your_module import even_odd_count  # Replace your_module

def test_valid_positive_integer():
    assert even_odd_count(123) == (1, 2)

def test_valid_negative_integer():
    assert even_odd_count(-12) == (1, 1)

def test_zero_input():
    assert even_odd_count(0) == (1, 0)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(1357) == (0, 4)

def test_mixed_digits():
    assert even_odd_count(123456) == (3, 3)

def test_large_positive_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_large_negative_number():
    assert even_odd_count(-9876543210) == (5, 5)

def test_repeating_digits():
    assert even_odd_count(112233) == (3, 3)

def test_invalid_input_string():
    with pytest.raises(TypeError):
        even_odd_count("abc")

def test_invalid_input_float():
    with pytest.raises(TypeError):
        even_odd_count(1.23)

def test_invalid_input_none():
    with pytest.raises(TypeError):
        even_odd_count(None)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(3) == (0, 1)

def test_boolean_input():
    with pytest.raises(TypeError):
        even_odd_count(True)

def test_very_large_number():
    assert even_odd_count(2147483647) == (3, 8) # Max int 32-bit