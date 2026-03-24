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
### Test cases:
### 1. Basic case: enough carrots to satisfy the need.
### 2. Not enough carrots: eat all remaining carrots.
### 3. Need is zero.
### 4. Number of eaten carrots is zero.
### 5. Edge cases: number, need, and remaining are all zero.
### 6. Edge cases: number, need, and remaining are all maximum values.
### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 3: CODE - Write the high-quality pytest suite.

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_need_is_zero():
    assert eat(5, 0, 10) == [5, 5]

def test_eat_number_is_zero():
    assert eat(0, 6, 10) == [6, 4]

def test_eat_all_zero():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_not_enough_carrots_all_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_need_greater_than_remaining():
    assert eat(0, 10, 5) == [10, 0]

def test_eat_number_greater_than_remaining():
    assert eat(10, 5, 5) == [15, 0]