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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function 'eat' calculates the total carrots eaten and remaining carrots after a rabbit eats.
# Equivalence partitioning focuses on dividing the input domain into partitions where the function behaves similarly.
# Key partitions:
# 1. remaining >= need: Rabbit eats all it needs.
# 2. remaining < need: Rabbit eats all remaining.
# 3. need = 0: Rabbit doesn't need to eat more.
# 4. remaining = 0: No carrots to eat.

# STEP 2: PLAN - List test functions names and scenarios.
# Test function 1: 'test_eat_remaining_greater_than_need' - Tests the case where remaining carrots are more than needed.
# Test function 2: 'test_eat_remaining_less_than_need' - Tests the case where remaining carrots are less than needed.
# Test function 3: 'test_eat_need_zero' - Tests the case where the rabbit doesn't need to eat more carrots.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_eat_remaining_greater_than_need():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(0, 5, 10) == [5, 5]
    assert eat(10, 2, 5) == [12, 3]

def test_eat_remaining_less_than_need():
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 5) == [6, 0]
    assert eat(100, 200, 50) == [150, 0]

def test_eat_need_zero():
    assert eat(1, 0, 10) == [1, 10]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(50, 0, 50) == [50, 50]

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

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (0, 5, 5, [5, 0]),  # Edge case: number is 0
    (5, 5, 0, [5, 0]),  # Edge case: remaining is 0
    (5, 10, 10, [15, 0]), # Need more than remaining
    (10, 5, 10, [15, 5]), # Need less than remaining
    (100, 200, 50, [150, 0]), # Larger numbers
    (500, 500, 1000, [1000, 500]), # Larger numbers, sufficient remaining
])
def test_eat_logic_branches(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected