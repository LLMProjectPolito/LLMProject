
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """

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
        (10, 10, 10),
        (10, 10, 0),
        (0, 10, 0),
        (1000, 0, 1000),
        (0, 1000, 0),
        (1, 1, 1),
        (1, 1, 0),
        (0, 1, 0),
        (999, 999, 999),
    ]

def test_eat_sufficient_carrots(sample_data):
    """Tests cases where there are enough carrots to meet the need."""
    for number, need, remaining in sample_data:
        if need <= remaining:
            expected_eaten = number + need
            expected_remaining = remaining - need
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_insufficient_carrots(sample_data):
    """Tests cases where there are not enough carrots to meet the need."""
    for number, need, remaining in sample_data:
        if need > remaining:
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
        if number == 1000 and need == 1000 and remaining == 1000:
            assert eat(number, need, remaining) == [2000, 0]
        if number == 0 and need == 0 and remaining == 0:
            assert eat(number, need, remaining) == [0, 0]

def test_eat_large_numbers(sample_data):
    """Tests with larger numbers to ensure no overflow issues."""
    for number, need, remaining in sample_data:
        if number == 999 and need == 999 and remaining == 999:
            assert eat(number, need, remaining) == [2997, 0]

def test_eat_negative_input_raises_error():
    """Tests that negative inputs raise a ValueError."""
    with pytest.raises(ValueError):
        eat(-1, 5, 10)
    with pytest.raises(ValueError):
        eat(5, -1, 10)
    with pytest.raises(ValueError):
        eat(5, 5, -1)

def test_eat_non_integer_input_raises_error():
    """Tests that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        eat(1.5, 5, 10)
    with pytest.raises(TypeError):
        eat(5, 5.5, 10)
    with pytest.raises(TypeError):
        eat(5, 5, 10.5)