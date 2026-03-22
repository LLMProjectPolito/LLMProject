import pytest

def test_negative_numbers_with_same_digit_sum():
    assert order_by_points([-10, -1, -100]) == [-1, -10, -100]