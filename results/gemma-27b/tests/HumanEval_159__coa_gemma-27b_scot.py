import pytest
import math


# Focus: Boundary Values
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
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining_carrots = remaining - eaten
    return [total_eaten, remaining_carrots]

@pytest.mark.parametrize("number, need, remaining, expected", [
    (0, 0, 0, [0, 0]),  # All boundaries at zero
    (1000, 1000, 1000, [2000, 0]),  # All boundaries at max
    (0, 1000, 0, [0, 0]),  # number=0, need=max, remaining=0
    (0, 0, 1000, [0, 1000]),  # number=0, need=0, remaining=max
    (1000, 0, 1000, [1000, 1000]),  # number=max, need=0, remaining=max
    (0, 1000, 500, [500, 0]),  # need > remaining
    (500, 1000, 0, [500, 0]),  # remaining = 0
    (1000, 1, 1, [1001, 0]), # number=max, need=min, remaining=min
])
def test_boundary_values(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

# Focus: Equivalence Partitioning
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
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining_carrots = remaining - eaten
    return [total_eaten, remaining_carrots]

# STEP 2: PLAN - List test functions names and scenarios.
# Test function 1: Enough remaining carrots to satisfy need
# Test function 2: Not enough remaining carrots, but some are eaten
# Test function 3: No remaining carrots

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),  # Enough remaining
    (4, 8, 9, [12, 1]),   # Enough remaining
    (1, 10, 10, [11, 0]), # Exactly enough
    (2, 11, 5, [7, 0]),   # Not enough, all eaten
    (0, 0, 0, [0, 0]),    # Zero values
    (100, 50, 200, [150, 150]), # Larger values within constraints
    (500, 600, 100, [600, 0]), # Need > remaining
    (999, 1, 1, [1000, 0]), # Max number, small need/remaining
])
def test_equivalence_partitioning(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

# Focus: Logic Branches
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
    if remaining >= need - number:
        return [number + need, remaining - (need - number)]
    else:
        return [number + remaining, 0]

def test_eat_enough_carrots():
    """Test case where there are enough carrots to satisfy the need."""
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    """Test case where there are not enough carrots to satisfy the need."""
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_carrots():
    """Test case where the remaining carrots are exactly enough to satisfy the need."""
    assert eat(1, 10, 10) == [11, 0]