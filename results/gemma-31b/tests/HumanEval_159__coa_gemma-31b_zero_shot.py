
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


# Focus: Logic Branches
def test_eat_enough_carrots():
    # Branch: remaining >= need
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    # Branch: remaining < need
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_carrots():
    # Boundary: remaining == need
    assert eat(1, 10, 10) == [11, 0]

# Focus: Boundary Values
import pytest

def test_eat_min_boundaries():
    # All inputs at minimum constraint (0)
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_boundaries():
    # All inputs at maximum constraint (1000)
    # Rabbit eats all 1000 remaining carrots
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_exact_boundary():
    # Need is exactly equal to remaining
    assert eat(0, 500, 500) == [500, 0]

# Focus: Type Scenarios
def test_eat_integer_types():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 0, 0) == [0, 0]

def test_eat_float_types():
    assert eat(5.0, 6.0, 10.0) == [11.0, 4.0]
    assert eat(2.0, 11.0, 5.0) == [7.0, 0.0]
    assert eat(1.5, 2.5, 5.0) == [4.0, 2.5]

def test_eat_mixed_types():
    assert eat(5, 6.5, 10) == [11.5, 3.5]
    assert eat(5.5, 6, 10.2) == [11.5, 4.2]
    assert eat(2, 11.5, 5) == [7, 0]