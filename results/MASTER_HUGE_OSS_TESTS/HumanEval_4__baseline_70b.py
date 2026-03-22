import pytest
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_mean_absolute_deviation_multiple_elements():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

def test_mean_absolute_deviation_negative_numbers():
    assert mean_absolute_deviation([-1.0, 0.0, 1.0]) == 1.0

def test_mean_absolute_deviation_float_numbers():
    assert mean_absolute_deviation([1.5, 2.5, 3.5]) == 0.5

def test_mean_absolute_deviation_large_numbers():
    assert mean_absolute_deviation([1000.0, 2000.0, 3000.0]) == 1000.0

def test_mean_absolute_deviation_mixed_numbers():
    assert mean_absolute_deviation([-10.0, 0.0, 10.0]) == 10.0

def test_mean_absolute_deviation_repeated_numbers():
    assert mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0