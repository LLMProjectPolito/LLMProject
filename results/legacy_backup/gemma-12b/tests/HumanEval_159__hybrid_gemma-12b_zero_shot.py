import pytest

from your_module import eat  # Replace your_module

@pytest.fixture
def sample_data():
    """Provides sample data for the eat function tests."""
    return [
        (5, 6, 10),
        (4, 8, 9),
        (1, 10, 10),
        (2, 11, 5),
        (0, 5, 5),
        (1000, 1, 1),
        (0, 1000, 1000),
        (1000, 1000, 1000),
        (500, 500, 500),
        (0, 0, 0),
        (10, 5, 2),
        (5, 10, 2),
        (1, 1, 1),
        (0, 1, 0),
        (1, 0, 1),
        (10, 20, 0),
        (1, 1, 0),
        (0, 1, 1),
        (1000, 0, 1000),
        (0, 1000, 0),
    ]

def test_eat_sufficient_carrots(sample_data):
    """Tests cases where there are enough carrots to meet the need."""
    for number, need, remaining in sample_data:
        if remaining >= need:
            expected_eaten = number + need
            expected_remaining = remaining - need
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]
        elif remaining < need:
            expected_eaten = number + remaining
            expected_remaining = 0
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_insufficient_carrots(sample_data):
    """Tests cases where there are not enough carrots to meet the need."""
    for number, need, remaining in sample_data:
        if remaining < need:
            expected_eaten = number + remaining
            expected_remaining = 0
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_edge_cases(sample_data):
    """Tests edge cases like zero values and boundary conditions."""
    for number, need, remaining in sample_data:
        if number == 0 and need == 0 and remaining == 0:
            assert eat(number, need, remaining) == [0, 0]
        if number == 1000 and need == 1000 and remaining == 1000:
            assert eat(number, need, remaining) == [2000, 0]
        if number == 1 and need == 1 and remaining == 0:
            assert eat(number, need, remaining) == [1, 0]
        if number == 0 and need == 1 and remaining == 1:
            assert eat(number, need, remaining) == [1, 0]
        if number == 1 and need == 0 and remaining == 1:
            assert eat(number, need, remaining) == [1, 1]
        if number == 1000 and need == 0 and remaining == 1000:
            assert eat(number, need, remaining) == [1000, 1000]
        if number == 0 and need == 1000 and remaining == 0:
            assert eat(number, need, remaining) == [0, 0]

def test_eat_constraints():
    """Tests that the function adheres to the given constraints."""
    assert 0 <= eat(0, 0, 0)[0] <= 1000
    assert 0 <= eat(0, 0, 0)[1] <= 1000
    assert 0 <= eat(1000, 1000, 1000)[0] <= 1000
    assert 0 <= eat(1000, 1000, 1000)[1] <= 1000
    assert 0 <= eat(0, 1000, 0)[0] <= 1000
    assert 0 <= eat(0, 1000, 0)[1] <= 1000

def test_eat_type_checking():
    """Tests that the function handles incorrect input types gracefully."""
    with pytest.raises(TypeError):
        eat("5", 6, 10)
    with pytest.raises(TypeError):
        eat(5, "6", 10)
    with pytest.raises(TypeError):
        eat(5, 6, "10")
    with pytest.raises(TypeError):
        eat(5.5, 6, 10)
    with pytest.raises(TypeError):
        eat(5, 6.5, 10)
    with pytest.raises(TypeError):
        eat(5, 6, 10.5)