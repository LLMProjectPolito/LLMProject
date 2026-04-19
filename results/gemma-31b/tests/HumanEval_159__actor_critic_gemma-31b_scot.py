
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
from solution import eat

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided Examples
    (5, 6, 10, [11, 4]),   # Sufficient carrots
    (4, 8, 9, [12, 1]),    # Sufficient carrots
    (1, 10, 10, [11, 0]),  # Exact amount
    (2, 11, 5, [7, 0]),    # Insufficient carrots
    
    # Edge Cases: Zeroes
    (0, 5, 10, [5, 5]),    # Initial eaten is 0
    (5, 0, 10, [5, 10]),   # Need is 0 (eats nothing)
    (5, 6, 0, [5, 0]),     # Remaining is 0 (cannot eat)
    (0, 0, 0, [0, 0]),     # All zeros
    
    # Edge Cases: Boundaries (Max constraints)
    (1000, 1000, 1000, [2000, 0]), # Max constraints, exact match
    (1000, 1000, 0, [1000, 0]),    # Max constraints, no stock
    (0, 1000, 1000, [1000, 0]),    # Max need, max stock
    (1000, 0, 1000, [1000, 1000]), # Max initial, no need
    
    # Edge Cases: Negative Values
    # Testing how the function handles inputs outside the 0-1000 constraint
    (-1, 5, 10, [4, 5]),   # Negative initial eaten
    (5, -1, 10, [5, 10]),  # Negative need (should treat as eating 0)
    (5, 5, -1, [5, 0]),     # Negative stock (should treat as 0 available)
    (-5, -5, -5, [-5, 0]), # All negative
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with various scenarios including 
    sufficient stock, insufficient stock, boundary values, and negative inputs.
    """
    assert eat(number, need, remaining) == expected