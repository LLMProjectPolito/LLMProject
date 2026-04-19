
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

# The function 'eat' is assumed to be defined in the environment.
# Logic:
# - If remaining >= need: return [number + need, remaining - need]
# - If remaining < need: return [number + remaining, 0]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # --- Provided Examples ---
    (5, 6, 10, [11, 4]),    # Sufficient stock
    (4, 8, 9, [12, 1]),     # Sufficient stock
    (1, 10, 10, [11, 0]),   # Exact stock match
    (2, 11, 5, [7, 0]),     # Insufficient stock

    # --- Boundary Cases: Zeros & Minimal Values ---
    (0, 0, 0, [0, 0]),      # All zeros
    (0, 5, 10, [5, 5]),     # Starting with zero eaten
    (5, 0, 10, [5, 10]),    # No hunger (need=0): nothing eaten, stock remains
    (5, 6, 0, [5, 0]),      # No stock available: nothing eaten, stock stays 0
    (0, 0, 10, [0, 10]),    # No eaten, no need, stock exists
    (0, 5, 2, [2, 0]),      # Start at 0, insufficient stock
    (100, 1, 1, [101, 0]),  # Minimum need, exact stock
    (100, 1, 0, [100, 0]),  # Minimum need, no stock

    # --- Boundary Cases: Limits (1000) ---
    (1000, 1000, 1000, [2000, 0]), # Max constraints, exact match
    (1000, 1, 1000, [1001, 999]),  # Max values, minimal need
    (0, 1000, 1000, [1000, 0]),    # Max need, max stock
    (1000, 1000, 0, [1000, 0]),    # Max eaten, max need, no stock
    (0, 1000, 1, [1, 0]),          # Max need, minimal stock

    # --- Logic Specifics: Buffer and Deficit ---
    (10, 5, 6, [15, 1]),    # Minimal buffer of stock (remaining = need + 1)
    (10, 6, 5, [15, 0]),    # Minimal deficit of stock (remaining = need - 1)
])
def test_eat_logic(number, need, remaining, expected):
    """
    Tests the eat function across a comprehensive matrix of scenarios:
    standard cases, zero-boundaries, maximum constraints, and edge-case logic.
    """
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """
    Ensure the function returns a list containing exactly two integers.
    """
    result = eat(5, 5, 5)
    assert isinstance(result, list), "Output should be a list"
    assert len(result) == 2, "Output list must have exactly 2 elements"
    assert all(isinstance(x, int) for x in result), "All elements in the list must be integers"

def test_eat_immutability():
    """
    Ensure the function does not modify the input arguments.
    """
    n, nd, r = 5, 6, 10
    eat(n, nd, r)
    assert n == 5, "Input 'number' was modified"
    assert nd == 6, "Input 'need' was modified"
    assert r == 10, "Input 'remaining' was modified"