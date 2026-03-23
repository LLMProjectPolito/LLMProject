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
    
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining -= eaten
    return [total_eaten, remaining]

def test_eat_basic1():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_basic2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_basic3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_basic4():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_no_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_exact_need():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_large_need():
    assert eat(100, 500, 200) == [300, 0]

def test_eat_large_remaining():
    assert eat(100, 50, 500) == [150, 450]

def test_eat_zero_initial():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 0) == [5, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_constrained_values():
    assert eat(500, 500, 500) == [1000, 0]

def test_eat_remaining_less_than_need():
    assert eat(10, 20, 5) == [15, 0]