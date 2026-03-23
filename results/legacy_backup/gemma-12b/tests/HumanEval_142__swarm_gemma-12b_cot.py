import pytest
import math

def test_sum_squares_empty_list():
    """Test with an empty list."""
    assert sum_squares([]) == 0

def test_sum_squares_empty_list_alt():
    """Test case for an empty list."""
    lst = []
    expected_sum = 0
    assert sum_squares(lst) == expected_sum