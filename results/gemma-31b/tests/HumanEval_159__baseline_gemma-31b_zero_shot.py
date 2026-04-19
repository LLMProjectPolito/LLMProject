
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
    
    # Edge cases: Zeroes
    (0, 0, 0, [0, 0]),       # Nothing eaten, nothing needed, nothing left
    (0, 5, 10, [5, 5]),      # Started with 0 eaten
    (5, 0, 10, [5, 10]),     # Needs 0 carrots
    (5, 5, 0, [5, 0]),       # No carrots remaining in stock
    
    # Edge cases: Boundaries (1000)
    (1000, 1000, 1000, [2000, 0]), # Max values, enough stock
    (1000, 1000, 0, [1000, 0]),    # Max values, no stock
    (0, 1000, 1000, [1000, 0]),    # Max need, exact stock
    (0, 1000, 500, [500, 0]),      # Max need, partial stock
    
    # Logic checks: Exact match vs Insufficient
    (10, 5, 5, [15, 0]),     # need == remaining
    (10, 6, 5, [15, 0]),     # need > remaining (by 1)
    (10, 4, 5, [14, 1]),     # need < remaining (by 1)
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with various scenarios including provided examples,
    boundary conditions, and edge cases.
    """
    assert eat(number, need, remaining) == expected