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
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


@pytest.mark.parametrize("numbers, expected", [
    ([1.0, 2.0, 3.0, 4.0], 1.0),
    ([5.0, 5.0, 5.0, 5.0], 0.0),
    ([10.0, 20.0, 30.0, 40.0], 15.0),
    ([-1.0, 0.0, 1.0], 1.0),
    ([0.0, 0.0, 0.0, 0.0], 0.0),
])
def test_mean_absolute_deviation(numbers, expected):
    assert mean_absolute_deviation(numbers) == expected


def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])


def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == 0.0


def test_mean_absolute_deviation_negative_numbers():
    assert mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]) == 1.0


def test_mean_absolute_deviation_mixed_numbers():
    assert mean_absolute_deviation([-1.0, 0.0, 1.0, 2.0]) == 1.0