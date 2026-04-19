
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
    """
    eaten_now = min(need, remaining)
    return [number + eaten_now, remaining - eaten_now]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Boundary cases: Zeroes
    (0, 0, 0, [0, 0]),
    (0, 0, 10, [0, 10]),
    (10, 0, 10, [10, 10]),
    (10, 10, 0, [10, 0]),
    (0, 10, 0, [0, 0]),
    
    # Boundary cases: Exact amounts
    (0, 5, 5, [5, 0]),
    (10, 5, 5, [15, 0]),
    
    # Insufficient carrots
    (10, 100, 1, [11, 0]),
    (10, 1, 0, [10, 0]),
    
    # Sufficient carrots
    (10, 1, 100, [11, 99]),
    (0, 1, 1, [1, 0]),
    
    # Maximum constraints
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected