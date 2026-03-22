import pytest
import math

def test_order_by_points_positive():
    nums = [1, 11, -1, -11, -12]
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(nums) == expected

def test_empty_input():
    """Test with an empty input list."""
    from solution import order_by_points
    assert order_by_points([]) == []

import pytest

def test_order_by_points_invalid_input():
    """
    Test case with a list containing a non-integer element.
    This tests the robustness of the function when it encounters
    an unexpected data type within the input list.
    """
    with pytest.raises(TypeError):
        order_by_points([1, 2, "a", 4])