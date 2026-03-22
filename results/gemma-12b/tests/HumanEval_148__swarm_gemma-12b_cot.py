import pytest
import math

def test_bf_identical_planets():
    """Test case: planet1 and planet2 are the same."""
    from your_module import bf  # Replace your_module
    result = bf("Earth", "Earth")
    assert result == ()