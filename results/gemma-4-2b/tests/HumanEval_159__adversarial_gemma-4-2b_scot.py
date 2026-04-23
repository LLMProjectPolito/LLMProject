
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
    total_eaten = number + need
    carrots_left = remaining - need
    return [total_eaten, carrots_left]

class TestEat:

    def test_basic_case(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_need_more_than_remaining(self):
        assert eat(4, 8, 9) == [12, 1]

    def test_exactly_enough_carrots(self):
        assert eat(1, 10, 10) == [11, 0]

    def test_need_more_than_remaining_edge_case(self):
        assert eat(2, 11, 5) == [7, 0]

    def test_zero_remaining(self):
        assert eat(1, 5, 0) == [6, 0]

    def test_zero_need(self):
        assert eat(5, 0, 10) == [5, 10]

    def test_negative_need(self):
        assert eat(5, -1, 10) == [4, 10]

    def test_negative_remaining(self):
        assert eat(5, 6, -10) == [11, -1]

    def test_large_numbers(self):
        assert eat(1000, 1000, 1000) == [2000, 0]

    def test_small_numbers(self):
        assert eat(1, 1, 1) == [2, 0]