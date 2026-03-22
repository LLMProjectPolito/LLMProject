import pytest
import math
from statistics import mean

def test_mean_absolute_deviation_single_element():
    """ Ensure that a single element dataset returns 0.0, as there's no deviation from the mean """
    result = mean_absolute_deviation([5.0])
    assert result == 0.0

def test_mean_absolute_deviation_empty_list():
    """ Edge case: List with a single element that is the mean of the list """
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([mean([1.0])])