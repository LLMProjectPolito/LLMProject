import pytest
import math

def test_edge_case_identical_planets():
    """Test when both planets are the same."""
    assert bf("Earth", "Earth") == ()