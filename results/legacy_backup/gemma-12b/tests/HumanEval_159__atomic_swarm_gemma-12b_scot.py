import pytest
import math

def test_eat_positive():
    assert eat(5, 6, 10) == [11, 4]

def test_edge_remaining_zero():
    """Test case: remaining carrots are zero."""
    number = 5
    need = 6
    remaining = 0
    expected = [5, 0]
    assert eat(number, need, remaining) == expected

def test_need_is_zero():
    assert eat(5, 0, 10) == [5, 10]
    assert eat(0, 0, 5) == [0, 5]
    assert eat(1000, 0, 1000) == [1000, 1000]