
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
    # Examples provided in problem descriptions
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Boundary conditions: Zeros and Edge Cases
    (0, 0, 0, [0, 0]),
    (0, 10, 0, [0, 0]),
    (10, 0, 0, [10, 0]),
    (0, 0, 10, [0, 10]),
    (10, 0, 10, [10, 10]),
    (5, 5, 0, [5, 0]),
    (0, 1, 0, [0, 0]),
    
    # Boundary conditions: Maximum constraints (1000)
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
    (0, 1000, 500, [500, 0]),
    
    # Cases where remaining is exactly equal to need
    (5, 5, 5, [10, 0]),
    (0, 100, 100, [100, 0]),
    (10, 5, 5, [15, 0]),
    
    # Cases where remaining is less than need
    (0, 10, 9, [9, 0]),
    (10, 10, 9, [19, 0]),
    (0, 15, 10, [10, 0]),
    (10, 11, 10, [20, 0]),
    (10, 10, 2, [12, 0]),
    
    # Cases where remaining is more than need
    (0, 10, 11, [10, 1]),
    (10, 10, 11, [20, 1]),
    (0, 5, 10, [5, 5]),
    (10, 9, 10, [19, 1]),
    (10, 5, 20, [15, 15]),
    (100, 1, 2, [101, 1]),
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected