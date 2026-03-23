import pytest

def test_eat_zero_remaining():
    """Test case for when there are no remaining carrots."""
    assert eat(5, 6, 0) == [5, 0]