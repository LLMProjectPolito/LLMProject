
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
    # Provided Examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Edge Case: Zero values
    (0, 0, 0, [0, 0]),
    (0, 5, 10, [5, 5]),
    (5, 0, 10, [5, 10]),
    (5, 5, 0, [5, 0]),
    
    # Edge Case: Need is exactly equal to remaining
    (10, 5, 5, [15, 0]),
    
    # Edge Case: Need is much larger than remaining
    (10, 1000, 1, [11, 0]),
    
    # Edge Case: Remaining is much larger than need
    (10, 1, 1000, [11, 999]),
    
    # Edge Case: Negative input values
    # Starting eaten is negative
    (-1, 5, 10, [4, 5]),
    # Need is negative (should eat 0)
    (5, -1, 10, [5, 10]),
    # Remaining is negative (should eat 0)
    (5, 5, -1, [5, -1]),
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with various scenarios including sufficient, 
    insufficient, boundary, and negative carrot counts.
    """
    assert eat(number, need, remaining) == expected