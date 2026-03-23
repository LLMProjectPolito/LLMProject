import pytest
import math

def test_find_max_positive():
    assert find_max(["name", "of", "string"]) == "string"

def test_empty_input():
    """Test with an empty list of words."""
    assert find_max([]) == ""

def test_find_max_empty_list():
    """Test with an empty list."""
    from solution import find_max
    assert find_max([]) == ""