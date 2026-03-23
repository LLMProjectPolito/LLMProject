import pytest
import math


# Focus: Boundary Values
def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining():
    assert eat(1, 10, 5) == [7, 0]

# Focus: Type Scenarios
def test_eat_sufficient_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_insufficient_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_carrots():
    assert eat(1, 10, 5) == [7, 0]

# Focus: Logic Branches
def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining():
    assert eat(1, 10, 5) == [7, 0]