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
    if remaining >= need - number:
        return [number + need, remaining - (need - number)]
    else:
        return [number + remaining, 0]

def test_sufficient_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_insufficient_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_no_carrots_needed():
    assert eat(5, 5, 10) == [10, 10]

def test_no_remaining_carrots():
    assert eat(5, 6, 0) == [5, 0]

def test_zero_initial_carrots():
    assert eat(0, 5, 10) == [5, 5]

def test_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_need_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_edge_case_1():
    assert eat(1, 10, 10) == [11, 0]

def test_edge_case_2():
    assert eat(2, 11, 5) == [7, 0]