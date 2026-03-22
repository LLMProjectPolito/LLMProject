import pytest
import math

def test_double_the_difference_positive():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_empty_list():
    """Test with an empty list."""
    assert double_the_difference([]) == 0

def test_double_the_difference_invalid_input():
    """Test with a list containing a string."""
    assert double_the_difference([1, 2, "a", 4]) == 1