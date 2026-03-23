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

def test_eat_zero_initial_and_need():
    assert eat(0, 0, 10) == [0, 10]

def test_eat_large_numbers():
    assert eat(100, 200, 300) == [300, 0]

def test_eat_large_numbers_2():
    assert eat(500, 600, 700) == [1100, 100]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_max_initial():
    assert eat(1000, 1, 1) == [1001, 0]

def test_eat_max_need():
    assert eat(1, 1000, 1000) == [1001, 0]

def test_eat_max_remaining():
    assert eat(1, 1, 1000) == [2, 999]