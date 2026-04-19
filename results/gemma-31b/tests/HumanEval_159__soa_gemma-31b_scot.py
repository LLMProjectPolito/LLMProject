
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

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Boundary cases: Zeroes
    (0, 0, 0, [0, 0]),
    (0, 10, 0, [0, 0]),
    (10, 0, 10, [10, 10]),
    (0, 0, 10, [0, 10]),
    
    # Boundary cases: Maximum constraints
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    
    # Edge cases: remaining vs need
    (10, 5, 6, [15, 1]),   # remaining = need + 1
    (10, 5, 4, [14, 0]),   # remaining = need - 1
    (10, 5, 5, [15, 0]),   # remaining = need
    
    # Edge cases: high need, low stock
    (0, 1000, 1, [1, 0]),
    (100, 1000, 0, [100, 0]),
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected