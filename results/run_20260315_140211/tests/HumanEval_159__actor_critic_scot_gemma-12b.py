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
    total_eaten = number + min(need, remaining)
    remaining_carrots = remaining - min(need, remaining)
    return [total_eaten, remaining_carrots]


class TestEat:
    def test_basic_case(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_remaining_less_than_need(self):
        assert eat(4, 8, 9) == [12, 1]

    def test_zero_number(self):
        assert eat(0, 10, 10) == [10, 0]

    def test_zero_need(self):
        assert eat(5, 0, 10) == [5, 10]

    def test_zero_remaining(self):
        assert eat(5, 6, 0) == [5, 0]

    def test_max_values(self):
        assert eat(1000, 1000, 1000) == [2000, 0]

    def test_large_numbers(self):
        assert eat(500, 750, 1200) == [1250, 200]

    def test_need_greater_than_max(self):
        assert eat(100, 1001, 500) == [1100, 0]

    def test_need_equals_number(self):
        assert eat(5, 5, 10) == [10, 5]

    def test_number_greater_than_need(self):
        assert eat(8, 5, 10) == [13, 2]

    def test_remaining_equals_need(self):
        assert eat(5, 5, 5) == [10, 0]

    def test_negative_inputs(self):
        with pytest.raises(ValueError):
            eat(-1, 5, 10)
        with pytest.raises(ValueError):
            eat(5, -1, 10)
        with pytest.raises(ValueError):
            eat(5, 5, -1)