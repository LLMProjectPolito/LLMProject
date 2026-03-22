import pytest
import math

def test_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_edge():
    assert eat(0, 0, 10) == [0, 10]
    assert eat(10, 0, 10) == [10, 0]
    assert eat(0, 10, 0) == [10, 0]
    assert eat(5, 5, 5) == [10, 0]

import pytest

def test_eat_no_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]