
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
    (5, 6, 10, [11, 4]),   # Sufficient: 5 + 6 = 11, 10 - 6 = 4
    (4, 8, 9, [12, 1]),    # Sufficient: 4 + 8 = 12, 9 - 8 = 1
    (1, 10, 10, [11, 0]),  # Exact: 1 + 10 = 11, 10 - 10 = 0
    (2, 11, 5, [7, 0]),    # Insufficient: 2 + 5 = 7, 5 - 5 = 0
    
    # Edge Cases: Zeroes
    (0, 5, 10, [5, 5]),    # Zero already eaten
    (5, 0, 10, [5, 10]),   # Zero need
    (5, 6, 0, [5, 0]),     # Zero remaining
    (0, 0, 0, [0, 0]),     # All zero
    
    # Boundary Cases: Maximum Constraints (1000)
    (1000, 1000, 1000, [2000, 0]), # Max values, exact match
    (1000, 1000, 2000, [2000, 1000]), # Max values, sufficient (though remaining constraint is 1000, testing logic)
    (1000, 1000, 500, [1500, 0]),   # Max values, insufficient
    (0, 1000, 1000, [1000, 0]),     # Min eaten, max need/remaining
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with various scenarios including sufficient, 
    insufficient, and boundary conditions.
    """
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """
    Ensure the function returns a list of integers.
    """
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)