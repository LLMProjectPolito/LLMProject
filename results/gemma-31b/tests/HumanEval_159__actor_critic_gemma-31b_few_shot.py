
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

def test_eat_sufficient_carrots():
    """ Test cases where there are more than enough carrots to satisfy the need """
    # Example: eat(5, 6, 10) -> [11, 4]
    assert eat(5, 6, 10) == [11, 4]
    # Example: eat(4, 8, 9) -> [12, 1]
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exact_carrots():
    """ Test cases where the remaining carrots exactly match the need """
    # Example: eat(1, 10, 10) -> [11, 0]
    assert eat(1, 10, 10) == [11, 0]

def test_eat_insufficient_carrots():
    """ Test cases where there are not enough carrots to satisfy the need """
    # Example: eat(2, 11, 5) -> [7, 0]
    assert eat(2, 11, 5) == [7, 0]
    # Rabbit needs 100 but only 1 is left
    assert eat(10, 100, 1) == [11, 0]

def test_eat_zero_values():
    """ Test edge cases involving zero """
    # Already eaten 0, needs 5, 10 available
    assert eat(0, 5, 10) == [5, 5]
    # Already eaten 5, needs 0, 10 available (rabbit isn't hungry)
    assert eat(5, 0, 10) == [5, 10]
    # Already eaten 5, needs 5, 0 available (no food in stock)
    assert eat(5, 5, 0) == [5, 0]
    # All zeros
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_constraints():
    """ Test the upper boundaries of the constraints (1000) """
    # Max values: already eaten 1000, needs 1000, 1000 available
    assert eat(1000, 1000, 1000) == [2000, 0]
    # Max values: already eaten 1000, needs 1000, 0 available
    assert eat(1000, 1000, 0) == [1000, 0]