import pytest
import math

def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_zero_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_not_enough_remaining():
    assert eat(2, 11, 5) == [7, 0]