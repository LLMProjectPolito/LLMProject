import pytest
import math

import pytest

def test_basic():
    assert eat(5, 6, 10) == [11, 4]

import pytest

def test_edge_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

import pytest

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]