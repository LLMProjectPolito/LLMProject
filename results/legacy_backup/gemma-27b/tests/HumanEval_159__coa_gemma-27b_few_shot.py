import pytest
import math


# Focus: Boundary Values
def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_exactly_enough_remaining():
    assert eat(5, 6, 1) == [6, 0]

def test_eat_large_remaining():
    assert eat(5, 6, 1000) == [1005, 994]

def test_eat_need_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_number_equals_remaining():
    assert eat(5, 6, 5) == [10, 0]

# Focus: Equivalence Partitioning
def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exact_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_carrots_needed():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_no_carrots_remaining():
    assert eat(5, 6, 0) == [5, 0]

# Focus: Logic Branches
def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_all_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_carrots_needed():
    assert eat(5, 5, 10) == [10, 5]