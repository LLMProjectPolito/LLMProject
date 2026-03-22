import pytest

def test_eat_example_1():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_example_2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_example_3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_example_4():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_remaining_is_zero():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_not_enough_carrots():
    assert eat(5, 10, 3) == [8, 0]

def test_eat_enough_carrots():
    assert eat(5, 6, 7) == [11, 1]

def test_eat_all_zero():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_number_max_need_zero_remaining_max():
    assert eat(1000, 0, 1000) == [1000, 1000]

def test_eat_number_zero_need_max_remaining_max():
    assert eat(0, 1000, 1000) == [1000, 0]

def test_eat_number_max_need_max_remaining_zero():
    assert eat(1000, 1000, 0) == [1000, 0]

def test_eat_number_5_need_5_remaining_5():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_number_1_need_1_remaining_1():
    assert eat(1, 1, 1) == [2, 0]