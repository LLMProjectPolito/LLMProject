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
    total_eaten = number
    remaining_after_meals = remaining
    
    if remaining <= 0:
        return [total_eaten, 0]
    else:
        return [total_eaten, remaining - remaining]

def test_eat_example_1():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_example_2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_example_3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_example_4():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_empty():
    assert eat(5, 0, 10) == [11, 0]

def test_eat_large_need():
    assert eat(1000, 5, 5) == [105, 0]

def test_eat_large_remaining():
    assert eat(5, 1000, 1000) == [1050, 0]