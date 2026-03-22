import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_more_carrots_than_needed():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_needed_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_all_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_carrots_initially():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_carrots_needed():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_carrots_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_large_numbers():
    assert eat(999, 999, 1000) == [1998, 1]

def test_eat_large_numbers_2():
    assert eat(100, 1000, 500) == [600, 0]

def test_eat_equal_numbers():
    assert eat(10, 10, 10) == [20, 0]

def test_eat_need_greater_than_remaining():
    assert eat(5, 15, 5) == [10, 0]

def test_eat_number_is_zero_need_is_zero():
    assert eat(0, 0, 10) == [0, 10]

def test_eat_number_is_zero_need_is_not_zero():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_number_is_not_zero_need_is_zero():
    assert eat(5, 0, 10) == [5, 10]