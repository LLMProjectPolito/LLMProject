import pytest
import math

import pytest

def test_basic():
    """Test the incr_list function with a typical positive case."""
    input_list = [1, 2, 3]
    expected_output = [2, 3, 4]
    assert incr_list(input_list) == expected_output

def test_zeroes():
    """Test function with all zeroes in input list."""
    # Test function with all zeroes in input list
    result = incr_list([0, 0, 0])
    expected_result = [1, 1, 1]
    assert result == expected_result

import pytest

def test_incr_list_invalid_boundary():
    # Test that the function works correctly for an empty list
    assert incr_list([]) == []
    
    # Test that the function works correctly for a list with a single element
    assert incr_list([0]) == [1]
    
    # Test that the function works correctly for a list with multiple negative elements
    assert incr_list([-5, -3, -5, -2, -3, -3, -9, -0, -123]) == [-4, -2, -4, -1, -2, -2, -8, -1, -122]