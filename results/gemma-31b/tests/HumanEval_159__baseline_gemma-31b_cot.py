
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
    (5, 6, 10, [11, 4]),   # Sufficient carrots
    (4, 8, 9, [12, 1]),    # Sufficient carrots
    (1, 10, 10, [11, 0]),  # Exactly enough carrots
    (2, 11, 5, [7, 0]),    # Insufficient carrots

    # Edge Cases: Zeros
    (0, 0, 0, [0, 0]),     # All zeros
    (0, 5, 10, [5, 5]),    # Start with 0 eaten
    (5, 0, 10, [5, 10]),   # Need 0 carrots
    (5, 5, 0, [5, 0]),     # No carrots remaining in stock
    (0, 5, 0, [0, 0]),     # Start 0, need 5, stock 0

    # Edge Cases: Boundaries (Max 1000)
    (1000, 1000, 1000, [2000, 0]), # Max values, exactly enough
    (1000, 1000, 2000, [2000, 1000]), # Max values, more than enough (though constraint says remaining <= 1000, testing robustness)
    (1000, 1000, 0, [1000, 0]),    # Max values, none remaining
    (0, 1000, 1000, [1000, 0]),    # Min eaten, max need, max stock
    (0, 1000, 500, [500, 0]),      # Min eaten, max need, partial stock

    # Logic check: remaining < need
    (10, 100, 50, [60, 0]),        # Eat all remaining, still hungry
    (10, 1, 50, [11, 49]),         # Eat only what is needed
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with various scenarios including sufficient, 
    insufficient, and boundary carrot counts.
    """
    assert eat(number, need, remaining) == expected