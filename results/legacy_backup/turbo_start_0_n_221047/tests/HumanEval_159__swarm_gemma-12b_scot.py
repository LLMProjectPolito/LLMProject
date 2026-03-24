import pytest
import math

def test_eat_need_zero():
    """Test case: Need is zero, should return current eaten and remaining."""
    assert eat(5, 0, 10) == [5, 10]