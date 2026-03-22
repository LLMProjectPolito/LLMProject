import pytest
import math


# Focus: Boundary Values
import pytest

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_exact_remaining():
    assert eat(4, 8, 4) == [8, 0]

def test_eat_large_remaining():
    assert eat(1, 10, 1000) == [11, 989]

def test_eat_need_equals_remaining():
    assert eat(2, 3, 3) == [5, 0]

def test_eat_number_at_max():
    assert eat(1000, 500, 500) == [1500, 0]

def test_eat_need_at_max():
    assert eat(500, 1000, 1000) == [1500, 0]

def test_eat_remaining_at_max():
    assert eat(500, 500, 1000) == [1000, 500]

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
    assert eat(500, 250, 750) == [750, 500]

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

def test_eat_zero_initial_carrots():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]