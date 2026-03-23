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
    assert eat(0, 5, 10) == [5, 10]

def test_eat_all_carrots_needed():
    assert eat(0, 10, 10) == [10, 0]

def test_eat_large_numbers():
    assert eat(500, 600, 1000) == [1100, 400]

def test_eat_edge_case_equal_need_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_need_greater_than_remaining():
    assert eat(2, 10, 3) == [5, 0]