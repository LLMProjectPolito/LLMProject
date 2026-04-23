
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
    
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining -= eaten
    
    return [total_eaten, remaining]

### Tests (Pytest):
import pytest

def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_need_less_than_remaining():
    assert eat(5, 1, 10) == [6, 9]

def test_eat_starting_zero():
    assert eat(0, 0, 10) == [0, 10]

def test_eat_upper_constraint():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_large_values():
    assert eat(500, 500, 500) == [1000, 0]

# Removed redundant test
# def test_eat_need_exceeds_remaining():
#     assert eat(10, 20, 5) == [15, 0]

def test_eat_need_is_zero():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_need_and_remaining_are_zero():
    assert eat(5, 0, 0) == [5, 0]

def test_eat_number_is_zero_need_positive_remaining_zero():
    assert eat(0, 5, 0) == [0, 0]

def test_eat_boundary_conditions():
    assert eat(999, 999, 999) == [1998, 0]
    assert eat(1, 1, 1) == [2, 0]