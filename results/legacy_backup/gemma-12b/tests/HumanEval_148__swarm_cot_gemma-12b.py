import pytest
import math

def test_bf_identical_planets():
    """Test case: Both planets are the same, should return an empty tuple."""
    from your_module import bf  # Replace your_module
    result = bf("Earth", "Earth")
    assert result == ()