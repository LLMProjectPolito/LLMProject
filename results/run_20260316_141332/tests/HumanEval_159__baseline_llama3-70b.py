import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_all_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_more_carrots_needed():
    assert eat(10, 0, 10) == [10, 10]

def test_eat_no_carrots_eaten():
    assert eat(0, 10, 10) == [10, 0]

def test_eat_no_carrots_remaining():
    assert eat(5, 5, 0) == [10, 0]

def test_eat_edge_case_zero():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_edge_case_max():
    assert eat(1000, 0, 1000) == [1000, 1000]

def test_eat_invalid_input():
    with pytest.raises(TypeError):
        eat("a", 5, 10)

def test_eat_negative_input():
    with pytest.raises(ValueError):
        eat(-1, 5, 10)

def test_eat_too_large_input():
    with pytest.raises(ValueError):
        eat(1001, 5, 10)