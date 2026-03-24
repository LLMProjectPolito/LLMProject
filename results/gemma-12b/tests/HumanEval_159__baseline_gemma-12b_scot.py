
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

    Have fun :)
    """
    total_eaten = number + remaining
    remaining_after_meal = 0
    if remaining >= need:
        remaining_after_meal = remaining - need
    else:
        remaining_after_meal = 0
    return [total_eaten, remaining_after_meal]

# STEP 1: REASONING
# The function `eat` calculates the total number of carrots eaten and the number of carrots remaining after a rabbit eats some carrots.
# The constraints are 0 <= number <= 1000, 0 <= need <= 1000, and 0 <= remaining <= 1000.
# We need to test various scenarios, including:
#   - Enough remaining carrots to meet the need.
#   - Not enough remaining carrots to meet the need (eat all remaining).
#   - Edge cases with zero values for input parameters.
#   - Boundary conditions for the input constraints.

# STEP 2: PLAN
# Test functions:
#   - test_enough_carrots: Enough remaining carrots to meet the need.
#   - test_not_enough_carrots: Not enough remaining carrots to meet the need.
#   - test_zero_carrots_eaten: Number of carrots eaten is zero.
#   - test_zero_carrots_needed: Number of carrots needed is zero.
#   - test_zero_carrots_remaining: Number of carrots remaining is zero.
#   - test_boundary_carrots_eaten: Number of carrots eaten is at the upper boundary (1000).
#   - test_boundary_carrots_needed: Number of carrots needed is at the upper boundary (1000).
#   - test_boundary_carrots_remaining: Number of carrots remaining is at the upper boundary (1000).
#   - test_all_zero_values: All input values are zero.
#   - test_large_values: Test with large values close to the upper boundary.

# STEP 3: CODE
class TestEat:
    def test_enough_carrots(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_not_enough_carrots(self):
        assert eat(4, 8, 9) == [13, 0]

    def test_zero_carrots_eaten(self):
        assert eat(0, 10, 10) == [10, 0]

    def test_zero_carrots_needed(self):
        assert eat(5, 0, 10) == [5, 10]

    def test_zero_carrots_remaining(self):
        assert eat(5, 6, 0) == [5, 0]

    def test_boundary_carrots_eaten(self):
        assert eat(1000, 5, 10) == [1015, 5]

    def test_boundary_carrots_needed(self):
        assert eat(5, 1000, 1000) == [2005, 0]

    def test_boundary_carrots_remaining(self):
        assert eat(5, 6, 1000) == [1005, 994]

    def test_all_zero_values(self):
        assert eat(0, 0, 0) == [0, 0]

    def test_large_values(self):
        assert eat(999, 999, 999) == [1998, 0]

    def test_need_equals_remaining(self):
        assert eat(5, 5, 5) == [10, 0]

    def test_need_greater_than_remaining(self):
        assert eat(2, 11, 5) == [7, 0]