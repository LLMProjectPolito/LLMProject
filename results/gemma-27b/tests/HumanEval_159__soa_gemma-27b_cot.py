import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 5, 2) == [2, 0]
    assert eat(10, 20, 5) == [15, 0]

def test_eat_exact_carrots():
    assert eat(5, 5, 5) == [10, 0]
    assert eat(0, 0, 10) == [0, 10]
    assert eat(10, 10, 10) == [20, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 0, 5) == [10, 5]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]
    assert eat(0, 5, 0) == [0, 0]
    assert eat(10, 20, 0) == [10, 0]

def test_eat_edge_cases():
    assert eat(0, 1000, 1000) == [1000, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(500, 500, 500) == [1000, 0]
    assert eat(1000, 0, 0) == [1000, 0]
    assert eat(0, 0, 0) == [0, 0]

def test_eat_large_numbers():
    assert eat(999, 999, 999) == [1998, 0]
    assert eat(500, 499, 1) == [999, 0]
    assert eat(1, 999, 999) == [1000, 0]