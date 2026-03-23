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
    remaining_carrots = remaining - eaten
    return [total_eaten, remaining_carrots]

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_no_carrots_needed():
    assert eat(2, 0, 5) == [2, 5]

def test_eat_no_carrots_remaining():
    assert eat(2, 11, 0) == [2, 0]

def test_eat_zero_initial_eaten():
    assert eat(0, 5, 7) == [5, 2]

def test_eat_large_numbers():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_large_numbers_not_enough():
    assert eat(500, 700, 300) == [800, 0]

def test_eat_need_more_than_remaining():
    assert eat(2, 11, 5) == [7, 0]