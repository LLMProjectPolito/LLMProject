
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
    
    if remaining >= need - number:
        return [number + need - number, remaining - (need - number)]
    else:
        return [number + remaining, 0]

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 5, 2) == [2, 0]
    assert eat(10, 20, 5) == [15, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]
    assert eat(0, 0, 0) == [0, 0]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]
    assert eat(0, 5, 0) == [0, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(500, 500, 500) == [1000, 0]
    assert eat(0, 1000, 1000) == [1000, 0]

def test_eat_edge_cases():
    assert eat(0, 1, 1) == [1, 0]
    assert eat(1, 1, 0) == [1, 0]
    assert eat(1, 2, 1) == [2, 0]
    assert eat(1, 2, 2) == [3, 0]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_more_than_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_no_carrots_eaten_initially():
    assert eat(0, 5, 7) == [5, 2]

def test_no_carrots_needed():
    assert eat(5, 0, 10) == [5, 10]

def test_no_remaining_carrots():
    assert eat(5, 6, 0) == [5, 0]

def test_zero_values():
    assert eat(0, 0, 0) == [0, 0]

def test_large_values():
    assert eat(100, 200, 300) == [300, 100]

def test_edge_case_number_equals_need():
    assert eat(5, 5, 10) == [10, 5]

def test_edge_case_need_equals_remaining():
    assert eat(5, 10, 10) == [15, 0]

def test_number_greater_than_need():
    assert eat(7, 5, 10) == [12, 5]

def test_remaining_equals_zero_and_need_greater_than_number():
    assert eat(2, 5, 0) == [2, 0]

def test_remaining_equals_zero_and_need_less_than_number():
    assert eat(5, 2, 0) == [5, 0]