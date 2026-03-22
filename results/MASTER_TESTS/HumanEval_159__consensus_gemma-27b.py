import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_enough_carrots_2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_enough_carrots_3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_enough_carrots_4():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_carrots_needed():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_no_remaining_carrots():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_zero_initial_carrots():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 0) == [5, 0]

def test_eat_large_numbers():
    assert eat(100, 200, 300) == [300, 100]

def test_eat_large_numbers_2():
    assert eat(500, 500, 500) == [1000, 0]

def test_eat_remaining_less_than_needed():
    assert eat(5, 10, 3) == [8, 0]

def test_eat_remaining_equal_to_needed():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_number_equal_to_need():
    assert eat(5, 5, 10) == [10, 5]

def test_eat_all_remaining():
    assert eat(1, 2, 1) == [2, 0]

def test_eat_edge_case_zero_all():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]