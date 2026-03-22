import pytest

def test_negative_numbers_with_same_digit_sum():
    """Test case for negative numbers with the same digit sum, ensuring original order is preserved."""
    nums = [-11, -2, -101]
    expected = [-11, -2, -101]
    assert order_by_points(nums) == expected