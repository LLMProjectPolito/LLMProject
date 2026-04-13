
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
from your_module import even_odd_count  # Replace your_module

def test_even_odd_count_positive_number():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_negative_number():
    assert even_odd_count(-123456) == (3, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_mixed_digits():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_number_with_repeating_digits():
    assert even_odd_count(2222) == (4, 0)

def test_even_odd_count_number_with_repeating_digits_odd():
    assert even_odd_count(1111) == (0, 4)

def test_even_odd_count_number_with_mixed_repeating_digits():
    assert even_odd_count(1212) == (2, 2)

def test_even_odd_count_number_with_leading_zeros():
    assert even_odd_count(10203) == (2, 2)

def test_even_odd_count_number_with_trailing_zeros():
    assert even_odd_count(12300) == (2, 2)

def test_even_odd_count_number_with_zeros_in_between():
    assert even_odd_count(10101) == (2, 3)

def test_even_odd_count_empty_string_input():
    with pytest.raises(TypeError):
        even_odd_count("")

def test_even_odd_count_float_input():
    with pytest.raises(TypeError):
        even_odd_count(1.23)

def test_even_odd_count_string_input():
    with pytest.raises(TypeError):
        even_odd_count("123")

def test_even_odd_count_none_input():
    with pytest.raises(TypeError):
        even_odd_count(None)