import pytest
from typing import List
import math

def test_mean_absolute_deviation_empty_list():
    # Test that an empty list raises a more informative error
    with pytest.raises(ZeroDivisionError) as e:
        mean_absolute_deviation([])
    assert str(e.value) == "division by zero"

def test_mean_absolute_deviation_single_element():
    # Test that MAD is 0 when the input list contains a single element
    assert mean_absolute_deviation([0.0]) == 0.0
    assert mean_absolute_deviation([1.0]) == 0.0