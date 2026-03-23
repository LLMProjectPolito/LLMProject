import pytest
import math

def test_bf_identical_planets():
    """Test case: When planet1 and planet2 are the same, expect an empty tuple."""
    assert bf("Earth", "Earth") == ()