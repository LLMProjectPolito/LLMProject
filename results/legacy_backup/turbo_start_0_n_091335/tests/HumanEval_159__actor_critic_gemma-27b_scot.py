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
        the number of remaining carrots that exist in stock
    
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

def test_normal_case():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_all_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_no_need_to_eat():
    assert eat(1, 10, 10) == [11, 0]

def test_zero_number():
    assert eat(0, 5, 10) == [5, 5]

def test_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_need_greater_than_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_need_equals_remaining():
    assert eat(3, 5, 5) == [8, 0]

def test_large_values():
    assert eat(500, 300, 200) == [800, 0]

def test_all_zeros():
    assert eat(0, 0, 0) == [0, 0]

def test_large_need_small_number():
    assert eat(1, 100, 200) == [101, 100]

def test_equal_number_and_need():
    assert eat(5, 5, 10) == [10, 5]