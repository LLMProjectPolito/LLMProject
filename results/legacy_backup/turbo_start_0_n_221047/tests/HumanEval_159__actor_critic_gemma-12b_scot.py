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
    total_eaten = number + remaining
    remaining_after_eating = max(0, remaining - need)
    return [total_eaten, remaining_after_eating]

def test_sufficient_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_insufficient_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_no_additional_need():
    assert eat(1, 0, 5) == [1, 5]

def test_no_remaining_carrots():
    assert eat(2, 5, 0) == [2, 0]

def test_no_carrots_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_equal_need_and_remaining():
    assert eat(2, 5, 5) == [7, 0]

def test_large_numbers():
    assert eat(500, 600, 1000) == [1500, 0]

def test_zero_values():
    assert eat(0, 0, 0) == [0, 0]

def test_max_need_remaining():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_max_need_no_remaining():
    assert eat(0, 1000, 0) == [1000, 0]

def test_max_eaten_no_need():
    assert eat(1000, 0, 1000) == [1000, 1000]

def test_need_greater_than_number_plus_remaining():
    assert eat(5, 10, 2) == [7, 0]

def test_number_greater_than_need():
    assert eat(10, 5, 2) == [12, -3]

def test_negative_remaining_handled():
    assert eat(5, 10, 2) == [7, 0]