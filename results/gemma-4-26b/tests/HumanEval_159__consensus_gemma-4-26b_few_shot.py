
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
    
    # Edge cases: Zero values
    (0, 0, 0, [0, 0]),
    (10, 0, 10, [10, 10]),
    (10, 5, 0, [10, 0]),
    (0, 5, 5, [5, 0]),
    (0, 10, 0, [0, 0]),
    (0, 0, 10, [0, 10]),
    
    # Edge cases: Need vs Remaining
    (5, 2, 10, [7, 8]),     # need < remaining
    (5, 5, 5, [10, 0]),     # need == remaining
    (5, 10, 5, [10, 0]),    # need > remaining
    (5, 15, 10, [15, 0]),   # need > remaining (eat all)
    
    # Boundary Constraints
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 500, 500, [1500, 0]),
    (0, 0, 1, [0, 1]),
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with various scenarios including provided examples,
    edge cases involving zeros, and boundary conditions.
    """
    assert eat(number, need, remaining) == expected

def test_eat_types():
    """
    Ensures the function returns a list of two integers.
    """
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)