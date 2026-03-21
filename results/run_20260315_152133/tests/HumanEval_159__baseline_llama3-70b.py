import pytest

def test_eat_base_case():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_base_case_2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_base_case_3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_carrots_needed():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_no_carrots_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_no_carrots_eaten_and_no_carrots_needed():
    assert eat(0, 0, 10) == [0, 10]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_zero_values():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_negative_values():
    with pytest.raises(ValueError):
        eat(-1, 0, 0)

def test_eat_negative_values_2():
    with pytest.raises(ValueError):
        eat(0, -1, 0)

def test_eat_negative_values_3():
    with pytest.raises(ValueError):
        eat(0, 0, -1)

def test_eat_non_integer_values():
    with pytest.raises(TypeError):
        eat(1.5, 0, 0)

def test_eat_non_integer_values_2():
    with pytest.raises(TypeError):
        eat(0, 1.5, 0)

def test_eat_non_integer_values_3():
    with pytest.raises(TypeError):
        eat(0, 0, 1.5)