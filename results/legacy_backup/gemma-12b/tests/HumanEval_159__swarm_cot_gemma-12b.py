import pytest
import math

def test_eat_need_equals_remaining():
    """Test case: need is exactly equal to remaining carrots."""
    assert eat(5, 6, 6) == [11, 0]