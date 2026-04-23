
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
    Returns a list containing the total carrots eaten and the remaining carrots.
    
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
    
    eat_amount = min(need - number, remaining)
    total_eaten = number + eat_amount
    remaining_carrots = remaining - eat_amount
    
    return [total_eaten, remaining_carrots]

def test_sufficient_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]

def test_insufficient_carrots():
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 5, 2) == [2, 0]
    assert eat(10, 20, 5) == [15, 0]

def test_no_need():
    assert eat(5, 5, 10) == [5, 10]
    assert eat(10, 10, 5) == [10, 5]

def test_no_remaining():
    assert eat(5, 6, 0) == [5, 0]
    assert eat(10, 15, 0) == [10, 0]

def test_initial_eaten_is_zero():
    assert eat(0, 5, 10) == [5, 5]
    assert eat(0, 10, 5) == [5, 0]

def test_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(999, 1, 1) == [1000, 0]
    assert eat(1000, 500, 500) == [1500, 0]

def test_edge_cases():
    assert eat(0, 0, 0) == [0, 0]

def test_negative_need():
    assert eat(5, -1, 10) == [5, 10]

def test_negative_number():
    assert eat(-5, 6, 10) == [1, 10]

def test_negative_remaining():
    assert eat(5, 6, -10) == [5, -10]

def test_small_remaining():
    assert eat(100, 200, 1) == [101, 0]

def test_large_need_minus_number_small_remaining():
    assert eat(1, 1001, 1) == [2, 0]