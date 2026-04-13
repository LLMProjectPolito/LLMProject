
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
        the number of remaining carrots that exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining -= eaten
    return [total_eaten, remaining]

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        (5, 0, 10, [5, 10]),
        (5, 6, 0, [5, 0]),
        (5, 5, 5, [10, 0]),
        (5, 10, 3, [8, 0]),
        (0, 5, 10, [5, 5]),
        (5, 0, 0, [5, 0]),
        (0, 5, 0, [0, 0]),
        (1000, 1000, 1000, [2000, 0]),
        (100, 100, 2000, [200, 1900]),
        (999, 999, 999, [1998, 0]),  # Large need and remaining
        (999, 1, 1, [1000, 0]), # Large initial, small need/remaining
    ],
)
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize(
    "number, need, remaining",
    [
        (-1, 5, 10),
        (5, -1, 10),
        (5, 5, -1),
        (1001, 5, 10),
        (5, 1001, 10),
        (5, 5, 1001)
    ]
)
def test_eat_negative_input(number, need, remaining):
    """Test with negative or out-of-range input to check for ValueError."""
    with pytest.raises(ValueError):
        eat(number, need, remaining)