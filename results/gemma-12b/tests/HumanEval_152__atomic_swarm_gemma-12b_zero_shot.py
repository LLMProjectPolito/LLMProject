import pytest
import math

def test_basic():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_edge_empty_input():
    """Test with empty input lists."""
    assert compare([], []) == []

def test_invalid_input_types():
    """Test with non-list inputs."""
    try:
        compare("123", [1, 2, 3])
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass

    try:
        compare([1, 2, 3], "123")
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass