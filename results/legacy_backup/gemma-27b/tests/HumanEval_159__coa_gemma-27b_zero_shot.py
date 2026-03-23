import pytest
import math


# Focus: Boundary Values
import pytest

def test_eat_boundary_remaining_zero():
    assert eat(10, 5, 0) == [10, 0]

def test_eat_boundary_need_zero():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_boundary_number_zero():
    assert eat(0, 5, 10) == [5, 5]

# Focus: Equivalence Partitioning
import pytest

def test_equivalence_partitioning_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]

def test_equivalence_partitioning_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]
    assert eat(10, 20, 5) == [15, 0]
    assert eat(5, 10, 2) == [7, 0]

def test_equivalence_partitioning_zero_values():
    assert eat(0, 0, 0) == [0, 0]
    assert eat(0, 5, 10) == [5, 5]
    assert eat(5, 0, 0) == [5, 0]
    assert eat(0, 5, 0) == [0, 0]

# Focus: Logic Branches
import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_all_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_needed_carrots():
    assert eat(1, 10, 10) == [11, 0]