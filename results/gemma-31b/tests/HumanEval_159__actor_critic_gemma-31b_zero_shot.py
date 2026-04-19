
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
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided Examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Edge Case: Zeroes
    (0, 0, 0, [0, 0]),       # Everything is zero
    (0, 5, 10, [5, 5]),      # Started with 0 eaten
    (10, 0, 10, [10, 10]),   # Needs to eat 0
    (10, 5, 0, [10, 0]),     # No carrots remaining in stock
    
    # Edge Case: Exact match
    (10, 5, 5, [15, 0]),     # Remaining exactly equals need
    
    # Edge Case: Maximum Constraints
    (1000, 1000, 1000, [2000, 0]), # Max values, enough stock
    (1000, 1000, 0, [1000, 0]),    # Max values, no stock
    (0, 1000, 1000, [1000, 0]),    # Max need, max stock
    
    # Edge Case: Need is more than remaining
    (10, 100, 50, [60, 0]),  # Rabbit eats all 50, still hungry
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_return_type():
    """Ensure the function returns a list of two integers."""
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)