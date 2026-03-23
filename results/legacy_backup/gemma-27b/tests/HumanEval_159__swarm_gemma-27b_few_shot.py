import pytest

def test_eat_exactly_enough():
    assert eat(5, 6, 1) == [6, 0]