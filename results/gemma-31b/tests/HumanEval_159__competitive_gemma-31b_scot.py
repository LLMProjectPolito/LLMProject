
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
    (5, 6, 10, [11, 4]),    # Example 1: Enough carrots
    (4, 8, 9, [12, 1]),     # Example 2: Enough carrots
    (1, 10, 10, [11, 0]),   # Example 3: Exactly enough carrots
    (2, 11, 5, [7, 0]),     # Example 4: Not enough carrots
    (0, 0, 0, [0, 0]),      # Zeroes
    (10, 0, 10, [10, 10]),  # No need to eat
    (10, 5, 0, [10, 0]),    # No carrots remaining
    (0, 5, 10, [5, 5]),     # Started with zero eaten
    (1000, 1000, 1000, [2000, 0]), # Max constraints: enough
    (1000, 1000, 500, [1500, 0]),  # Max constraints: not enough
    (0, 1000, 1000, [1000, 0]),    # Max need, max remaining
    (1000, 0, 1000, [1000, 1000]), # Max eaten, no need
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected