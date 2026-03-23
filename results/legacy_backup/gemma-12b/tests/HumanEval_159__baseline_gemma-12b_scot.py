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
# 1. Test case 1: Enough remaining carrots to satisfy the need.
# 2. Test case 2: Not enough remaining carrots to satisfy the need.
# 3. Test case 3: No remaining carrots.
# 4. Test case 4: Need is zero.
# 5. Test case 5: Number is zero.
# 6. Test case 6: All inputs are zero.
# 7. Test case 7: Boundary conditions for number, need, and remaining.
# 8. Test case 8: Large values for inputs within constraints.

# STEP 3: CODE - Write the high-quality pytest suite.
class TestEat:
    def test_enough_remaining(self):
        assert eat(5, 6, 10) == [11, 4]

    def test_not_enough_remaining(self):
        assert eat(4, 8, 9) == [13, 0]

    def test_no_remaining(self):
        assert eat(1, 10, 0) == [1, 0]

    def test_need_is_zero(self):
        assert eat(2, 0, 5) == [2, 5]

    def test_number_is_zero(self):
        assert eat(0, 10, 10) == [10, 0]

    def test_all_inputs_zero(self):
        assert eat(0, 0, 0) == [0, 0]

    def test_boundary_conditions(self):
        assert eat(1000, 1000, 1000) == [2000, 0]
        assert eat(0, 0, 1000) == [0, 1000]
        assert eat(1000, 0, 0) == [1000, 0]
        assert eat(0, 1000, 0) == [1000, 0]

    def test_large_values(self):
        assert eat(500, 600, 700) == [1200, 100]
        assert eat(999, 999, 999) == [1998, 0]