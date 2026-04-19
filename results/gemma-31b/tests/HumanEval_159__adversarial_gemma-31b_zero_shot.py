
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
    Implementation of the rabbit carrot eating logic.
    """
    eaten_now = min(need, remaining)
    total_eaten = number + eaten_now
    left_over = remaining - eaten_now
    return [total_eaten, left_over]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided Examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Boundary Cases: Zeros
    (0, 0, 0, [0, 0]),       # Everything zero
    (0, 10, 10, [10, 0]),    # Start with 0 eaten
    (10, 0, 10, [10, 10]),   # Need 0 carrots
    (10, 10, 0, [10, 0]),    # No carrots remaining in stock
    
    # Boundary Cases: Maximums (Constraint 1000)
    (1000, 1000, 1000, [2000, 0]), # Max values, need met
    (1000, 1000, 0, [1000, 0]),    # Max values, no stock
    (0, 1000, 1000, [1000, 0]),    # Max need and stock
    
    # Edge Cases: Need vs Remaining
    (5, 1, 10, [6, 9]),     # Need is much less than remaining
    (5, 100, 10, [15, 0]),  # Need is much more than remaining
    (5, 10, 10, [15, 0]),   # Need is exactly equal to remaining
    
    # Large values within constraints
    (500, 500, 500, [1000, 0]),
    (100, 200, 300, [300, 100]),
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function against various scenarios including 
    provided examples, boundary values, and edge cases.
    """
    assert eat(number, need, remaining) == expected

def test_return_type():
    """
    Ensure the function returns a list of integers.
    """
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)