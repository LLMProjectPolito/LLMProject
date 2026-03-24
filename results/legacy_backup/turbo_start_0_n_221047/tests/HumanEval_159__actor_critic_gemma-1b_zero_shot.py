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
    remaining_after_meals = remaining - need
    return [total_eaten, remaining_after_meals]

def test_eat_example1():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_example2():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_example3():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_example4():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_example5():
    assert eat(0, 5, 10) == [0, 0]

def test_eat_example6():
    assert eat(1000, 1, 1) == [1000, 0]

def test_eat_example7():
    assert eat(500, 2, 1) == [500, 0]

def test_eat_example8():
    assert eat(1, 0, 10) == [10, 0]

def test_eat_example9():
    assert eat(0, 0, 10) == [0, 0]

def test_eat_example10():
    assert eat(100, 10, 1) == [110, 0]