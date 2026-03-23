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
    left_remaining = remaining - eat_amount
    return [total_eaten, left_remaining]

# STEP 2: PLAN - List test functions names and scenarios.
# Test function names:
# - test_eat_enough_carrots
# - test_eat_not_enough_carrots
# - test_eat_exactly_enough_carrots
# - test_eat_zero_initial_eaten
# - test_eat_zero_need
# - test_eat_zero_remaining
# - test_eat_large_numbers
# - test_eat_edge_cases

# Scenarios:
# - Enough carrots to satisfy need
# - Not enough carrots to satisfy need
# - Exactly enough carrots to satisfy need
# - Initial eaten carrots is zero
# - Need to eat is zero
# - Remaining carrots is zero
# - Large numbers within constraints
# - Edge cases (0, 1, max values)

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (0, 5, 10, [5, 5]),
    (5, 5, 0, [5, 0]),
    (5, 0, 10, [5, 10]),
    (100, 200, 300, [300, 0]),
    (999, 1000, 1000, [1999, 0]),
    (0, 0, 0, [0, 0]),
    (1, 1, 1, [2, 0]),
    (1000, 1000, 1000, [2000, 0]),
    (5, 10, 3, [8, 0]),
    (7, 3, 5, [7, 0])
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_zero_initial_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 5, 0) == [5, 0]

def test_eat_large_numbers():
    assert eat(100, 200, 300) == [300, 0]

def test_eat_edge_cases():
    assert eat(999, 1000, 1000) == [1999, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(1, 1, 1) == [2, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]