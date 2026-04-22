
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
    # Docstring examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Edge Case: Zeros
    (0, 0, 0, [0, 0]),
    (5, 0, 10, [5, 10]),
    (5, 0, 0, [5, 0]),
    (5, 10, 0, [5, 0]),
    (0, 5, 10, [5, 5]),
    (10, 0, 10, [10, 10]),
    (10, 10, 0, [10, 0]),
    (0, 10, 0, [0, 0]),
    (0, 5, 5, [5, 0]),
    (5, 5, 0, [5, 0]),
    (0, 5, 0, [0, 0]),
    
    # Logic: Need < Remaining
    (5, 5, 10, [10, 5]),
    (5, 2, 10, [7, 8]),
    (50, 25, 100, [75, 75]),
    (10, 5, 20, [15, 15]),
    (500, 250, 750, [750, 500]),
    
    # Logic: Need == Remaining
    (5, 10, 10, [15, 0]),
    (10, 5, 5, [15, 0]),
    
    # Logic: Need > Remaining
    (5, 20, 10, [15, 0]),
    (5, 20, 5, [10, 0]),
    (5, 20, 0, [5, 0]),
    (50, 100, 25, [75, 0]),
    (50, 50, 25, [75, 0]),
    (10, 5, 2, [12, 0]),
    
    # Boundary Constraints (Max values)
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
    (0, 0, 1000, [0, 1000]),
    (500, 500, 500, [1000, 0]),
    
    # Mixed boundary values
    (1000, 1, 1, [1001, 0]),
    (1, 1000, 1, [2, 0]),
    (1, 1, 1000, [2, 999]),
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with a comprehensive set of scenarios including:
    - Docstring examples
    - Zero values for all parameters
    - Scenarios where need > remaining (hunger case)
    - Scenarios where need <= remaining
    - Boundary conditions for the constraints (0 and 1000)
    """
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """Ensures the function returns a list of two integers."""
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)