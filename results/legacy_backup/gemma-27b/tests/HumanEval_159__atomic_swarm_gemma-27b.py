import pytest
import math

def test_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_edge_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

import pytest

def test_eat_remaining_zero():
    assert eat(5, 6, 0) == [5, 0]