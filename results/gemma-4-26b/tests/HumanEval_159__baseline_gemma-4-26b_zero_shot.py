
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

    # Edge Case: All zeros
    (0, 0, 0, [0, 0]),

    # Edge Case: Need is zero (no more eating required)
    (5, 0, 10, [5, 10]),
    (0, 0, 10, [0, 10]),

    # Edge Case: Remaining is zero (nothing left to eat)
    (5, 10, 0, [5, 0]),
    (0, 10, 0, [0, 0]),

    # Edge Case: Need is greater than remaining (eat all remaining)
    (0, 10, 5, [5, 0]),
    (10, 50, 25, [35, 0]),

    # Edge Case: Need is exactly equal to remaining
    (5, 10, 10, [15, 0]),
    (0, 10, 10, [10, 0]),

    # Edge Case: Need is less than remaining
    (5, 5, 10, [10, 5]),

    # Constraint Boundaries: Max values (1000)
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
    (1000, 500, 200, [1700, 0]),
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with a variety of scenarios:
    - Standard cases from the problem description.
    - Boundary cases (zeros, max constraints).
    - Scenarios where need > remaining.
    - Scenarios where need < remaining.
    - Scenarios where need == remaining.
    """
    assert eat(number, need, remaining) == expected