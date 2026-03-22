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
    eaten = number + need
    left = remaining - eaten
    return [eaten, left]

def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_remaining():
    assert eat(0, 5, 0) == [5, 0]
    assert eat(5, 0, 0) == [5, 0]

def test_eat_enough_remaining():
    assert eat(10, 5, 20) == [15, 5]
    assert eat(1, 1, 1) == [2, 0]

def test_eat_not_enough_remaining():
    assert eat(0, 1, 1) == [1, 0]
    assert eat(1, 2, 1) == [3, 0]
    assert eat(5, 6, 2) == [11, 0]

def test_eat_edge_cases():
    assert eat(0, 0, 0) == [0, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(0, 1000, 1000) == [1000, 0]
    assert eat(1000, 0, 1000) == [1000, 0]
    assert eat(500, 500, 500) == [1000, 0]

def test_eat_large_numbers():
    assert eat(999, 999, 999) == [1998, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_zero_remaining():
    assert eat(5, 6, 0) == [11, 0]

def test_need_exceeds_remaining():
    assert eat(0, 5, 3) == [5, 0]

def test_number_is_zero():
    assert eat(0, 5, 10) == [5, 5]

def test_need_is_zero():
    assert eat(5, 0, 10) == [5, 5]

def test_number_equals_need():
    assert eat(3, 3, 10) == [6, 4]

def test_large_numbers():
    assert eat(999, 999, 999) == [1998, 0]

def test_remaining_equals_need():
    assert eat(1, 1, 1) == [2, 0]

def test_remaining_equals_number_plus_need():
    assert eat(1, 2, 3) == [3, 0]

def test_number_close_to_max_need_close_to_max_remaining_close_to_max():
    assert eat(998, 998, 998) == [1996, 2]

def test_edge_case_1():
    assert eat(0, 0, 10) == [0, 10]

def test_edge_case_2():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_edge_case_3():
    assert eat(500, 500, 500) == [1000, 0]