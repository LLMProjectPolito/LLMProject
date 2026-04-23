
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
    if remaining >= need:
        return [total_eaten, remaining - need]
    else:
        return [total_eaten, remaining]

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        (0, 0, 10, [0, 10]),
        (1000, 1000, 1000, [2000, 0]),
        (0, 1, 0, [1, 0]),
        (1, 0, 0, [1, 0]),
        (100, 500, 100, [600, 0]),
        (500, 100, 500, [1000, 0]),
    ],
)
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (1, 1, 1, [2, 0]),
        (1, 1, 0, [2, 0]),
        (0, 1, 1, [1, 0]),
        (0, 1, 0, [1, 0]),
        (1, 0, 1, [1, 0]),
        (1, 0, 0, [1, 0]),
        (0, 0, 1, [0, 1]),
        (0, 0, 0, [0, 0]),
    ],
)
def test_eat_zero(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (1000, 1000, 1000, [2000, 0]),
        (1000, 1000, 0, [2000, 0]),
        (0, 1000, 1000, [1000, 0]),
        (1000, 0, 1000, [1000, 0]),
    ],
)
def test_eat_boundary(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected