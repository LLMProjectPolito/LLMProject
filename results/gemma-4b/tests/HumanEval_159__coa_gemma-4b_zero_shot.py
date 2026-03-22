import pytest
import math


# Focus: Boundary Values
import pytest

def test_eat_zero_number():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_max_number():
    assert eat(1000, 5, 10) == [1000, 0]

def test_eat_need_zero():
    assert eat(5, 0, 10) == [5, 10]

# Focus: Type Scenarios
import pytest

def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining():
    assert eat(2, 11, 5) == [7, 0]

# Focus: Logic Branches
import pytest

def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining():
    assert eat(1, 10, 5) == [7, 0]