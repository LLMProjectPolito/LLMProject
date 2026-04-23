
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
    """
    if number < 0 or need < 0 or remaining < 0:
        raise ValueError("Inputs must be non-negative.")

    actual_to_eat = min(need, remaining)
    total_eaten = number + actual_to_eat
    leftover = remaining - actual_to_eat
    return [total_eaten, leftover]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided Examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Edge Case: All zeros
    (0, 0, 0, [0, 0]),
    
    # Edge Case: No need to eat more
    (5, 0, 10, [5, 10]),
    (5, 0, 0, [5, 0]),
    
    # Edge Case: No carrots remaining in stock
    (5, 10, 0, [5, 0]),
    (0, 10, 0, [0, 0]),
    
    # Edge Case: Need exactly matches remaining
    (0, 5, 5, [5, 0]),
    
    # Edge Case: Need is much greater than remaining (Hungry rabbit)
    (10, 100, 5, [15, 0]),
    
    # Edge Case: Need is much less than remaining
    (10, 2, 100, [12, 98]),
    
    # Edge Case: Maximum constraints
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
])
def test_eat(number, need, remaining, expected):
    """
    Tests the eat function with various scenarios. 
    By converting the result to a list, we test the behavior (values) 
    rather than the specific container type (list vs tuple), making the test less brittle.
    """
    assert list(eat(number, need, remaining)) == expected

@pytest.mark.parametrize("number, need, remaining", [
    (-1, 5, 5),
    (5, -1, 5),
    (5, 5, -1),
    (-1, -1, -1),
])
def test_eat_negative_inputs(number, need, remaining):
    """
    Ensures that negative inputs raise a ValueError as per business logic requirements.
    """
    with pytest.raises(ValueError):
        eat(number, need, remaining)