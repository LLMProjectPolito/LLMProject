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
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `eat` calculates the total carrots eaten and the remaining carrots after eating.
### It handles the case where there are not enough carrots to satisfy the need.
### The function should return a list containing the total eaten carrots and the remaining carrots.
### The input parameters are integers within the range [0, 1000].
### STEP 2: PLAN - List test functions names and scenarios.
### test_eat_sufficient_carrots() - Tests cases where there are enough carrots to satisfy the need.
### test_eat_insufficient_carrots() - Tests cases where there are not enough carrots to satisfy the need.
### test_eat_zero_need() - Tests cases where the need is zero.
### test_eat_zero_remaining() - Tests cases where the remaining carrots are zero.
### test_eat_edge_cases() - Tests edge cases with number, need, and remaining close to the boundaries.

### STEP 3: CODE - Write the high-quality pytest suite.
### test_eat_sufficient_carrots
def test_eat_sufficient_carrots():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

### test_eat_insufficient_carrots
def test_eat_insufficient_carrots():
    assert eat(5, 6, 3) == [11, 0]
    assert eat(10, 5, 2) == [15, 0]

### test_eat_zero_need
def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 5]
    assert eat(0, 0, 10) == [0, 10]

### test_eat_zero_remaining
def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [11, 0]
    assert eat(0, 6, 0) == [6, 0]

### test_eat_edge_cases
def test_eat_edge_cases():
    assert eat(0, 0, 0) == [0, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(0, 1000, 1000) == [1000, 0]
    assert eat(1000, 0, 1000) == [1000, 1000]