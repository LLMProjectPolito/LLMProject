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
# The input parameters are number, need, and remaining, all integers between 0 and 1000.

# STEP 2: PLAN - List test functions names and scenarios.
# test_eat_basic_case() - Tests a simple case where there are enough carrots.
# test_eat_not_enough_carrots() - Tests a case where there are not enough carrots.
# test_eat_all_carrots_eaten() - Tests a case where all carrots are eaten.
# test_eat_zero_need() - Tests a case where the need is zero.
# test_eat_zero_remaining() - Tests a case where the remaining carrots are zero.
# test_eat_large_numbers() - Tests with larger numbers to ensure no overflow issues.

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_eat_basic_case():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_carrots_eaten():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_zero_need():
    assert eat(2, 0, 5) == [2, 3]

def test_eat_zero_remaining():
    assert eat(0, 5, 0) == [5, 0]

def test_eat_large_numbers():
    assert eat(999, 500, 1000) == [1499, 0]

def test_eat_edge_case_need_equals_remaining():
    assert eat(0, 5, 5) == [5, 0]

def test_eat_edge_case_number_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_edge_case_all_zero():
    assert eat(0, 0, 0) == [0, 0]