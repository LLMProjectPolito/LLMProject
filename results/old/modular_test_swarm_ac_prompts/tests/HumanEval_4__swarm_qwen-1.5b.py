import pytest
import math

def test_mean_absolute_deviation_empty_list():
    """Edge case: calculate MAD for an empty list"""
    assert math.isnan(mean_absolute_deviation([]))

def test_mean_absolute_deviation_single_element_list():
    """ Test Mean Absolute Deviation calculation for a list with only one element.
        Expected behavior: MAD should be zero since there's no deviation from the mean.
    """
    assert mean_absolute_deviation([3.0]) == 0.0

def test_mean_absolute_deviation_multiple_element_list():
    """ Test Mean Absolute Deviation calculation for a list with multiple elements.
        Expected behavior: MAD should be calculated correctly.
    """
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    assert mean_absolute_deviation(numbers) == mad