
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
    total_eaten = number + need
    remaining_after_meal = remaining - need
    if remaining_after_meal < 0:
        remaining_after_meal = 0
    return [total_eaten, remaining_after_meal]

def test_eat_basic_case_1():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_basic_case_2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_basic_case_3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_basic_case_4():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_number():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [11, 0]

def test_eat_all_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_remaining_less_than_need():
    assert eat(5, 10, 3) == [15, 0]

def test_eat_large_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_number_at_max():
    assert eat(1000, 5, 1000) == [1005, 0]

def test_eat_need_at_max():
    assert eat(5, 1000, 1000) == [1005, 0]

def test_eat_remaining_at_max():
    assert eat(5, 6, 1000) == [11, 994]

def test_eat_need_greater_than_remaining():
    assert eat(5, 10, 3) == [15, 0]

def test_eat_number_and_need_greater_than_remaining():
    assert eat(5, 10, 3) == [15, 0]

def test_eat_negative_number():
    assert eat(-5, 6, 10) == [1, 4]

def test_eat_negative_need():
    assert eat(5, -6, 10) == [1, 4]

def test_eat_negative_remaining():
    assert eat(5, 6, -10) == [11, 0]

def test_eat_negative_number_and_need():
    assert eat(-5, -6, 10) == [1, 4]

def test_eat_negative_number_and_remaining():
    assert eat(-5, 6, -10) == [1, 0]

def test_eat_negative_need_and_remaining():
    assert eat(5, -6, -10) == [11, 0]