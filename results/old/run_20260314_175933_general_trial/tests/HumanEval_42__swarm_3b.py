import pytest
import math

def test_incr_list_with_single_element():
    """Test that a list with a single element is incremented correctly."""
    assert incr_list([0]) == [1]

def test_incr_list_with_empty_list():
    """Test the function with an empty list."""
    result = incr_list([])
    assert result == []

# Removed test_zero as it's a duplicate of test_incr_list_with_single_element