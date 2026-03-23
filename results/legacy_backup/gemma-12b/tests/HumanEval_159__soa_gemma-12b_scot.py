import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_almost_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_initial_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_large_numbers():
    assert eat(999, 999, 1000) == [1998, 1]

def test_eat_equal_need_and_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_need_greater_than_remaining():
    assert eat(10, 20, 5) == [15, 0]

def test_eat_all_remaining_carrots():
    assert eat(100, 200, 50) == [150, 0]

def test_eat_edge_case_zero_all():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_number_at_max():
    assert eat(1000, 1, 1000) == [1001, 999]

def test_eat_need_at_max():
    assert eat(1, 1000, 1000) == [1001, 0]

def test_eat_remaining_at_max():
    assert eat(1, 1, 1000) == [2, 998]