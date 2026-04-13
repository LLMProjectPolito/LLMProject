
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

def test_eat_sufficient_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_insufficient_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exact_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_very_insufficient_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_equal_need_remaining():
    assert eat(3, 7, 7) == [10, 0]

def test_eat_large_numbers():
    assert eat(999, 1000, 1000) == [1999, 0]

def test_eat_large_numbers_insufficient():
    assert eat(500, 1000, 200) == [700, 0]

def test_eat_all_carrots_and_still_hungry():
    assert eat(100, 200, 150) == [250, 0]

def test_eat_edge_case_zero_all():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_number_equal_need_equal_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_number_greater_than_need():
    assert eat(10, 5, 10) == [15, 5]

def test_eat_number_greater_than_need_and_remaining():
    assert eat(15, 5, 10) == [20, 0]