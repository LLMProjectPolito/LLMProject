
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
        (1, 1, 1),
        (1, 1, 0),
        (0, 1, 0),
        (1000, 0, 1000),
        (0, 1000, 0),
    ]

def test_eat_sufficient_carrots(sample_data):
    """Tests cases where there are enough carrots to meet the need."""
    for number, need, remaining in sample_data:
        if need <= remaining:
            expected_eaten = number + need
            expected_remaining = remaining - need
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]
        else:
            expected_eaten = number + remaining
            expected_remaining = 0
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_insufficient_carrots(sample_data):
    """Tests cases where there are not enough carrots to meet the need."""
    for number, need, remaining in sample_data:
        if need > remaining:
            expected_eaten = number + remaining
            expected_remaining = 0
            assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_edge_cases(sample_data):
    """Tests edge cases like zero values and maximum values."""
    for number, need, remaining in sample_data:
        if number == 1000 and need == 1 and remaining == 1:
            assert eat(number, need, remaining) == [1001, 0]
        if number == 0 and need == 1000 and remaining == 1000:
            assert eat(number, need, remaining) == [1000, 0]
        if number == 1000 and need == 1000 and remaining == 1000:
            assert eat(number, need, remaining) == [2000, 0]
        if number == 500 and need == 500 and remaining == 500:
            assert eat(number, need, remaining) == [1000, 0]
        if number == 0 and need == 0 and remaining == 0:
            assert eat(number, need, remaining) == [0, 0]
        if number == 10 and need == 5 and remaining == 2:
            assert eat(number, need, remaining) == [12, 0]
        if number == 5 and need == 10 and remaining == 2:
            assert eat(number, need, remaining) == [7, 0]
        if number == 1 and need == 1 and remaining == 1:
            assert eat(number, need, remaining) == [2, 0]
        if number == 1 and need == 1 and remaining == 0:
            assert eat(number, need, remaining) == [1, 0]
        if number == 0 and need == 1 and remaining == 0:
            assert eat(number, need, remaining) == [0, 0]
        if number == 1000 and need == 0 and remaining == 1000:
            assert eat(number, need, remaining) == [1000, 1000]
        if number == 0 and need == 1000 and remaining == 0:
            assert eat(number, need, remaining) == [0, 0]

def test_eat_invalid_input():
    """Tests cases with invalid input (negative values)."""
    with pytest.raises(TypeError):
        eat(-1, 5, 10)
    with pytest.raises(TypeError):
        eat(5, -1, 10)
    with pytest.raises(TypeError):
        eat(5, 5, -1)
    with pytest.raises(TypeError):
        eat(5.5, 5, 10)
    with pytest.raises(TypeError):
        eat(5, 5.5, 10)
    with pytest.raises(TypeError):
        eat(5, 5, 10.5)