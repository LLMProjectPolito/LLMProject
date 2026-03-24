
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
    
    eaten = number
    
    if remaining >= need - number:
        eaten += need - number
        remaining -= (need - number)
    else:
        eaten += remaining
        remaining = 0
        
    return [eaten, remaining]

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 5, 2) == [2, 0]
    assert eat(10, 20, 5) == [15, 0]

def test_eat_no_carrots_needed():
    assert eat(5, 5, 10) == [5, 10]
    assert eat(10, 10, 0) == [10, 0]

def test_eat_no_remaining_carrots():
    assert eat(5, 6, 0) == [5, 0]
    assert eat(10, 10, 0) == [10, 0]

def test_eat_zero_initial_carrots():
    assert eat(0, 5, 10) == [5, 5]
    assert eat(0, 10, 5) == [5, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]
    assert eat(10, 0, 0) == [10, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(0, 1000, 1000) == [1000, 0]
    assert eat(1000, 0, 1000) == [1000, 1000]

def test_eat_edge_cases():
    assert eat(5, 5, 1) == [6, 0]
    assert eat(1, 2, 1) == [2, 0]
    assert eat(999, 1000, 1) == [1000, 0]