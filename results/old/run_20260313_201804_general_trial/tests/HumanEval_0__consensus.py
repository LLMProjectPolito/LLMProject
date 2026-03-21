# tests/test_functions.py

import pytest
from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.    
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

# Test cases for has_close_elements function
@pytest.mark.parametrize(
    "numbers, threshold, expected",
    [
        ([1.0, 2.0, 3.0], 0.5, False),
        ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
        ([1.0, 2.0, 3.0], 0.0, True),
        ([1.0, 1.0], 0.0, True),
        ([1.0, 2.0, 3.0], 1.0, False),
        ([1.0, 1.1, 2.0], 0.5, True),
        ([1.0, 2.0, 3.0, 4.0, 5.0], 0.5, False),
        ([1.0, 2.0, 3.0, 4.0, 5.0], 1.0, False),
        ([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, True),
        ([], 0.5, False),
        ([1.0], 0.5, False),
        ([1.0, 2.0, 3.0], 0.5, False),
        ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
        ([1.0, 2.0, 3.0], 0, False),
        ([1.0, 2.0, 3.0], 0, False),
        ([1.0, 2.0, 3.0], 1e6, False),
        ([1.0, -2.8, -3.0, 4.0, 5.0, -2.0], 0.3, True),
        ([1.0, -2.8, 3, 4.0, 5.0, -2.0], 0.3, True),
        ([1.0, 1.0, 1.0], 0.5, False),
        ([1.0, 1.2, 1.0], 0.1, True),
        ([i * 0.1 for i in range(100)], 0.5, False),
        ([i * 0.1 for i in range(100)], 0.5, False),
    ],
)
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool) -> None:
    """Test has_close_elements function with different inputs."""
    assert has_close_elements(numbers, threshold) == expected

def test_has_close_elements_negative_threshold():
    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, 3.0], -0.5)