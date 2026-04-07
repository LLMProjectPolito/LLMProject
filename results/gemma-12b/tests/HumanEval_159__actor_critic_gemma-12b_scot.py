
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
    total_eaten = number + remaining
    remaining_after_eating = max(0, total_eaten - need)
    return [total_eaten, remaining_after_eating]


def test_enough_carrots():
    assert eat(5, 6, 10) == [15, 4]

def test_insufficient_carrots():
    assert eat(4, 8, 9) == [13, 5]

def test_need_greater_than_remaining_less_than_number():
    assert eat(5, 8, 2) == [7, 0]

def test_no_carrots_remaining():
    assert eat(1, 10, 0) == [1, 0]

def test_no_need():
    assert eat(5, 0, 10) == [15, 10]

def test_no_carrots_eaten():
    assert eat(0, 10, 10) == [10, 0]

def test_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_min_values():
    assert eat(0, 0, 0) == [0, 0]

def test_need_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_large_numbers():
    assert eat(500, 600, 700) == [1200, 100]

def test_large_remaining_small_need():
    assert eat(2, 1, 1000) == [1002, 999]

def test_insufficient_carrots_2():
    assert eat(1, 5, 2) == [3, 0]