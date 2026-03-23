import pytest
import math


# Focus: Boundary Values
def test_eat_boundary_need_equals_remaining():
    assert eat(5, 10, 10) == [20, 0]

def test_eat_boundary_need_slightly_greater_than_remaining():
    assert eat(2, 11, 10) == [22, 0]

def test_eat_boundary_number_equals_need():
    assert eat(5, 5, 10) == [10, 5]

# Focus: Type Scenarios
def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_more_carrots_than_needed():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

# Focus: Logic Branches
def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_remaining():
    assert eat(1, 10, 10) == [11, 0]