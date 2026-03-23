import pytest
import math


# Focus: Boundary Values
import pytest

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_exact_remaining():
    assert eat(5, 6, 1) == [6, 0]

def test_eat_large_remaining():
    assert eat(5, 6, 1000) == [11, 994]

def test_eat_need_zero():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_number_zero():
    assert eat(0, 6, 10) == [6, 4]

def test_eat_number_and_need_zero():
    assert eat(0, 0, 10) == [0, 10]

def test_eat_remaining_equal_need():
    assert eat(5, 6, 6) == [11, 0]

def test_eat_remaining_less_than_need():
    assert eat(5, 6, 5) == [10, 0]

# Focus: Equivalence Partitioning
import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 5, 2) == [2, 0]
    assert eat(100, 200, 50) == [150, 0]

def test_eat_edge_cases():
    assert eat(0, 0, 0) == [0, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(500, 500, 500) == [1000, 0]
    assert eat(0, 1000, 1000) == [1000, 0]
    assert eat(1000, 0, 1000) == [1000, 1000]

# Focus: Logic Branches
import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_all_remaining_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_less_than_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]