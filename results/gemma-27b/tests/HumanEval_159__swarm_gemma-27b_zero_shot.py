import pytest

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]