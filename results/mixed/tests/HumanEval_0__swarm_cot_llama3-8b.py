import pytest
import math
from your_module import has_close_elements  # replace 'your_module' with the actual module name

def test_has_close_elements_empty_list():
    """Test that has_close_elements returns False for an empty list."""
    assert not has_close_elements([], 0.1)

def test_has_close_elements_zero_threshold():
    # Given a list of numbers with exactly two equal elements, check if the function returns True when threshold is 0.
    # This is an edge case because the function should return True even if there are multiple identical elements.
    assert has_close_elements([1.0, 1.0, 1.0, 3.0], 0.0)

def test_has_close_elements_edge_two_elements():
    numbers = [1.0, 1.000001]  # create two consecutive numbers that are very close to each other
    threshold = 0.000001  # set the threshold to be slightly smaller than their difference

    assert has_close_elements(numbers, threshold) == True