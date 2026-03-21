import pytest

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (0, 0, 0, [0, 0]),
    (1000, 0, 0, [1000, 0]),
    (0, 1000, 0, [0, 0]),
    (0, 0, 1000, [0, 1000]),
    (1000, 1000, 1000, [2000, 0]),
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_not_enough_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_no_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_zero_input():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_input():
    assert eat(1000, 1000, 1000) == [2000, 0]