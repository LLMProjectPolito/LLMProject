
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
    # Provided Examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Edge Case: Zero values
    (0, 0, 0, [0, 0]),
    (0, 0, 10, [0, 10]),
    (0, 10, 0, [0, 0]),
    (10, 0, 0, [10, 0]),
    (10, 0, 10, [10, 10]),
    (10, 0, 20, [10, 20]),
    (0, 5, 0, [0, 0]),
    (0, 5, 10, [5, 5]),
    (0, 10, 5, [5, 0]),
    (5, 10, 0, [5, 0]),
    
    # Boundary Constraints: Maximum values (1000)
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
    
    # Logic Checks: Need vs Remaining
    (10, 5, 5, [15, 0]),
    (10, 6, 5, [15, 0]),
    (10, 4, 5, [14, 1]),
    (0, 5, 5, [5, 0]),
    (0, 10, 1, [1, 0]),
    (100, 100, 1, [101, 0]),
    (50, 100, 20, [70, 0]),
    (0, 1, 1000, [1, 999]),
    (1000, 1, 1000, [1001, 999]),
    (10, 1, 1, [11, 0]),
    (10, 1, 2, [11, 1]),
    (5, 10, 1, [6, 0]),
    (0, 1000, 500, [500, 0]),
    (1000, 1000, 2000, [2000, 1000]),
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """Ensure the function returns a list as specified."""
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2

def test_eat_large_values():
    """Test beyond constraints to ensure mathematical robustness."""
    assert eat(1000000, 1000000, 1000000) == [2000000, 0]