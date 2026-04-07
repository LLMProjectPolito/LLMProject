
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `eat` calculates the total number of carrots eaten and the remaining carrots after a meal.
# It takes three integer arguments: `number` (already eaten), `need` (carrots needed), and `remaining` (carrots in stock).
# The function returns a list containing the total carrots eaten and the remaining carrots.
# If the remaining carrots are less than the needed carrots, all remaining carrots are eaten, and the remaining carrots after the meal is 0.
# Constraints: 0 <= number <= 1000, 0 <= need <= 1000, 0 <= remaining <= 1000.

# STEP 2: PLAN - List test functions names and scenarios.
# 1. Test with enough remaining carrots: `test_enough_remaining`
# 2. Test with not enough remaining carrots: `test_not_enough_remaining`
# 3. Test with zero remaining carrots: `test_zero_remaining`
# 4. Test with zero needed carrots: `test_zero_needed`
# 5. Test with zero already eaten carrots: `test_zero_eaten`
# 6. Test with all inputs being zero: `test_all_zero`
# 7. Test boundary conditions for inputs (max values): `test_max_values`
# 8. Test with large numbers within constraints: `test_large_numbers`

# STEP 3: CODE - Write the high-quality pytest suite.
class TestEat:
    def test_enough_remaining(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_not_enough_remaining(self):
        assert eat(4, 8, 9) == [13, 0]

    def test_zero_remaining(self):
        assert eat(1, 10, 0) == [1, 0]

    def test_zero_needed(self):
        assert eat(2, 0, 5) == [2, 5]

    def test_zero_eaten(self):
        assert eat(0, 10, 10) == [10, 0]

    def test_all_zero(self):
        assert eat(0, 0, 0) == [0, 0]

    def test_max_values(self):
        assert eat(1000, 1000, 1000) == [2000, 0]

    def test_large_numbers(self):
        assert eat(500, 600, 700) == [1200, 100]