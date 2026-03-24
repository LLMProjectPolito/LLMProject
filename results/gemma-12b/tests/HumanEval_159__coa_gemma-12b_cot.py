
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


# Focus: Boundary Values
def test_eat_boundary_need_equals_remaining():
    assert eat(5, 10, 10) == [20, 0]

def test_eat_boundary_need_slightly_greater_than_remaining():
    assert eat(2, 11, 10) == [22, 0]

def test_eat_boundary_number_equals_need():
    assert eat(5, 5, 10) == [10, 5]

# Focus: Type Scenarios
def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_more_carrots_than_needed():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

# Focus: Logic Branches
def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_remaining():
    assert eat(1, 10, 10) == [11, 0]