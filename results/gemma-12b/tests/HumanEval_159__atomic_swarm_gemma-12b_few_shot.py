import pytest
import math

def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_negative_need():
    assert eat(5, -1, 10) == [5, 10]

def test_eat_negative_need():
    assert eat(5, -1, 10) == [5, 10]