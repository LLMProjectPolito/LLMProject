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
        (5, 10, 0),
        (100, 1, 100),
        (1, 100, 100),
        (1000, 1000, 0),
        (0, 1000, 0),
        (1000, 0, 1000),
        (0, 0, 1000),
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

def test_eat_zero_need(sample_data):
    """Tests cases where the need is zero."""
    for number, need, remaining in sample_data:
        if need == 0:
            expected_eaten = number
            expected_remaining = remaining
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_zero_remaining(sample_data):
    """Tests cases where there are no carrots remaining."""
    for number, need, remaining in sample_data:
        if remaining == 0:
            expected_eaten = number
            expected_remaining = 0
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_edge_cases(sample_data):
    """Tests edge cases like maximum values and zero values."""
    for number, need, remaining in sample_data:
        assert isinstance(eat(number, need, remaining)[0], int)
        assert isinstance(eat(number, need, remaining)[1], int)

def test_eat_large_numbers(sample_data):
    """Tests with large numbers to ensure no overflow issues."""
    for number, need, remaining in sample_data:
        result = eat(number, need, remaining)
        assert result[0] >= 0
        assert result[1] >= 0

def test_eat_invalid_input():
    """Tests with invalid input (negative numbers) - should not happen based on constraints, but good to check."""
    with pytest.raises(TypeError):
        eat(-1, 5, 10)
    with pytest.raises(TypeError):
        eat(5, -1, 10)
    with pytest.raises(TypeError):
        eat(5, 5, -1)

def test_eat_input_types():
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