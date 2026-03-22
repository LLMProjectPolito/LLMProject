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

### STEP 1: REASONING
# The function `eat` calculates the total carrots eaten and the remaining carrots after eating.
# It handles the case where there are not enough carrots to satisfy the need.
# We need to test various scenarios with different inputs to ensure the function works correctly.
# Test cases should cover:
# 1. Sufficient carrots to meet the need.
# 2. Not enough carrots to meet the need (eat all remaining).
# 3. Zero values for inputs.
# 4. Edge cases (e.g., need is larger than remaining).

### STEP 2: PLAN
# Test functions:
# - test_eat_sufficient_carrots
# - test_eat_not_enough_carrots
# - test_eat_zero_values
# - test_eat_edge_case

### STEP 3: CODE
def test_eat_sufficient_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

def test_eat_not_enough_carrots():
    assert eat(5, 6, 3) == [11, 0]
    assert eat(1, 2, 1) == [3, 0]

def test_eat_zero_values():
    assert eat(0, 0, 0) == [0, 0]
    assert eat(0, 5, 10) == [5, 10]
    assert eat(5, 0, 10) == [5, 10]

def test_eat_edge_case():
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(1000, 1001, 1000) == [2001, 0]
    assert eat(0, 1000, 1000) == [1000, 0]