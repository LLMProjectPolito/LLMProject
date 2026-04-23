
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
    total_eaten = number + need
    remaining = min(remaining + need, 1000)
    return [total_eaten, remaining]

import pytest

def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 0, 10) == [10, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_need_greater_than_remaining():
    assert eat(5, 10, 3) == [15, 0]
    assert eat(1, 10, 1) == [11, 0]

def test_eat_remaining_zero():
    assert eat(5, 6, 0) == [11, 0]
    assert eat(0, 0, 0) == [0, 0]

def test_eat_number_greater_than_remaining():
    assert eat(10, 5, 3) == [15, 0]
    assert eat(5, 10, 3) == [15, 0]

def test_eat_edge_case_zero_number():
    assert eat(0, 5, 10) == [5, 5]
    assert eat(0, 0, 0) == [0, 0]

def test_eat_edge_case_zero_remaining():
    assert eat(5, 6, 0) == [11, 0]
    assert eat(0, 0, 0) == [0, 0]

def test_eat_large_number():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_negative_number():
    assert eat(-1, 10, 10) == [9, 10] #Handles negative number gracefully
    assert eat(10, -1, 10) == [11, 0] #Handles negative number gracefully
    assert eat(10, 10, -1) == [20, 0] #Handles negative number gracefully

def test_eat_negative_number_need():
    assert eat(5, -6, 10) == [11, 4]
    assert eat(5, -10, 10) == [11, 0]

def test_eat_negative_number_remaining():
    assert eat(5, 6, -10) == [11, 4]
    assert eat(5, 6, -10) == [11, 4]

def test_eat_negative_number_all():
    assert eat(-5, -6, -10) == [11, 4]