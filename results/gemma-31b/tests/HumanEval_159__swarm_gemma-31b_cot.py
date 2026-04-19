
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
import math

def test_eat_no_need():
    # Case: The rabbit doesn't need to eat any more carrots, 
    # so the total eaten remains the same and all remaining carrots stay in stock.
    assert eat(10, 0, 5) == [10, 5]

def test_eat_no_carrots_available():
    # Tests the scenario where the rabbit needs carrots but the stock is completely empty.
    # number=10 (already eaten), need=5 (wants more), remaining=0 (none available)
    # Expected result: [10 + 0, 0] -> [10, 0]
    assert eat(10, 5, 0) == [10, 0]