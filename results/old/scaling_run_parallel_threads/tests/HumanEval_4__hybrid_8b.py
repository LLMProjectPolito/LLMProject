import pytest
from statistics import mean
from typing import List

@pytest.mark.parametrize("numbers, expected", [
    ([1.0, 2.0, 3.0, 4.0], 1.0),
    ([5.0, 5.0, 5.0, 5.0], 0.0),
    ([-1.0, 0.0, 1.0], 1.0),
    ([10.0, 20.0, 30.0], 10.0),
    ([10.5, 11.5, 12.5], 1.0),
    ([1.0, 1.0, 1.0, 1.0], 0.0),
    ([0.5, 1.5, 2.5], 1.0),
    ([1.0, 1.0, 1.0, 10.0], 3.25),
    ([i for i in range(1000)], 250.0)
])
def test_mean_absolute_deviation(numbers, expected):
    assert mean_absolute_deviation(numbers) == expected

def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

def test_mean_absolute_deviation_single_element_list():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_mean_absolute_deviation_non_numeric_input():
    with pytest.raises(TypeError):
        mean_absolute_deviation(['a', 'b', 'c'])

def test_mean_absolute_deviation_mixed_numeric_input():
    with pytest.raises(TypeError):
        mean_absolute_deviation([1, 'a', 3.0])