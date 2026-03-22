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
    assert eat(0, 100, 100) == [100, 0]

def test_eat_more_carrots_than_needed():
    assert eat(1, 5, 10) == [6, 4]

def test_eat_large_numbers():
    assert eat(500, 600, 1000) == [1100, 400]

def test_eat_edge_case_zero_all():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_number_greater_than_remaining():
    assert eat(10, 5, 2) == [7, 0]