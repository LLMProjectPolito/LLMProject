import pytest
import math


# Focus: Boundary Values
def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_exactly_enough_remaining():
    assert eat(5, 6, 1) == [6, 0]

def test_eat_large_remaining():
    assert eat(5, 6, 1000) == [11, 994]

# Focus: Equivalence Partitioning
def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

# Focus: Logic Branches
def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]