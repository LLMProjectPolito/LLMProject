
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
    total_eaten = number
    left = remaining
    
    if remaining >= need:
        total_eaten += need
        left -= need
    else:
        total_eaten += remaining
        left = 0
        
    return [total_eaten, left]

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (0, 0, 0, [0, 0]),
    (0, 5, 10, [5, 5]),
    (1000, 1000, 1000, [2000, 0]),
    (0, 1000, 0, [0, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (500, 500, 500, [1000, 0]),
    (100, 200, 100, [200, 0]),
    (200, 100, 100, [300, 0]),
    (0, 1, 1, [1, 0]),
    (1, 0, 1, [1, 1]),
    (1000, 1, 1, [1001, 0]),
    (1, 1000, 1, [1001, 0]),
    (500, 500, 500, [1000, 0]),
    # Edge case: need equals remaining
    (500, 500, 500, [1000, 0]),
    # Zero need
    (100, 0, 100, [100, 100]),
    # Zero number
    (0, 100, 100, [100, 0]),
    # Negative input tests - demonstrating current behavior (not ideal)
    (500, -100, 100, [400, 100]),  # Demonstrates that negative need is handled by subtraction
    (-100, 500, 100, [-100, 100]), # Demonstrates that negative number is handled by subtraction
    (-100, -100, 100, [0, 100]),   # Demonstrates that negative need and number are handled by subtraction
    (100, 100, -100, [200, 0]),    # Demonstrates that negative remaining is handled by subtraction
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected