import pytest
import math  # Included as a standard import per requirements


def test_eat_zero_remaining():
    """Test case where there are no remaining carrots."""
    assert eat(5, 6, 0) == [5, 0]