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


class TestEat:
    def test_enough_remaining(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_not_enough_remaining(self):
        assert eat(4, 8, 9) == [13, 0]

    def test_zero_remaining(self):
        assert eat(1, 10, 0) == [1, 0]

    def test_zero_need(self):
        assert eat(5, 0, 10) == [5, 10]

    def test_zero_eaten(self):
        assert eat(0, 6, 10) == [6, 4]

    def test_all_zeros(self):
        assert eat(0, 0, 0) == [0, 0]

    def test_max_values(self):
        assert eat(1000, 1000, 1000) == [2000, 0]

    def test_large_need(self):
        assert eat(100, 1001, 200) == [1200, 0]

    def test_edge_case_need_equals_remaining(self):
        assert eat(5, 5, 5) == [10, 0]

    def test_edge_cases(self):
        assert eat(1, 1, 1) == [2, 0]
        assert eat(1, 1, 0) == [2, 0]
        assert eat(0, 1, 1) == [1, 0]

    def test_large_numbers(self):
        assert eat(999, 999, 1000) == [1998, 1]