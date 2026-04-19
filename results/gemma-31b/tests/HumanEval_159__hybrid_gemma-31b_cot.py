
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

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Provided Examples
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    
    # Boundary Cases: Zeroes
    (0, 0, 0, [0, 0]),       # Everything zero
    (0, 5, 10, [5, 5]),      # Started with none, needs some, plenty left
    (5, 0, 10, [5, 10]),     # Started with some, needs none, plenty left
    (5, 5, 0, [5, 0]),       # Started with some, needs some, none left
    (0, 5, 0, [0, 0]),       # Started with none, needs some, none left
    (5, 0, 0, [5, 0]),       # Started with some, needs none, none left
    (0, 0, 10, [0, 10]),     # Nothing eaten, nothing needed, plenty left
    
    # Boundary Cases: Maximum Constraints (1000)
    (1000, 1000, 1000, [2000, 0]), # Max eaten, max need, max stock
    (1000, 0, 1000, [1000, 1000]), # Max eaten, no need, max stock
    (0, 1000, 1000, [1000, 0]),    # None eaten, max need, max stock
    (0, 1000, 0, [0, 0]),          # None eaten, max need, no stock
    (1000, 1000, 0, [1000, 0]),    # Max eaten, max need, no stock
    
    # Logic Cases: Stock vs Need
    (10, 1, 1, [11, 0]),           # Exactly one available and needed
    (10, 1, 2, [11, 1]),           # More available than needed
    (10, 2, 1, [11, 0]),           # Less available than needed
    (10, 1, 1000, [11, 999]),      # Minimal need, huge stock
    (10, 1000, 1, [11, 0]),        # Huge need, minimal stock
    (50, 50, 50, [100, 0]),        # Exact match: need == remaining
    (50, 51, 50, [100, 0]),        # Need just one more than remaining
    (50, 49, 50, [99, 1]),         # Need just one less than remaining
])
def test_eat(number, need, remaining, expected):
    """
    Tests the rabbit's eating logic across a comprehensive set of scenarios:
    - Standard cases from provided examples.
    - Edge cases involving zero values for inputs.
    - Maximum constraint boundaries (1000).
    - Logic variations comparing stock availability against the rabbit's need.
    """
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """Ensures the function returns a list of two integers."""
    result = eat(1, 1, 1)
    assert isinstance(result, list), "Function should return a list"
    assert len(result) == 2, "List should contain exactly two elements"
    assert all(isinstance(x, int) for x in result), "All elements in the list must be integers"