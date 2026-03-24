
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

def test_eat_boundary_remaining_zero():
    assert eat(10, 5, 0) == [10, 0]

def test_eat_boundary_need_zero():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_boundary_number_zero():
    assert eat(0, 5, 10) == [5, 5]

# Focus: Equivalence Partitioning
import pytest

def test_equivalence_partitioning_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]

def test_equivalence_partitioning_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]
    assert eat(10, 20, 5) == [15, 0]
    assert eat(100, 200, 50) == [150, 0]

def test_equivalence_partitioning_zero_values():
    assert eat(0, 0, 0) == [0, 0]
    assert eat(0, 5, 10) == [5, 5]
    assert eat(5, 0, 10) == [5, 10]
    assert eat(5, 5, 0) == [5, 0]

# Focus: Logic Branches
import pytest

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_all_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_needed_carrots():
    assert eat(1, 10, 10) == [11, 0]