import pytest

def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_basic_2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_basic_3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_basic_4():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_enough_remaining():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_exact_remaining():
    assert eat(0, 5, 5) == [5, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_zero_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_large_numbers():
    assert eat(999, 999, 1000) == [1998, 1]

def test_eat_large_numbers_2():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_large_numbers_3():
    assert eat(500, 600, 200) == [700, 0]

def test_eat_edge_case_1():
    assert eat(1000, 1000, 0) == [1000, 0]

def test_eat_edge_case_2():
    assert eat(0, 1000, 0) == [0, 0]

def test_eat_edge_case_3():
    assert eat(1000, 0, 1000) == [1000, 1000]

def test_eat_all_remaining():
    assert eat(5, 10, 3) == [8, 0]

def test_eat_all_remaining_2():
    assert eat(10, 20, 1) == [11, 0]

def test_eat_all_remaining_3():
    assert eat(0, 10, 1) == [1, 0]