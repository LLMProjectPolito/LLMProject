
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
    if number < 0 or need < 0 or remaining < 0:
        raise ValueError("Inputs must be non-negative")
    if number > 1000 or need > 1000 or remaining > 1000:
        raise ValueError("Inputs must be less than or equal to 1000")

    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


class TestEat:
    def test_enough_carrots(self):
        assert eat(5, 6, 10) == [11, 4]
        assert eat(4, 8, 9) == [12, 1]
        assert eat(1, 10, 10) == [11, 0]

    def test_not_enough_carrots(self):
        assert eat(2, 11, 5) == [7, 0]
        assert eat(0, 5, 2) == [2, 0]
        assert eat(100, 200, 50) == [150, 0]

    def test_zero_values(self):
        assert eat(0, 0, 0) == [0, 0]
        assert eat(0, 5, 0) == [5, 0]
        assert eat(5, 0, 0) == [5, 0]

    def test_edge_cases(self):
        assert eat(1000, 1000, 1000) == [2000, 0]
        assert eat(0, 1000, 0) == [1000, 0]
        assert eat(1000, 0, 1000) == [1000, 1000]

    def test_large_values(self):
        assert eat(999, 999, 999) == [1998, 0]
        assert eat(100, 500, 200) == [600, 0]

    def test_type_checking(self):
        with pytest.raises(ValueError):
            eat("5", 6, 10)
        with pytest.raises(ValueError):
            eat(5, "6", 10)
        with pytest.raises(ValueError):
            eat(5, 6, "10")
        with pytest.raises(ValueError):
            eat(5.5, 6, 10)
        with pytest.raises(ValueError):
            eat(5, 6.5, 10)
        with pytest.raises(ValueError):
            eat(5, 6, 10.5)

    def test_negative_values(self):
        with pytest.raises(ValueError):
            eat(-5, 6, 10)
        with pytest.raises(ValueError):
            eat(5, -6, 10)
        with pytest.raises(ValueError):
            eat(5, 6, -10)

    def test_constraint_validation(self):
        with pytest.raises(ValueError):
            eat(1001, 6, 10)
        with pytest.raises(ValueError):
            eat(5, 1001, 10)
        with pytest.raises(ValueError):
            eat(5, 6, 1001)