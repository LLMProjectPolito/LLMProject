
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

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Boundary cases: Zeros
    (0, 0, 0, [0, 0]),
    (0, 10, 0, [0, 0]),
    (10, 0, 0, [10, 0]),
    (0, 0, 10, [0, 10]),
    (0, 5, 10, [5, 5]),
    (10, 0, 10, [10, 10]),
    (10, 5, 0, [10, 0]),
    (0, 5, 0, [0, 0]),
    (5, 0, 0, [5, 0]),
    (5, 0, 10, [5, 10]),
    
    # Boundary cases: Maximum constraints (1000)
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
    (0, 1000, 500, [500, 0]),
    
    # Scenarios: remaining > need
    (10, 5, 20, [15, 15]),
    (100, 1, 100, [101, 99]),
    (10, 1, 2, [11, 1]),
    (0, 1, 1000, [1, 999]),
    
    # Scenarios: remaining == need
    (50, 50, 50, [100, 0]),
    (0, 1, 1, [1, 0]),
    (5, 5, 5, [10, 0]),
    (10, 1, 1, [11, 0]),
    
    # Scenarios: remaining < need
    (10, 100, 50, [60, 0]),
    (0, 100, 1, [1, 0]),
    (5, 10, 0, [5, 0]),
    (5, 6, 5, [10, 0]),
    (10, 5, 2, [12, 0]),
    (5, 4, 5, [9, 1]),
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """Ensure the function returns a list of two integers."""
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)