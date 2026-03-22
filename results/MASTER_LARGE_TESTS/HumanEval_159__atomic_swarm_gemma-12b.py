import pytest
import math

def test_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_edge_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_negative_need():
    """Test with a negative need value."""
    assert eat(5, -6, 10) == [5, 10]