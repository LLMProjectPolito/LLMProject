
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
def test_eat_sufficient_carrots():
    # Branch: remaining >= need
    assert eat(5, 6, 10) == [11, 4]
    assert eat(1, 10, 10) == [11, 0]

def test_eat_insufficient_carrots():
    # Branch: remaining < need
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 10, 0) == [0, 0]

# Focus: Boundary Values
import pytest

def test_eat_lower_boundaries():
    # All inputs at minimum constraint
    assert eat(0, 0, 0) == [0, 0]
    # Need is 0, remaining is 0
    assert eat(1000, 0, 0) == [1000, 0]

def test_eat_upper_boundaries():
    # All inputs at maximum constraint
    assert eat(1000, 1000, 1000) == [2000, 0]
    # Max number, max need, but 0 remaining
    assert eat(1000, 1000, 0) == [1000, 0]

def test_eat_exact_remaining_boundary():
    # Need exactly equals remaining
    assert eat(5, 10, 10) == [15, 0]
    # Need is exactly one more than remaining
    assert eat(5, 11, 10) == [15, 0]
    # Need is exactly one less than remaining
    assert eat(5, 9, 10) == [14, 1]

# Focus: Type Scenarios
def test_eat_minimum_boundaries():
    """Test with the minimum allowed integer values (0)."""
    assert eat(0, 0, 0) == [0, 0]

def test_eat_maximum_boundaries():
    """Test with the maximum allowed integer values (1000)."""
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_mixed_boundary_types():
    """Test with a mix of minimum and maximum boundary values."""
    assert eat(1000, 0, 1000) == [1000, 1000]