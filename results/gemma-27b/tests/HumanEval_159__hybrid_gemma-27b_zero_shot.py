
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
    
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining_carrots = remaining - eaten
    
    return [total_eaten, remaining_carrots]

class TestEat:
    def test_basic_case1(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_basic_case2(self):
        assert eat(4, 8, 9) == [12, 1]

    def test_basic_case3(self):
        assert eat(1, 10, 10) == [11, 0]

    def test_basic_case4(self):
        assert eat(2, 11, 5) == [7, 0]

    def test_no_need(self):
        assert eat(5, 0, 10) == [5, 10]

    def test_no_remaining(self):
        assert eat(5, 6, 0) == [5, 0]

    def test_enough_remaining(self):
        assert eat(5, 6, 100) == [11, 94]

    def test_exactly_enough(self):
        assert eat(5, 6, 6) == [11, 0]

    def test_zero_initial_eaten(self):
        assert eat(0, 5, 10) == [5, 5]

    def test_zero_need(self):
        assert eat(5, 0, 0) == [5, 0]

    def test_large_numbers(self):
        assert eat(500, 500, 1000) == [1000, 500]

    def test_large_numbers_not_enough(self):
        assert eat(500, 600, 100) == [600, 0]

    def test_max_values(self):
        assert eat(1000, 1000, 1000) == [2000, 0]

    def test_edge_case_remaining_one(self):
        assert eat(5, 6, 1) == [6, 0]

    def test_edge_case_need_one(self):
        assert eat(5, 1, 10) == [6, 9]

    def test_need_equals_remaining(self):
        assert eat(5, 10, 10) == [15, 0]

    def test_number_equals_need(self):
        assert eat(10, 10, 10) == [20, 0]

    def test_all_zeros(self):
        assert eat(0, 0, 0) == [0, 0]

    def test_remaining_less_than_need(self):
        assert eat(2, 5, 3) == [5, 0]