import pytest

def test_bf_same_planet():
    """Test case for when both planets are the same."""
    assert bf("Earth", "Earth") == ()