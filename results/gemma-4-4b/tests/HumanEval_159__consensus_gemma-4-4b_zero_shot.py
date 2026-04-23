
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
    if remaining > 0:
        total_eaten += remaining
        remaining = 0
    else:
        total_eaten += 0
        remaining = 0
    return [total_eaten, remaining]

class TestEat:

    def test_example_1(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_example_2(self):
        assert eat(4, 8, 9) == [12, 1]

    def test_example_3(self):
        assert eat(1, 10, 10) == [11, 0]

    def test_example_4(self):
        assert eat(2, 11, 5) == [7, 0]

    def test_no_remaining(self):
        assert eat(5, 6, 0) == [11, 0]

    def test_all_remaining_eaten(self):
        assert eat(5, 6, 6) == [11, 0]

    def test_need_zero(self):
        assert eat(5, 0, 10) == [5, 10]

    def test_number_zero(self):
        assert eat(0, 6, 10) == [6, 4]

    def test_need_zero_remaining_zero(self):
        assert eat(5, 0, 0) == [5, 0]

    def test_large_numbers(self):
        assert eat(1000, 500, 2000) == [3500, 0]

    def test_edge_case_number_equals_need(self):
        assert eat(5, 5, 5) == [10, 0]

    def test_edge_case_remaining_equals_need(self):
        assert eat(5, 5, 5) == [10, 0]

    def test_edge_case_large_remaining(self):
        assert eat(1, 1, 1000) == [1002, 0]