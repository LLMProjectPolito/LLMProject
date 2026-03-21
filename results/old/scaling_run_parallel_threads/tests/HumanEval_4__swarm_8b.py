import pytest
import math
from statistics import mean

def test_mean_absolute_deviation_empty_input():
    """
    Edge case: Test that the function raises an exception for an empty list.

    Args:
        None

    Returns:
        None
    """
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

def test_mean_absolute_deviation_non_empty_list():
    """
    Test case to ensure that the function correctly calculates the mean absolute deviation for a non-empty list.
    """
    data = [1, 2, 3, 4, 5]
    mean_value = mean(data)
    expected_mad = sum(abs(x - mean_value) for x in data) / len(data)
    assert mean_absolute_deviation(data) == expected_mad

def test_mean_absolute_deviation_single_element_list():
    """
    Edge case: Test that the function correctly handles a list with a single element.
    """
    data = [5]
    assert mean_absolute_deviation(data) == 0