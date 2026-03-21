import pytest
from typing import List

def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([1.0]) == 0.0

def test_mean_absolute_deviation_two_elements():
    assert mean_absolute_deviation([1.0, 2.0]) == 0.5

def test_mean_absolute_deviation_multiple_elements():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

def test_mean_absolute_deviation_negative_numbers():
    assert mean_absolute_deviation([-1.0, 0.0, 1.0]) == 1.0

def test_mean_absolute_deviation_float_numbers():
    assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5]) == 1.0

def test_mean_absolute_deviation_large_numbers():
    assert mean_absolute_deviation([1000.0, 2000.0, 3000.0, 4000.0]) == 1000.0

def test_mean_absolute_deviation_zero():
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]) == 0.0

def test_mean_absolute_deviation_non_numeric_input():
    with pytest.raises(TypeError):
        mean_absolute_deviation([1, 'a', 3, 4])

def test_mean_absolute_deviation_none_input():
    with pytest.raises(TypeError):
        mean_absolute_deviation([1, None, 3, 4])