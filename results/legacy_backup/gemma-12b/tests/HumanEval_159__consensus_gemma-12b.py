import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_almost_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_zero_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_all_values_zero():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_large_values():
    assert eat(999, 999, 1000) == [1998, 1]

def test_eat_need_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]