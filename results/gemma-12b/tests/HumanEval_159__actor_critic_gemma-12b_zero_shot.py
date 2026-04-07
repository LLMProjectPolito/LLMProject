
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
    total_eaten = number
    remaining_carrots = remaining
    
    if remaining >= need:
        total_eaten += need
        remaining_carrots -= need
    else:
        total_eaten += remaining
        remaining_carrots = 0
    
    return [total_eaten, remaining_carrots]

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),  # Sufficient remaining carrots to meet the need
    (4, 8, 9, [12, 1]),  # Sufficient remaining carrots to meet the need
    (1, 10, 10, [11, 0]), # Sufficient remaining carrots to meet the need
    (2, 11, 5, [7, 0]),  # Not enough remaining carrots
    (0, 0, 0, [0, 0]),   # All zeros
    (0, 5, 10, [5, 5]),  # Zero eaten, need some, remaining available
    (1000, 1000, 1000, [2000, 0]), # Max values, enough carrots
    (0, 1000, 0, [0, 0]), # Zero eaten, max need, zero remaining
    (1000, 0, 1000, [1000, 1000]), # Max eaten, zero need, remaining available
    (500, 500, 500, [1000, 0]), # Need and remaining equal
    (100, 200, 100, [200, 0]), # Need more than remaining
    (200, 100, 100, [300, 0]), # Remaining more than need
    (0, 1, 1, [1, 0]),   # Small values, need exactly one
    (1, 0, 1, [1, 1]),   # One eaten, zero need
    (1000, 1, 1, [1001, 0]), # Max eaten, need one, one remaining
    (1, 1000, 1, [1001, 0]), # One eaten, max need, one remaining
    (5, 5, 5, [10, 0]), # Need and remaining equal, number > 0
    (0, 0, 5, [0, 5]), # Need and number are 0, remaining > 0
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (1, 1, 1, [2, 0]),  # Need and remaining equal, number > 0
    (0, 0, 0, [0, 0]),  # All zeros
])
def test_equal_need_remaining(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (1001, 100, 100),  # Number exceeds constraint
    (100, 1001, 100),  # Need exceeds constraint
    (100, 100, 1001),  # Remaining exceeds constraint
    (-1, 100, 100),   # Negative number
    (100, -1, 100),   # Negative need
    (100, 100, -1),   # Negative remaining
])
def test_invalid_inputs(number, need, remaining, expected):
    try:
        eat(number, need, remaining)
        assert False, "Should have raised an exception"
    except Exception:
        pass