
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
    (0, 0, 10, [0, 10]),
    (10, 0, 0, [10, 0]),
    (10, 0, 10, [10, 10]),
    (0, 10, 10, [10, 0]),
    
    # Boundary cases: Maximum constraints (1000)
    (1000, 1000, 1000, [2000, 0]),
    (1000, 1000, 0, [1000, 0]),
    (0, 1000, 1000, [1000, 0]),
    (0, 0, 1000, [0, 1000]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 500, [500, 0]),
    
    # Logic variations: Need vs Remaining
    (100, 50, 200, [150, 150]),    # need < remaining
    (100, 100, 100, [200, 0]),     # need == remaining
    (100, 150, 100, [200, 0]),     # need > remaining
    (50, 1, 10, [51, 9]),          # Minimal need
    (5, 10, 9, [14, 0]),           # remaining is 1 less than need
    (5, 10, 11, [15, 1]),          # remaining is 1 more than need
    (5, 10, 10, [15, 0]),          # remaining is exactly need
    (1, 1, 1000, [2, 999]),        # Large remaining stock
    (500, 0, 500, [500, 500]),     # Not hungry
    (100, 500, 0, [100, 0]),       # Hungry but empty stock
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected