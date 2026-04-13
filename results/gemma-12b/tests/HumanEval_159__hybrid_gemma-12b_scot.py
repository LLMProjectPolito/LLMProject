
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
    remaining_carrots = remaining
    
    if remaining_carrots >= need:
        total_eaten += need
        remaining_carrots -= need
    else:
        total_eaten += remaining_carrots
        remaining_carrots = 0
    
    return [total_eaten, remaining_carrots]


def test_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_zero_remaining():
    assert eat(1, 10, 0) == [1, 0]

def test_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_zero_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_edge_case_equal_need_remaining():
    assert eat(2, 5, 5) == [7, 0]

def test_large_numbers():
    assert eat(500, 600, 1000) == [1100, 400]

def test_all_zeros():
    assert eat(0, 0, 0) == [0, 0]

def test_need_greater_than_max():
    assert eat(100, 1100, 500) == [600, 0]

def test_remaining_greater_than_max():
    assert eat(100, 100, 1100) == [200, 1000]

def test_zero_remaining_suite2():
    assert eat(1, 10, 0) == [1, 0]

def test_zero_need_suite2():
    assert eat(5, 0, 10) == [5, 10]

def test_zero_eaten_suite2():
    assert eat(0, 6, 10) == [6, 4]

def test_all_zeros_suite2():
    assert eat(0, 0, 0) == [0, 0]

def test_large_numbers_suite2():
    assert eat(500, 600, 1000) == [1100, 400]

def test_edge_cases_suite2():
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(0, 0, 1000) == [0, 1000]
    assert eat(1000, 0, 0) == [1000, 0]
    assert eat(0, 1000, 0) == [0, 0]