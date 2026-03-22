import pytest
import math


# Focus: Boundary Values
def test_eat_boundary_need_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_boundary_need_one_more_than_remaining():
    assert eat(5, 6, 5) == [11, 0]

def test_eat_boundary_need_zero():
    assert eat(5, 0, 10) == [5, 10]

# Focus: Type Scenarios
def test_eat_sufficient_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_insufficient_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exact_need():
    assert eat(1, 10, 10) == [11, 0]

# Focus: Logic Branches
def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]