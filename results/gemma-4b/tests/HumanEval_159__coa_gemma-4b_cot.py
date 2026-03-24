
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
import pytest

def test_eat_zero_number():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_max_number():
    assert eat(1000, 5, 10) == [1000, 0]

def test_eat_need_zero():
    assert eat(5, 0, 10) == [5, 10]

# Focus: Type Scenarios
import pytest

def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining():
    assert eat(2, 11, 5) == [7, 0]

# Focus: Logic Branches
import pytest

def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_eat_all_remaining_2():
    assert eat(2, 11, 5) == [7, 0]