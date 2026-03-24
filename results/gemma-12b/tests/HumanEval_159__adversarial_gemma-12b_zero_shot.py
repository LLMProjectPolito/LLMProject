
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
    total_eaten = number
    remaining_carrots = remaining
    
    if remaining >= need:
        total_eaten += need
        remaining_carrots -= need
    else:
        total_eaten += remaining
        remaining_carrots = 0
        
    return [total_eaten, remaining_carrots]

class TestEat:
    def test_enough_carrots(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_not_enough_carrots(self):
        assert eat(4, 8, 9) == [12, 1]

    def test_exact_need(self):
        assert eat(1, 10, 10) == [11, 0]

    def test_less_remaining(self):
        assert eat(2, 11, 5) == [7, 0]

    def test_zero_initial_eaten(self):
        assert eat(0, 5, 10) == [5, 5]

    def test_zero_need(self):
        assert eat(5, 0, 10) == [5, 10]

    def test_zero_remaining(self):
        assert eat(5, 6, 0) == [5, 0]

    def test_large_numbers(self):
        assert eat(999, 999, 1000) == [1998, 1]

    def test_large_numbers_not_enough(self):
        assert eat(999, 1000, 1) == [1000, 0]

    def test_equal_need_and_remaining(self):
        assert eat(5, 5, 5) == [10, 0]

    def test_edge_case_zero_all(self):
        assert eat(0, 0, 0) == [0, 0]

    def test_number_at_max(self):
        assert eat(1000, 5, 10) == [1005, 5]

    def test_need_at_max(self):
        assert eat(5, 1000, 10) == [1005, 0]

    def test_remaining_at_max(self):
        assert eat(5, 6, 1000) == [11, 994]