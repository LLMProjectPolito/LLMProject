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
    eaten = number + need
    left = remaining - eaten
    return [eaten, left]

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `eat` calculates the total carrots eaten and the remaining carrots after eating.
# It handles the case where there are not enough carrots to satisfy the need.
# The function should return a list containing the total eaten carrots and the remaining carrots.
# Edge cases include:
#   - Need is greater than remaining carrots.
#   - Number of carrots eaten is zero.
#   - Need is zero.
#   - Remaining carrots is zero.

# STEP 2: PLAN - List test functions names and scenarios.
# test_eat_basic_case() - Tests a simple case where there are enough carrots.
# test_eat_not_enough_carrots() - Tests the case where there are not enough carrots.
# test_eat_zero_need() - Tests the case where the need is zero.
# test_eat_zero_remaining() - Tests the case where the remaining carrots are zero.
# test_eat_large_numbers() - Tests with large numbers to ensure no overflow issues.
# test_eat_number_equals_need() - Tests when the number of carrots eaten equals the need.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_eat_basic_case():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [11, 0]

def test_eat_large_numbers():
    assert eat(999, 500, 1000) == [1499, 0]

def test_eat_number_equals_need():
    assert eat(5, 5, 10) == [10, 5]

def test_eat_need_greater_than_remaining():
    assert eat(0, 10, 5) == [10, 0]

def test_eat_number_is_zero():
    assert eat(0, 5, 10) == [5, 5]