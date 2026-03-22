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
    eat_amount = min(need - number, remaining)
    total_eaten = number + eat_amount
    remaining_carrots = remaining - eat_amount
    return [total_eaten, remaining_carrots]

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Basic case: Enough carrots to satisfy need.
# 2. Basic case: Not enough carrots to satisfy need.
# 3. Edge case: No carrots remaining.
# 4. Edge case: Need is already satisfied.
# 5. Edge case: Zero initial eaten carrots.
# 6. Edge case: Zero need.
# 7. Edge case: Zero remaining carrots.
# 8. Boundary case: number = 1000, need = 1000, remaining = 1000
# 9. Boundary case: number = 0, need = 0, remaining = 0
# 10. Boundary case: number = 0, need = 1000, remaining = 1000
# 11. Boundary case: number = 1000, need = 0, remaining = 1000
# 12. Invalid input (negative number, need, remaining) - should not raise errors, but handle gracefully (treat as 0)

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (5, 5, 10, [5, 10]),  # Need already satisfied
    (0, 5, 10, [5, 5]),  # Zero initial eaten carrots
    (5, 0, 10, [5, 10]),  # Zero need
    (5, 6, 0, [5, 0]),  # Zero remaining carrots
    (1000, 1000, 1000, [2000, 0]),  # Boundary case
    (0, 0, 0, [0, 0]),  # Boundary case
    (0, 1000, 1000, [1000, 0]),  # Boundary case
    (1000, 0, 1000, [1000, 1000]),  # Boundary case
    (5, 6, 2, [7, 0]), # Not enough remaining
    (10, 5, 5, [10, 5]), # Need already met
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (-1, 5, 10, [4, 6]),  # Negative number
    (5, -1, 10, [5, 10]),  # Negative need
    (5, 5, -1, [5, 0]),  # Negative remaining
])
def test_eat_negative_inputs(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected