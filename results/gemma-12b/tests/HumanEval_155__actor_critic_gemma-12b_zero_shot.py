
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
from your_module import even_odd_count  # Replace your_module

def _assert_value_error(func, input_value, expected_exception_type):
    """Helper function to assert that a ValueError is raised with the expected type."""
    with pytest.raises(expected_exception_type) as excinfo:
        func(input_value)


def test_positive_number():
    assert even_odd_count(123456) == (3, 3)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_mixed_digits():
    assert even_odd_count(12345) == (2, 3)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_number_with_leading_zeros():
    assert even_odd_count(10203) == (2, 2)

def test_negative_number_with_zeros():
    assert even_odd_count(-102) == (2, 1)

def test_empty_input():
    _assert_value_error(even_odd_count, None, ValueError)

def test_string_input():
    _assert_value_error(even_odd_count, "123", ValueError)

def test_string_input_non_numeric():
    _assert_value_error(even_odd_count, "1a2b3", ValueError)

def test_float_input():
    _assert_value_error(even_odd_count, 12.3, ValueError)

def test_decimal_input():
    import decimal
    _assert_value_error(even_odd_count, decimal.Decimal('12.3'), ValueError)

def test_very_large_number():
    assert even_odd_count(2147483647) == (0, 10)

def test_repeating_digits():
    assert even_odd_count(112233) == (3, 3)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(4) == (1, 0)
    assert even_odd_count(6) == (1, 0)
    assert even_odd_count(8) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(5) == (0, 1)
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(9) == (0, 1)

def test_negative_single_digit():
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-2) == (1, 0)
    assert even_odd_count(-3) == (0, 1)
    assert even_odd_count(-4) == (1, 0)
    assert even_odd_count(-5) == (0, 1)
    assert even_odd_count(-6) == (1, 0)
    assert even_odd_count(-7) == (0, 1)
    assert even_odd_count(-8) == (1, 0)
    assert even_odd_count(-9) == (0, 1)

def test_boolean_input():
    _assert_value_error(even_odd_count, True, ValueError)
    _assert_value_error(even_odd_count, False, ValueError)