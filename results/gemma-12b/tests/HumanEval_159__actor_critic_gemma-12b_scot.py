
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
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


def test_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_zero_remaining():
    assert eat(1, 10, 0) == [1, 0]

def test_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_zero_eaten():
    assert eat(0, 6, 10) == [6, 4]

def test_all_zeros():
    assert eat(0, 0, 0) == [0, 0]

def test_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_need_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_need_one_greater_than_remaining():
    assert eat(2, 3, 2) == [4, 0]

def test_need_significantly_exceeds_remaining():
    assert eat(2, 6, 3) == [5, 0]

def test_number_exceeds_need():
    assert eat(6, 5, 10) == [11, 5]

def test_remaining_significantly_exceeds_need():
    assert eat(2, 3, 100) == [5, 97]

def test_negative_input_number():
    with pytest.raises(TypeError):
        eat(-1, 5, 10)

def test_negative_input_need():
    with pytest.raises(TypeError):
        eat(5, -1, 10)

def test_negative_input_remaining():
    with pytest.raises(TypeError):
        eat(5, 5, -1)